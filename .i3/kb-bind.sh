#!/usr/local/bin/zsh

winid=$(xdotool getactivewindow)
is_browser=$(xprop -id $winid WM_CLASS | grep -ci "\(chrom\|firefox\)")

if [ $is_browser -eq 1 ]; then
    xdotool getactivewindow key $1
else
    xdotool getactivewindow key $2
fi