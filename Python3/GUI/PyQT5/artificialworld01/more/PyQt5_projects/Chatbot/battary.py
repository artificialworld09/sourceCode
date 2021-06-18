import psutil

battery=psutil.sensors_battery()
percentage=battery.percent
per=str(percentage)[0:5]
percent=float(per)

# print(percent)

if percent>=75:
    print('We have enough power to continue our work')
elif (percent>=40) and (percentage<=75):
    print('We should connect our system to charging point to charge our battery')
elif (percent>=15) and (percentage<=30):
    print("We don't have enough power to work, please connect to charging")
elif percent<=15:
    print("we have very low power, please connect to charging the system will shutdown very soon")