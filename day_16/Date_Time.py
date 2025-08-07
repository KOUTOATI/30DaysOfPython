from datetime import datetime, timedelta

#Get current date and time details
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(f"Current Date: {day}/{month}/{year}, Time: {hour}:{minute}, Timestamp: {timestamp}")

#Format current date
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Formatted Date: {formatted_date}")
#Convert time string to datetime
date_str = "5 December, 2019"
print(f"Date String: {date_str}")
converted_time = datetime.strptime(date_str, "%d %B, %Y")
print(f"Converted Time: {converted_time}")

#Time difference between now and next New Year
next_new_year = datetime(year=now.year + 1, month=1, day=1)
print(f"Next New Year: {next_new_year}")
time_until_new_year = next_new_year - now
print(f"Time until next New Year: {time_until_new_year}")
#Time difference since 1 January 1970
epoch = datetime(1970, 1, 1)
time_since_epoch = now - epoch
print(f"Time since epoch (1 Jan 1970): {time_since_epoch}")

# Uses of datetime:
""""
- Time series analysis (e.g., stock data, logs)
- Logging user activity timestamps
- Scheduling or time-based triggers
- Formatting dates in UIs
- Age calculation or duration
"""

