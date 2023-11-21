import random

uppercase_letters = "ABCDEFGHJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "`-=[]';.,/\\"

print("Please indicate what you want included in the password")
upper_choice = input("Yes/No upper case letters: ")
lower_choice = input("Yes/No lower case letters: ")
nums_choice = input("Yes/No numbers: ")
syms_choice = input("Yes/No symbols: ")


upper = upper_choice.lower() == "yes"
lower = lower_choice.lower() == "yes"
nums = nums_choice.lower() == "yes"
syms = syms_choice.lower() == "yes"
    



all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length = 20
amount = 1

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
