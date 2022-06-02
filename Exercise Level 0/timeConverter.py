# Get a number of seconds from the user.
second = float(input('Seconds: '))

# Get the number of hours.
hours = second // 3600

# Get the number of remaining minutes.
minutes = (second // 60) % 60

# Get the number of remaining seconds.
seconds = second % 60

# Display the results.
print('Here is the time in hours, minutes, and seconds:')
print('Hours:', hours)
print('Minutes:', minutes)
print('Seconds:', seconds)


