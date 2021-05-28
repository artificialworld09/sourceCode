import psutil

battery=psutil.sensors_battery()
percentage=battery.percent
print(f"sir our system have {percentage} percent battery")