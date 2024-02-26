a = 10
a = a + 2
print(a*2)
a = 19
print(a+3)
a = a // 2

print((2+3)*6/2 and 18.0)

import datetime
a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year
print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

import random
random_numbers = []
for i in range (10):
    random_numbers.append(random.randint(1,100))
for i in range(len(random_numbers)):
    if random_numbers[i] > 80:
        random_numbers[i] = -random_numbers[i]
print(random_numbers[-1])

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
print (palindrome("4257304920394478392772938744930294037524"))

s = "http://google.com"
start = 0
while True:
    start = s.find("http://", start)
    if start == 1:
        break
    end = s.find(" ", start)
    if end == -1:
        print(s[start:])
        break
    print(s[start:end])
    start = end


def days_since_birthday(birthday):
    day, month, year = map(int, birthday.split('-'))
    current_day = 26
    current_month = 2
    current_year = 2024
    days_in_birth_year = 365 - (day + sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:month - 1]))
    days_in_current_year = current_day + sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:current_month - 1])
    whole_years = current_year - year - 2
    total_days_passed = whole_years * 365 + days_in_birth_year + days_in_current_year
    return total_days_passed
birthday = "11-11-2004"
result = days_since_birthday(birthday)
print(f"Days passed since {birthday}: {result} days")


def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def count_pattern_occurrences(text):
    match_count = 0
    i = 0
    while i < len(text):

        if text[i:i + 2] == "un":

            i += 2
            while i < len(text) and text[i].isalpha():
                i += 1
            if i < len(text) and text[i:i + 2] == "an":
                match_count += 1
                i += 2
            else:
                i += 1
        else:
            i += 1

    return match_count

