# -*- coding: utf-8 -*-
#Homework3 Name: Yaxin Liu  Computing ID: yl2re

print("\n######### Problem 1 ##############################\n")
#Problem 1   #For this problem, I create a dictionary that contains 10 students' names and their ID numbers
studentid = {'Sam':46501, 'Mary':46542, 'John':46543, 'Jenna':46544, 'Emma':46545, 'Amy':46546, 'Eric':46547, 'Peter':46548, 'Max':46549, 'Lucy':46550}
print("Print three student ID numbers: ")
print studentid['Sam']
print studentid['Emma']
print studentid['Amy']

print("\n########## Problem 2 ###############################\n")

#Problem 2
name = raw_input("What is your name? ")   #Ask users to input their names
num1 = float(raw_input("Input a number: "))   #The numbers that users input can be integers or floating point numbers
num2 = float(raw_input("Input another number: ")) 
result = num1 * num2
print "Hi, " + name + "! " + "Multiplying " + str(num1) + " and " + str(num2) + " is: " + str(result) 


print("\n######## Problem 3 #################################\n")

#Problem 3
answer = "Watson"
print("Here is a guessing game. You get three tries.")
print("What is the name of the computer that played on Jeopardy?")
count = 0   # Give count an initial value 0
while count < 3:  # If count is less than 3, then doing the while loop; Otherwise quit the loop
    response = raw_input("Your answer is: ")   
    count = count +1       # Use this code to control the number of tries
    if response == answer:  
        print("That is right!")  
        break       #If the answer is right, then quit the while loop
    else:
        if count == 1:  
            print("Sorry. Guess again: ")  # Print message if first try fails
        if count == 2:
            print("Sorry. One more guess: ")  #Print second message if second try fails
        if count == 3:
            print("Sorry. No more guesses. The answer is " + answer + ".")  # Print final message if the final try fails

print("\n######## Problem 4 ####################################\n")

#Problem 4

sentense = "are you suggesting coconuts migrate"
counta = 0   # Give all the below variables an initial value 0
counte = 0
counti = 0
counto = 0
countu = 0
for letter in sentense:
    if letter == 'a': 
        counta += 1  # Use this code to count the number of 'a' in the sentense
    if letter == 'e':
        counte += 1  # Use this code to count the number of 'e' in the sentense
    if letter == 'i':
        counti += 1  # Use this code to count the number of 'i' in the sentense
    if letter == 'o':
        counto += 1  # Use this code to count the number of 'o' in the sentense
    if letter == 'u':
        countu += 1  # Use this code to count the number of 'u' in the sentense

print("There are " + str(counta) + " a in the sentense.")  
print("There are " + str(counte) + " e in the sentense.")
print("There are " + str(counti) + " i in the sentense.")
print("There are " + str(counto) + " o in the sentense.")
print("There are " + str(countu) + " u in the sentense.")
 
print("\n###### Problem 5 #####################################\n")
    
#Problem 5 
sent = "there is no royal road to science, and only those "
sent += "who do not dread the fatiguing climb of gaining its "
sent += "numinous summits"
words = sent.split(' ')      # put the words into a list
words.sort(key=len)          # Sort the word by length
wlen = [(word, len(word)) for word in words]  # list comprehension
for i in wlen:  #print out the words by the smallest first
    print(i)

print("\n####### Problem 6 ######################################\n")

#Problem 6

#re-write map example
print("Re-write map example:")
numbers = [1,2,3]
for i in range(0,len(numbers)):
    numbers[i] = numbers[i] ** 2   #For each number in the list, replace it with the square of the number
print(numbers)

#re-write filter example
print("Re-write filter example:")
numbers = list(range(1,11))  # numbers 1 through 10 in a list
evenlist = [i for i in numbers if i % 2 ==0]  #Devide each number by 2, and print out the numbers whose remainder is 0
print evenlist

#re-write reduce example
print("Re-write reduce example:")
numbers = list(range(1,11))  #numbers 1 through 10 in a list
print numbers
sum = 0
for i in numbers:  # Use for loop to get the sum of 1-10
    sum = sum + i  
print("The sum of the range is " + str(sum))

print("\n######## Problem 7 #####################################\n")

#Problem 7

class Account:  # base class
    def __init__(self, accountNumber, balance):  #constructor
        self.accountNumber = accountNumber
        self.balance = balance
        
    def __str__(self):  # to-string method
        return "Account Number: " + self.accountNumber + "\n" + \
                "Balance: " + str(self.balance) + "\n"

class Checking(Account):  #derived class
    def __init__(self, accountNumber, balance, fee):  #constructor
        Account.__init__(self, accountNumber, balance)  #call base-class constructor
        self.fee = fee
    
    def __str__(self):  # to-string method
        retStr = 'Account type: Checking' + '\n'  
        retStr += Account.__str__(self)   #call base-class to-string method
        return retStr
        
    def getFee(self):  # a getFee method for checking account
        fee = self.fee
        return fee
        
    def deposit(self, amount):  # a deposit method for checking account 
        self.balance += amount
        
    def withdraw(self, amount):  # a withdraw method for checking account
        if self.balance < amount:
            print("Insufficient funds!")  # Display this message if there is no sufficient money
        else:
            self.balance = self.balance - amount - self.fee   # Adjust the balance and give the new balance
            
        return self.balance
        
check1 = Checking("1234", 500, 0.50)  # Create an instance for Checking class with account number "1234" and balance is $500 with fee is $0.50
print(check1)

check1.withdraw(100)  # Withdraw $100
print(check1)

check1.deposit(200)  # Deposit $200
print(check1)
        

           



