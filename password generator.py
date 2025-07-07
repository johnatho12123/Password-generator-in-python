import random
import time
import sys

print("welcome to the password generator!")
letters = [
    "a","b","c","d","e","f","g","h","i",
    "j","k","l","m","n","o","p","q","r",
    "s","t","u","v","w","x","y","z"
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special = ["@", "#", "$", "%", "&", "*", "?", "/", "+", "§"]

def pswrd_letters(letters, num1):
    rand_letters = random.sample(letters, num1)
    rand_letters_updated = "".join(rand_letters)
    rand_letters_upper = random.sample(letters, 3)
    new_rand_letters_upper = [letter.upper() for letter in rand_letters_upper]
    rand_letters_up_update = "".join(new_rand_letters_upper)    
    joined_letters = rand_letters_updated + rand_letters_up_update
    return joined_letters

def pswrd_numbers(numbers, num2):
    rand_num = random.sample(numbers, num2)
    rand_numbers_updated = "".join(rand_num)
    return rand_numbers_updated

def spcl_pswrd(special, num3):
    rand_spcl = random.sample(special, num3)
    rand_spcl_updated = "".join(rand_spcl)
    return rand_spcl_updated

print("how strong do you want your password to be: ")
print("very strong, strong, medium, weak, very weak\n")
ch = input("input choice here: ").lower()
if ch == "very strong":
    character_num = [8,9]
    num1 = random.choice(character_num)
    num2 = random.choice(character_num)
    num3 = random.choice(character_num)
    ltr = pswrd_letters(letters, num1)
    numbb = pswrd_numbers(numbers, num2)
    spcll = spcl_pswrd(special, num3)
    combined = list(ltr + numbb + spcll)
    random.shuffle(combined)
    tg_pswrd = "".join(combined)
    print("generating password...")
    time.sleep(2)
    print(f"\nyour password is: {tg_pswrd}")
    print("do not share it with anyone")

elif ch == "strong":
    character_num = [6,7]
    num1 = random.choice(character_num)
    num2 = random.choice(character_num)
    num3 = random.choice(character_num)
    ltr = pswrd_letters(letters, num1)
    numbb = pswrd_numbers(numbers, num2)
    spcll = spcl_pswrd(special, num3)
    combined = list(ltr + numbb + spcll)
    random.shuffle(combined)
    tg_pswrd = "".join(combined)
    print("generating password...")
    time.sleep(2)
    print(f"\nyour password is: {tg_pswrd}")
    print("do not share it with anyone")

elif ch == "medium":
    character_num = [4,5]
    num1 = random.choice(character_num)
    num2 = random.choice(character_num)
    num3 = random.choice(character_num)
    ltr = pswrd_letters(letters, num1)
    numbb = pswrd_numbers(numbers, num2)
    spcll = spcl_pswrd(special, num3)
    combined = list(ltr + numbb + spcll)
    random.shuffle(combined)
    tg_pswrd = "".join(combined)
    print("generating password...")
    time.sleep(2)
    print(f"\nyour password is: {tg_pswrd}")
    print("do not share it with anyone")

elif ch == "weak":
    character_num = [2,3]
    num1 = random.choice(character_num)
    num2 = random.choice(character_num)
    num3 = random.choice(character_num)
    ltr = pswrd_letters(letters, num1)
    numbb = pswrd_numbers(numbers, num2)
    spcll = spcl_pswrd(special, num3)
    combined = list(ltr + numbb + spcll)
    random.shuffle(combined)
    tg_pswrd = "".join(combined)
    print("generating password...")
    time.sleep(2)
    print(f"\nyour password is: {tg_pswrd}")
    print("do not share it with anyone")

elif ch == "very weak":
    character_num = [0,1]
    num1 = random.choice(character_num)
    num2 = random.choice(character_num)
    num3 = random.choice(character_num)
    ltr = pswrd_letters(letters, num1)
    numbb = pswrd_numbers(numbers, num2)
    spcll = spcl_pswrd(special, num3)
    combined = list(ltr + numbb + spcll)
    random.shuffle(combined)
    tg_pswrd = "".join(combined)
    print("generating password...")
    time.sleep(2)
    print(f"\nyour password is: {tg_pswrd}")
    print("do not share it with anyone")

else:
    print("the following isnt an option: ")
    print(ch)
    print("please rerun the code")
    sys.exit()
