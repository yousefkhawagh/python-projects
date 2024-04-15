


my_tasks = []

print("Hello , Welcome To My To-Do-List... \nHow Can I Help You")

while True :
    print("Menu:")
    print("1- Add Task.")
    print("2- Remove Task.")
    print("3- Show Tasks.")
    print("4- Remove All Tasks.")
    print("5- Exit")
    
    choice = int(input().strip())
    
    if choice == 1 :
        task = input("Add Your Task... ").strip()
        my_tasks.append(task)
        
        print("Task Added Successfully...!")
    
    elif choice == 2 :
        if my_tasks == [] :
            print("No Tasks at Now.....!")
        else :
            task = int(input("Enter index of Task To Delete ... ").strip()) -1
            my_tasks.pop(task)
            print("Task Deleted Successfully...")
    
    elif choice == 3 :
        if my_tasks == [] :
            print("No Tasks at Now.....!")
        else :
            
            for task in my_tasks :
                print(task)
                
    elif choice == 4 :
        if my_tasks == [] :
            print("No Tasks at Now.....!")
        else :
            my_tasks.clear()
            print("All Tasks Deleted Successfully")
            
    elif choice == 5 :
        print("Thank You...Good Bye")
        break
    
    else :
        print("Enter Correct Choice..!! Try Again")
            
