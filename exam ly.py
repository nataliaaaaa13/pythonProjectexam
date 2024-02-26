# What does the following code print?
print(2*3+5*6)

# What will the following code print?
print(3+10**2/2)

# Write a function that checks if the passed parameters is a valid URL or not. Please also explain your reasoning

# Here is some code: continue by replacing the numbers greater than 80 with their corresponding negative value (90 will be replaced with -90). Print the last at the end
import random
random_numbers = []
for i in range (10):
    random_numbers.append(random.randint(1,100))
for i in range(len(random_numbers)):
    if random_numbers[i] > 80:
        random_numbers[i] = -random_numbers[i]
print(random_numbers[-1])

#What is the maximum value that this code can print? Besides giving the correct answer, please explain your reasoning
import datetime
import random
today = datetime.date.today()
start_of_year = datetime.date(today.year, 1, 1)
day_of_year = (today - start_of_year).days + 1

sum = 0
for i in range(day_of_year//10):
    sum += random.randint(1, day_of_year//7)
print (sum)

max_value = (day_of_year // 10) * (day_of_year // 7)
print(max_value)

# Here is a function that needs to determine if a number is smaller, greater or equal to another number. I have written the beginning, please continue and paste the entire function in the answers box
def compare(first, second):
    if first == second:
        print(f"{first} = {second}")
    elif first > second:
        print(f"{first} is greater than {second}")
first = int(input("Input first number:"))
second = int(input("Input second number:"))
compare(first, second)

# What will be the value of a at the end of the code? The answer is 2
a = 6
a = a -2
print(a*2)
a = a*2
print(a +1)
a = a//3

# Here is a function that determines if a number is palindrome or not. The answer is 74896...
def palindrome (word):
    if word == word[::-1]:
        return True
    else:
        return False

# Explain what it means that a list is mutable, and a string is not mutable (immutable). Give some code that shows the difference
# Mutable list
mutable_list = [1, 2, 3, 4, 5]
mutable_list[2] = 10
mutable_list.append(6)
mutable_list.remove(4)
print("Mutable List:", mutable_list)

# Immutable string
immutable_string = "Hello"
new_string = immutable_string + " World"
print("Original Immutable String:", immutable_string)
print("New String:", new_string)

#Fill in what the code below prints (all the lines) abcabcabcabc (this is d)
a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)

c = a + b
print(c)

d = "abc" + (c//3)
print(d)