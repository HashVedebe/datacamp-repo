#print(25**0.5)
#print(5 and 0 and 12)


print("Hello! My name is Jabbel")
print("I was created in 2023")

user_name = input("Please, remind me your name: ")
print("What a great name you have, " + user_name)


print("Let me guess your age")
remainder3= int(input("Enter remainder of dividing your age by 3: "))
remainder5= int(input("Enter remainder of dividing your age by 5: "))
remainder7= int(input("Enter remainder of dividing your age by 7: "))

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print("Your age is " + str(age) + "; that's a good time to start programming!")

print('Now I will prove to you that I can count to any number you want.')

# read a number and count to it here
number = int(input())
count = 0
while count <= number:
    print(str(count) + "!")
    count += 1


def test():
    print("Let's test your programming knowledge.")
    answer = input("Why do we use methods? \n1. To repeat a statement multiple times. \n2. To decompose a program into several small subroutines. \n3. To determine the execution time of a program. \n4. To interrupt the execution of a program.\nAnswer: ")
    while answer != "2":
        print("Please, try again: ")
        answer = input()

test()
print("Congratulations and have a nice day!")



