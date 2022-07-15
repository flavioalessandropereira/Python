import datetime as dt

natal = dt.date(2022, 12,25)
reveillon = dt.date(2023, 1, 1)

print(reveillon-natal)
print((reveillon-natal).days)
print((reveillon-natal).seconds)
print((reveillon-natal).microseconds)