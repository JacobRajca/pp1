hour_24 = input('Enter time (24-hour format): ')
only_hour = int(hour_24[0:2])

if only_hour > 12 and only_hour < 24:
    print(f'Time in 12-hour format: {only_hour-12}:{hour_24[3:5]}pm')
else:
    print(f'Time in 12-hour format: {only_hour}:{hour_24[3:5]}am')