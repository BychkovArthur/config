return {

	{
		"nvim-treesitter/nvim-treesitter",
		opts = {
			ensure_installed = {"c", "cpp", "lua", "python", },
			sync_install = false,
			auto_install = true,
			highlight = {
				enable = true,
			},
		},
		-- Надо обновлять все парсеры при обновлении самого TreeSitter
		-- https://github.com/nvim-treesitter/nvim-treesitter?tab=readme-ov-file#installation
		build = ":TSUpdate",
		config = function(_, opts)
			require("nvim-treesitter.configs").setup(opts)
		end,
	},

}
