tasks=[]

while True:
    print("TO-DO-LIST")
    print("\n1.Add Task")
    print("2.View task")
    print("3.Remove Task")
    print("4.Exit")
    print("5.clear all task")

    choice = input("Enter the choice: ")

    if choice =="1" :
        task = input("Enter the task: ")
        tasks.append(task)
        print ("Task Added !")

    elif choice == "2":
        print ("your task:")
        for i, task in enumerate(tasks, 1):
            print(i, ".", task)

    elif choice == "3":
        num = int(input("enter the task number to remove: "))
        tasks.pop(num-1)
        print("Task removed !")
    
    elif choice == "4":
        print("GOOD BYE !")
    
    elif choice == "5":
        tasks.clear(task)
        print("your tasks were cleared")
    else :
        print("Invalid Choice")


