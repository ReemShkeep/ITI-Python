

#1. # 1st way 
# def reverse_string(st):
#    print (st[::-1])
# reverse_string("hello")
# # 2nd
# def reverse_str():
#    st = str(input("enter the wanted reverse word: " ))
#    return st[::-1]
# print(reverse_str())


# #3rd way  
# def convert (): 
#    st = str(input("enter the word you want to reverse it: " ))
#    # st=str(n)
#    result=[]
#    for word in st:
#       result.append(str(word))
#    result.reverse()
#    return result      
   
# print(convert())

############################################################
#2.
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# print("Sum: ", num1 + num2)
# print("Difference: ", num1 - num2)
# print("Product: ", num1 * num2)
# print("Quotient: ", num1 / num2)

############################################################

# #3. the function take from the user  a list of integers as input and returns the largest number in the list
 

#########################

# def find_largest_number():
#     num_list = input("Enter a list of integers separated by spaces: ").split()
#     num_list = [int(num) for num in num_list]  # convert input string to a list of integers
#     return max(num_list)
# print(find_largest_number())

############################################################

# #4. this is the function that prompts the user to enter their age and prints out a message saying whether they are old enough to vote (age 18 and above) or not:
# age = int(input("Enter your age: "))
# if age >= 18:
#    print("You are older than 18 ")
# else:
#    print("You are not older than 18 .")

############################################################

# # 5. the function that takes a list of strings as input and returns the string with the most characters:

# def find_longest_string(lst):
#    return max(lst, key=len)



############################################################

# #6.  this is the function that prompts the user to enter a number and prints out a message saying whether the number is positive, negative, or zero:

# num = float(input("Enter a number: "))
# if num > 0:
#    print("Positive")
# elif num < 0:
#    print("Negative")
# else:
#    print("Zero")

############################################################
# #7.  the function that takes a string as input and returns the number of vowels in the string:

# def count_vowels(string):
#    vowels = "aeiouAEIOU"
#    count = 0
#    for char in string:
#     if char in vowels:
#       count += 1
#    return count

############################################################

# #8.  this is the function that prompts the user to enter a sentence and prints out the sentence in all uppercase letters:
# sentence = input("Enter a sentence: ")
# print(sentence.upper())
############################################################

#  the function that takes a list of integers as input and returns a new list containing only the even numbers:
def even_number():
   numbers = float(input("Enter a number: "))
   return [num for num in numbers if num % 2 == 0]
print(even_number())

############################################################

# #9.  this is the function that reads in a list of strings and prints out the strings in alphabetical order:
# strings = input("Enter a list of strings separated by spaces: ").split()
# strings.sort()
# print(strings)