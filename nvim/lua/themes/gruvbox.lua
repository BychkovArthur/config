return {

	{
		"ellisonleao/gruvbox.nvim",
		priority = 1000,
		opts = {
						
		},
		config = function(_, opts)
			require("gruvbox").setup(opts)			
			vim.o.background = "dark" -- Can be light
			vim.cmd("colorscheme gruvbox")
		end,
	},
}
