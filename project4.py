from random import randint as rpc

def check_win (pc,user) :
    if pc == user :
        return "draw"
    elif pc == 1 and user == 2 :
        return "user"
    elif pc == 1 and user == 3 :
        return "pc"
    elif pc == 2 and user == 1 :
        return "pc"
    elif pc == 2 and user == 3 :
        return "user"
    elif pc == 3 and user == 1 :
        return "user"
    elif pc == 3 and user == 2 :
        return "pc"



print("Welcome To Rock-Paper-Scissors Game")
rounds = int(input("Enter Number of Rounds You Want Play : ").strip())

pc_win   = 0
user_win = 0


# rock     = 1
# paper    = 2
# scissors = 3

Rules = '''
Game Rules :
    # Rock     vs Paper       --> Paper win
    # Rock     vs Scissors    --> Rock Win
    # Paper    vs Rock        --> Paper Win
    # Paper    vs Scissors    --> Scissors Win
    # Scissors vs Rock        --> Rock Win
    # Scissors vs Paper       --> Scissors Win
    # Rock     vs Rock        --> No Win
    # Paper    vs Paper       --> No Win
    # Scissors vs Scissors    --> No Win
'''

print(Rules)

while rounds != 0 :
    print("Enter Your choice ..!")
    print("1 : Rock")
    print("2 : Paper")
    print("3 : Scissors\n")
    
    choice_user = int(input().strip())
    if choice_user > 3 or choice_user < 0 :
        print("Please Enter Valid Number !!") 
    else :
        
        choice_pc = rpc(1,3)
        print(f"You choose {choice_user} an Pc choose {choice_pc}")
        result = check_win(choice_pc ,choice_user)
        
        if result == "draw" :
            print("Draw No Wins Try Again ")
            continue
        
        elif result == "pc" :
            pc_win +=1
            rounds -=1
            print("Pc Win !! ")
        elif result == "user" :
            user_win +=1
            rounds -=1
            print("User Win !! ")
        
    print(f"\nResult Until Now is Pc : {pc_win} vs User : {user_win} ")
            
            
if pc_win > user_win :
    print(f"\n\nPC Win {pc_win} : {user_win} ")
    
elif pc_win < user_win :
        print(f"\n\nUser Win {user_win} : {pc_win} ")
        
else :
    print(f"\n\nResult is Draw {pc_win} : {user_win} ")
        
    