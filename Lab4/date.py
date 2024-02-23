from datetime import datetime, timedelta

current_date = datetime.now()

five_days_ago = current_date - timedelta(days=5)

print("Five days ago was:", five_days_ago)

today = datetime.now()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday was:", yesterday)
print("Today is:", today)
print("Tomorrow will be:", tomorrow)

current_datetime = datetime.now()

current_datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Datetime without microseconds:", current_datetime_without_microseconds)

date1 = datetime(2024, 2, 20, 12, 0, 0)
date2 = datetime(2024, 2, 24, 12, 0, 0)

difference = date2 - date1

difference_seconds = difference.total_seconds()

print("Difference between the two dates in seconds:", difference_seconds)