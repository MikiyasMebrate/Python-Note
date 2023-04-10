from datetime import datetime

now = datetime.now()
print(now)
print(now.day)
print(now.month)
print(now.year)
print(now.hour)
print(now.minute)
print(now.second)


print(str(now.day)+'/'+str(now.month)+'/'+str(now.year))