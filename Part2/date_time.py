print("#############################################################")
from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
print()
my_date = date(2019, 11, 4)
print(my_date)
print("#############################################################")
import time

timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)
print("#############################################################")
d = date.fromisoformat('2019-11-04')
print(d)

print("#############################################################")
d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)

print("#############################################################")

d = date(2019, 11, 4)
print(d.weekday())

print("#############################################################")
from datetime import time
t = time(14, 53, 20, 1)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)

print("#############################################################")
import time

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")

student = Student()
student.take_nap(2)

print("#############################################################")
timestamp = 1572879180
print(time.ctime())

print("#############################################################")
timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.asctime(st))
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))

print("#############################################################")
from datetime import datetime

dt = datetime(2019, 11, 4, 14, 53)

print("Datetime:", dt)
print("Date:", dt.date())
print("Time:", dt.time())

print("#############################################################")
from datetime import datetime

print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.utcnow())

print("#############################################################")

dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())

print("#############################################################")
d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

print("#############################################################")
from datetime import time
from datetime import datetime

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))

print("#############################################################")
timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))

print("#############################################################")
from datetime import datetime
print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

print("#############################################################")
d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)

print("#############################################################")
from datetime import timedelta

delta = timedelta(weeks=-2, days=-2, hours=-3)
print(delta)
delta = timedelta(weeks=2, days=2, hours=3)
print("Days:", delta.days)
print("Seconds:", delta.seconds)
print("Microseconds:", delta.microseconds)
print("#############################################################")
from datetime import datetime

dt = datetime(2020, 11, 4, 14, 53, 0)
print(dt.strftime("%Y/%m/%d %H:%M:%S"))
print(dt.strftime("%y/%B/%d %H:%M:%S %p"))
print(dt.strftime("%a, %Y %b %d"))
print(dt.strftime("%A, %Y %B %d"))
print("Weekday:", dt.weekday() + 1)  # Monday=0 → add 1 to match example
print("Day of the year:", dt.strftime("%j"))
print("Week number of the year:", dt.strftime("%U"))

print("#############################################################")
