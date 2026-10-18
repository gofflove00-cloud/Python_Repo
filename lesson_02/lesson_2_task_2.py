def is_year_leap(year):
    return True if year % 4 == 0 else False


leap = int(input('введите год: '))
result = is_year_leap(leap)
print(f"год {leap}: {result}")
