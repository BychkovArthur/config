return {

    {
        "WhoIsSethDaniel/mason-tool-installer.nvim",

        opts = {
            
            ensure_installed = {

                "lua-language-server",
                "vim-language-server",
                "clangd",
                "clang-format",

            },
            auto_update = true,       -- Автообновление/автоустановка всего
            run_on_start = true,      -- Запуск автообновления при старте
            start_delay = 0,          -- Задержка до запуска обновления
            debounce_hours = 5,       -- Чтобы часто не проверять обновление

        }

    }

}
