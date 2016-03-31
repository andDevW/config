#!/usr/bin/zsh

SLEEP_TIME=5
SAFE_PERCENT=20
DANGER_PERCENT=8
CRITICAL_PERCENT=3

export DISPLAY=:0.0

function launchNagBar {
    i3-nagbar -m 'Battery low!' -b 'Hibernate' 'pm-hibernate' >/dev/null 2>&1 &
    echo $! > /tmp/i3nagbar-pid
}

function killNagBar {
    if ! [[ -a /tmp/i3nagbar-pid ]]; then
        echo "0" > /tmp/i3nagbar-pid
    fi

    NAGBAR_PID=$(cat /tmp/i3nagbar-pid 2>/dev/null)

    if [[ $NAGBAR_PID -ne 0 ]]; then
        ps -p $NAGBAR_PID | grep "i3-nagbar"
        if [[ $? -eq 0 ]]; then
            kill $NAGBAG_PID
        fi
        echo $NAGBAR_PID > /tmp/i3nagbar-pid
    fi
}

function checkBattery {
    killNagBar

    echo "checking ..." >> /tmp/check-errors

    rem_bat=$(acpi -b | grep -Eo "[0-9]+%" | grep -Eo "[0-9]+")
    if [[ $rem_bat -le $DANGER_PERCENT ]]; then
        launchNagBar
    fi

    if [[ $rem_bat -le $CRITICAL_PERCENT ]]; then
        pm-hibernate
    fi

    echo "done checking ..." >> /tmp/check-errors
}

case $1 in
    true)
        sudo crontab -l -u gregg > /tmp/gregg-cron
        echo "* * * * * /home/gregg/.local/bin/check-battery.sh check >> /tmp/check-errors" >> /tmp/gregg-cron
        sudo crontab -u gregg /tmp/gregg-cron
    ;;
    false)
        sudo crontab -l -u gregg > /tmp/gregg-cron
        last_line=$(tail -1 /tmp/gregg-cron)
        if echo $last_line | grep --quiet check-battery.sh; then
            echo match
            head -n 1 /tmp/gregg-cron > /tmp/gregg-cron-tmp ; mv /tmp/gregg-cron-tmp /tmp/gregg-cron
            sudo crontab -u gregg /tmp/gregg-cron
        fi
    ;;
    check) checkBattery ;;
    *) exit
esac

exit 0
