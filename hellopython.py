# arrays ----------------------------------------
people = ['John' , 'Jane' , 'Joe']

people.append('Jackson')

print(people)

name = people.pop()

print(name)
print(people)

people.remove('Jane')

print(people)

people.append(9)

print(people)

# append without append function ----------------------------------------

people_tuple = ('Jamie', 'Jackie')

print(people_tuple)

people_tuple = ('Jamie', 'Jackie', 'Jason')

print(people_tuple)

# if statements ----------------------------------------
i = 28

if i >= 18:
  print("Okeeey let's go")
else:
  print("MI DISSOCIO")

age = 28

if age < 19:
  print('The person is a child')
elif age < 70:
  print('The person is an adult')
else:
  print('The person is a senior citizen')

# for loop ----------------------------------------
for i in range(3):
  print("Hello Phyton")

i = 6

peoples = ['John', 'Jane', 'Joe']

for name in peoples:
  print(name)

# while loop ----------------------------------------
while i > 0:
  print("I am working")
  i = i - 1
print("I stopped working")

user_input = input('random ')

while user_input != 'exit':
  user_input = input('>>> ')
  print('You entered: ', user_input)

print('Goodbye!')

# declaring a function -------------------------
def add_two_numbers(x, y):
  total = x + y
  return total

output = add_two_numbers(1, 2)
print(output)

def print_sq_value(numbers):
  for n in numbers:
    sq = n*n
    print('Square of', n, 'is', sq)

numbers = [1, 2, 3, 4, 5]

print_sq_value(numbers)
