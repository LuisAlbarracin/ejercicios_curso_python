import datetime

my_time = datetime.datetime.now()
print(my_time)

# Formato UTC
other_time = datetime.datetime.utcnow()
print(other_time)

my_day = datetime.date.today()
print(my_day)

print(f'Year: {my_day.year}')
print(f'Month: {my_day.month}')
print(f'Day: {my_day.day}')
