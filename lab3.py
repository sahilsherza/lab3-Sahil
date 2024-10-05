# Define a function that prints some text

def hello():

    print('Hello World')

    print('Inside a Function')

# Call the hello function three times

hello()

hello()

hello()

my_stuff = hello()

print('Stuff returned from hello():', my_stuff)

print('The object my_stuff is of type:', type(my_stuff))

def return_text_value():

        name = 'Terry'

        greeting = 'Good Morning ' + name

        return greeting



text = return_text_value()

print(text)

# Part 3 - Function that does not take arguments but returns a number

def return_number_value():

    num1 = 10

    num2 = 5

    num3 = num1 + num2

    return num3

# Call the return_number_value function

number = return_number_value()

print(number)                     # Prints the returned number (15)

print(number + 5)                # Prints 20

print(return_number_value() + 10) # Prints 25




# Displaying both strings and numbers correctly

print('my number is', number)     

print('my number is ' + str(number)) 

print('my number is ' + str(return_number_value()))




