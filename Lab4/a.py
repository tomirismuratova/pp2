import datetime

today = datetime.date.today()
day = today.strftime("%A")
if day in ["Saturday", "Sunday"]:
    print("weekend:", day)
else:
    print("weekday:", day)
