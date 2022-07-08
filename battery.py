# pip install psutil
import psutil

battery = psutil.sensors_battery()
plugged = batter.power_plugged
percent = battery.percent

if percent >= 30:

    # pip install py-notifier
    # pip install win10toast
    from pynotifier import Notification

    Notification(
        title = "Battery Low",
        description=str(percent) + "% Batter remain!",
        duration = 5, # Duration in seconds
        urgency = Notification.URGENCY_CRITICAL,
        icon = "battery.png"
    ).send()
    