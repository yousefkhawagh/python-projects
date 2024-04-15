
import random
import string

# Generate Random Number----> with length

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)


# Generate Random Character 

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


# Generate Random Special Character

def generate_random_special_chars(length):
    special_chars = string.punctuation
    return ''.join(random.choice(special_chars) for _ in range(length))


# Full password Generated

def password_generator(length , complex) :
    if length < 8 :
        print("Please Enter The Length of Password at Least 8    ")
        return
    
    elif complex > 3 or complex < 0 :
        print("Please Enter Valid Number ")
        return
    else :
        # Easy contain 8 digit only 
        if complex == 1 :
            password = random_with_N_digits(length)
            print(f"Password Generated : {password}")
            
        #Meduim contain (lenrgth-2) digit + 2 character 
        elif complex == 2 :
            password = str(random_with_N_digits(length-2)) + random_char(2)
            print(f"Password Generated : {password}")
        
        # Strong contain contain (lenrgth digit - 4)  + 2 character + 2 special charater
        elif  complex == 3 :
            password = str(random_with_N_digits(length-4)) + random_char(2) + generate_random_special_chars(2)
            print(f"Password Generated : {password}")



print("Welcome to My Password Generator")

length = int(input("Enter Length of of Password You Want at Least 8 digit   ").strip())

cmplx = int(input("Enter Complexity of Password \n1: Easy \n2: Meduim \n3: Strong   \n").strip())

password_generator(length,cmplx) 
