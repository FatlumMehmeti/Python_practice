import calendar
print(calendar.calendar(2020))
print("#############################################################")
calendar.prcal(2020)
print("#############################################################")
print(calendar.month(2020, 11))
calendar.prmonth(2020,11)

print("#############################################################")
calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2020, 12)

print("#############################################################")
print(calendar.weekday(2020, 12, 24))

print("#############################################################")
print(calendar.weekheader(3))

print("#############################################################")
print(calendar.isleap(2020))
print(calendar.leapdays(2010, 2021))  # Up to but not including 2021.

print("#############################################################")
c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")

print("#############################################################")
c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")

print("#############################################################")

c = calendar.Calendar()

for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")
for iter in c.itermonthdays2(2019, 11):
    print(iter, end=" ")
for iter in c.itermonthdays3(2019, 11):
    print(iter, end=" ")
for iter in c.itermonthdays4(2019, 11):
    print(iter, end=" ")

print("#############################################################")
c = calendar.Calendar()

for data in c.monthdays2calendar(2020, 12):
    print(data)

print("#############################################################")

class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        count = 0
        for month in range(1, 13):
            for week in self.monthdays2calendar(year, month):
                for day, day_of_week in week:
                    if day != 0 and day_of_week == weekday:
                        count += 1
        return count
my_cal = MyCalendar()
print(my_cal.count_weekday_in_year(2019, 0))  
print("#############################################################")