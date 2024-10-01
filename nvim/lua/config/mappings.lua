vim.g.mapleader = " "


-- NeoTree
vim.keymap.set("n", "<leader>df", ":Neotree float focus<CR>", { silent = true }) -- dirs float
vim.keymap.set("n", "<leader>dl", ":Neotree left focus<CR>", { silent = true })  -- dirs left


-- My mappings
vim.keymap.set("i", "<C-Right>", "<Esc>ea", { silent = true, noremap = true })
vim.keymap.set("i", "<C-z>", "<Esc>ua", { silent = true, noremap = true })

