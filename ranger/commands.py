# This is a sample commands.py.  You can add your own commands here.
#
# Please refer to commands_full.py for all the default commands and a complete
# documentation.  Do NOT add them all here, or you may end up with defunct
# commands when upgrading ranger.

# A simple command for demonstration purposes follows.
# -----------------------------------------------------------------------------

from __future__ import (absolute_import, division, print_function)

# You can import any python module as needed.
import os

# You always need to import ranger.api.commands here to get the Command class:
from ranger.api.commands import Command


# Any class that is a subclass of "Command" will be integrated into ranger as a
# command.  Try typing ":my_edit<ENTER>" in ranger!
class my_edit(Command):
    # The so-called doc-string of the class will be visible in the built-in
    # help that is accessible by typing "?c" inside ranger.
    """:my_edit <filename>

    A sample command for demonstration purposes that opens a file in an editor.
    """

    # The execute method is called when you run this command in ranger.
    def execute(self):
        # self.arg(1) is the first (space-separated) argument to the function.
        # This way you can write ":my_edit somefilename<ENTER>".
        if self.arg(1):
            # self.rest(1) contains self.arg(1) and everything that follows
            target_filename = self.rest(1)
        else:
            # self.fm is a ranger.core.filemanager.FileManager object and gives
            # you access to internals of ranger.
            # self.fm.thisfile is a ranger.container.file.File object and is a
            # reference to the currently selected file.
            target_filename = self.fm.thisfile.path

        # This is a generic function to print text in ranger.
        self.fm.notify("Let's edit the file " + target_filename + "!")

        # Using bad=True in fm.notify allows you to print error messages:
        if not os.path.exists(target_filename):
            self.fm.notify("The given file does not exist!", bad=True)
            return

        # This executes a function from ranger.core.acitons, a module with a
        # variety of subroutines that can help you construct commands.
        # Check out the source, or run "pydoc ranger.core.actions" for a list.
        self.fm.edit_file(target_filename)

    # The tab method is called when you press tab, and should return a list of
    # suggestions that the user will tab through.
    # tabnum is 1 for <TAB> and -1 for <S-TAB> by default
    def tab(self, tabnum):
        # This is a generic tab-completion function that iterates through the
        # content of the current directory.
        return self._tab_directory_content()


class yank_content(Command):
    # TODO: Maybe, add tab method?
    
    """:yank_content [-FLAGS...]

    Copies the contents of marked files.
    By default, files are marked as in `yank`.

    Flags:
     -a, --all-directories
        All files marked with the tag elements will be copied.
        By default this is the 'C' tag.
        
     -t <TAG>, --tag=<TAG>
        What tag to tag a file when copying `all-directories`.
        The tag must consist of 1 character.
        Doesn't affect anything unless the all-directories flag is set.
        
     -r, --remove-tags
        After copying, remove the tag from the marked files.
        Doesn't affect anything unless the all-directories flag is set.
    """
    
    def execute(self):
        import subprocess
        
        try:
            flags = self.__parse_flags(self.rest(1))
        except ValueError as e:
            self.fm.notify(
                f'Flag parse error: {e}',
                bad=True
            )
            return
        
        clipboard_commands = self.__clipboards()
        if clipboard_commands is None:
            self.fm.notify(
                'Clipboard manager absent. Install one of: [xclip, ]',
                bad=True
            )
            return
            
        selection = self.__get_selection(flags)
        new_clipboard_contents = '\n'.join(selection)
        
        with subprocess.Popen(
            clipboard_commands, universal_newlines=True, stdin=subprocess.PIPE
        ) as process:
            process.communicate(input=new_clipboard_contents)
        
        if flags.all_directories and flags.remove_tags:
            self.__remove_tags(flags.tag)
        
    def __parse_flags(self, flag_string):
        import argparse
        import shlex
        
        parser = argparse.ArgumentParser(
            description='Parses yank_content flags',
            add_help=False,
            exit_on_error=False,
        )

        parser.add_argument(
            '-a', '--all-directories', action='store_true',
            help='Copy all files marked with the tag (default tag: \'C\').'
        )
        parser.add_argument(
            '-t', '--tag', type=str, default='C',
            help='Specify the tag to use when copying all directories. Must be a single character.'
        )
        parser.add_argument(
            '-r', '--remove-tags', action='store_true',
            help='Remove tags from marked files after copying.'
        )
        
        args, unknown_args = parser.parse_known_args(shlex.split(flag_string))
        if args.tag and len(args.tag) != 1:
            raise ValueError('The tag must be a single character.')
        if len(unknown_args) > 0:
            raise ValueError('Invalid arguments.')
        
        return args
    
    @staticmethod
    def __clipboards():
        from ranger.ext.get_executables import get_executables
        
        # TODO: Add support of `wl-copy`, `pbcopy`
        clipboard_managers = {
            'xclip': ['xclip', '-selection', 'clipboard', '-t', 'text/uri-list'],
        }
        ordered_managers = ['xclip']
        executables = get_executables()
        
        for manager in ordered_managers:
            if manager in executables:
                return clipboard_managers[manager]
    
    def __get_selection(self, flags):
        if flags.all_directories:
            return self.__get_selection_by_tag(flags.tag)
        else:
            return self.__get_selection_by_mark()
        
    def __get_selection_by_tag(self, tag):
        return [f'file://{path_}' for path_, tag_ in self.fm.tags.tags.items() if tag_ == tag]
    
    def __get_selection_by_mark(self):
        return [f'file://{file.path}' for file in self.fm.thistab.get_selection()]
        
    def __remove_tags(self, tag):
        files = [path_ for path_, tag_ in self.fm.tags.tags.items() if tag_ == tag]
        self.fm.tags.remove(*files)
        self.fm.ui.redraw_main_column()