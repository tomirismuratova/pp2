import datetime

date1 = datetime.datetime(2025, 10, 8, 12, 0, 0)
date2 = datetime.datetime(2025, 10, 8, 12, 30, 0)
x = (date2 - date1).total_seconds()
print("Difference in seconds:", x)
