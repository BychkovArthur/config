vim.g.did_load_filetypes = 1             -- Отключить автоопределение типа файлов. Предполагается, что файл уже загружен ?? 
vim.g.formatoptions = "qrn1"             -- ??  
vim.opt.showmode = false                 -- Отключение отображения текущего режима внизу 
vim.opt.updatetime = 100                 -- Время обновления экрана       ??
vim.wo.signcolumn = "yes"                -- Отображать колонку для знаков ??
vim.opt.scrolloff = 8                    -- То, сколько строк видно при прокрутке
vim.opt.wrap = false                     -- Отключение переноса строки. Получается горизонтальная прокрутка.
vim.wo.linebreak = true                  -- Если перенос включен, то он работает по словам, а не буквам
vim.opt.virtualedit = "block"            -- ?? 
vim.opt.undofile = true                  -- undo можно применять даже после закрытия
vim.opt.shell = "/bin/zsh"               -- Будет использоваться в `:!` и `:termial`  


-- Line number
vim.wo.number = true                     -- Показ номеров
vim.wo.relativenumber = true             -- Сделать номера относительными


-- Mouse
vim.opt.mouse = "a"                      -- Мышь будет работать во a (all) режимах.
vim.opt.mousefocus = true                -- Устанавливать фокус на окно, где тыкнул мышью. Нет, это не так работает... ???


-- Splits
vim.opt.splitbelow = true
vim.opt.splitright = true


-- Clipboard
vim.opt.clipboard = "unnamedplus"        -- Общий буфер обмена ??         


-- Shorter messages
vim.opt.shortmess:append("c")            -- ??


-- Indent Settings
vim.opt.expandtab = true                 -- tab = spaces
vim.opt.shiftwidth = 4                   -- ??
vim.opt.tabstop = 4                      -- ??
vim.opt.softtabstop = 4                  -- ?? 
vim.opt.smartindent = true               -- Отступ для новых строк на основе предыдущих


-- Fillchars
vim.opt.fillchars = {
    vert = "│",
    fold = "⠀",
    eob = " ", -- suppress ~ at EndOfBuffer
    -- diff = "⣿", -- alternatives = ⣿ ░ ─ ╱
    msgsep = "‾",
    foldopen = "▾",
    foldsep = "│",
    foldclose = "▸"
}

vim.cmd([[highlight clear LineNr]])
vim.cmd([[highlight clear SignColumn]])
