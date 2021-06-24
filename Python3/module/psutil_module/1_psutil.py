import psutil

battery=psutil.sensors_battery()
percentage=battery.percent
print(type(percentage))

print(f"sir our system have {percentage} percent battery")