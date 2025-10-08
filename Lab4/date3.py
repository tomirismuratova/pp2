import datetime

now = datetime.datetime.now()
result = now.replace(microsecond=0)

print("With microseconds:", now)
print("Without microseconds:", result)
