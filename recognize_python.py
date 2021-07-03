num1 = 42 # variable declaration, Number
num2 = 2.3 # variable declaration, Number
boolean = True # variable declaration, boolean
string = 'Hello World' # variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, dictionary 
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, tuples
print(type(fruit)) #log statement, type check
print(pizza_toppings[1]) # log statement, access value
pizza_toppings.append('Mushrooms') # add value
print(person['name']) #log statement, access value 
person['name'] = 'George' # change value 
person['eye_color'] = 'blue' # change value
print(fruit[2]) #log statement, access value

if num1 > 45: #conditional if and else statements
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5: # conditional if, else if, and else statements
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):  # for loop, 5 iterations. starts at 0 and ends at 4
    print(x)
for x in range(2,5): # for loop, 3 iterations. starts at 2
    print(x)
for x in range(2,10,3): # for loop, goes till 9, starts at 2, iterates 3 at a time
    print(x)
x = 0
while(x < 5): # while loop, if x is less then 5 do this thing then add one to x
    print(x)
    x += 1

pizza_toppings.pop() # deletes value
pizza_toppings.pop(1) # deletes value of list index position

print(person)   #log statement      
person.pop('eye_color') #deletes value
print(person) #log statement of new value without "eye_color"

for topping in pizza_toppings: # this is a loop which loops for the length of the list specified. it stops when it sees "olives"
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): #function with log statement that prints hello ten times
    for num in range(10):
        print('Hello')

print_hello_ten_times() #function call

def print_hello_x_times(x):  # function with log statement that prints hello x times
    for num in range(x):
        print('Hello')

print_hello_x_times(4)  #function call with argument 

def print_hello_x_or_ten_times(x = 10): # function with default argument peramaters 
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #two function calls, the first one provides the default which is ten.
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)  name error variable not defined 
# num3 = 72    declaring variable 
# fruit[0] = 'cranberry'   TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])  KeyError: 'favorite_team'
# print(pizza_toppings[7])   IndexError: list index out of range
#   print(boolean)     IndentationError: unexpected indent
# fruit.append('raspberry') AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)   AttributeError: 'tuple' object has no attribute 'pop'