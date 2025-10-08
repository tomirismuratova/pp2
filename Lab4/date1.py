import datetime

today = datetime.date.today()
new_date = today - datetime.timedelta(days=5)
print("Current date:", today)
print("Date five days ago:", new_date)
