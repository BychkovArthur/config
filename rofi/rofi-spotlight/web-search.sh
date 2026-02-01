#!/usr/bin/env bash

MY_PATH="$(realpath "$0" | xargs dirname)"

# Pass the argument to python script
function web_search() {
	# Pass the search query to web-search script
	"${MY_PATH}/web-search.py" "${1}"
	exit;
}

# Handles the web search method
if [ ! -z "$@" ]
then
	# Search directly from your web browser
	web_search "$(printf '%s\n' "${1}")"
	exit
fi
