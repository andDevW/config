#!/usr/local/bin/zsh
running=$(ps aux | grep "emacs --daemo[n]" | wc -l)
if [ $running -eq 0 ]; then
    urxvt -e emacs --daemon
fi
emacsclient "$0"