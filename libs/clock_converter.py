#function that receives time as a string
def clock_converter(time_str):
    # Split hour, minute, and period
    time_parts = time_str.split(':')

#used tuple unpacking 
    hour_str, minute_period = time_parts
    # spilt minutes and period
    minute_str, period = minute_period.split()

    # Convert hour and minute to integers
    hour = int(hour_str)
    minute = int(minute_str)

    # Check if the period is "am"
    if period.lower() == "am":
      #the nested if check it 12 if true it will return 0
        if hour == 12:
            hour = 0  # Midnight
    # Check if the period is "pm"
    else:
      #if the period is greater than 12 i will add 12
        if hour > 12:
            hour += 12 

    # Format the time in 24-hour format as a four-digit string
    time_24_hour = f"{hour:02d}{minute:02d}"

    return time_24_hour

#test example
print( clock_converter("8:10 am"))
print( clock_converter("12:10 am"))
print(clock_converter("8:10 pm"))
print(clock_converter("11:10 pm"))

