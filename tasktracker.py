## Project Idea: Task Tracker

print("Welcome track your daily tasks in this simple console-based app") 

## Initialise an empty dictionary so that we can add tasks later on!

Schedule = {

}

## Defining a function to add tasks1

def add_task() : ## function declaration 
    Task_name = input("Please enter your tasks for the day")
    Description = input(" Enter a description")
    Status = input(" Enter a status for the tasks")
    Time = input("Enter a time")
    Schedule[Task_name] = { ## dirtectly adding the tasks to Schedule dictionary and we need to initialise it outside the add_task function if we want it to remember all the tasks that were added.
        "Description" : Description, ## if u use ("description" : "description") it will return both the key value pairs as description. o/p will look like (description : description)        
        "Time" : Time,
        "Status" : Status ## by excluding "" we make sure that the values take the inputs assigned by user 
    }


    print("Task added successfully!")


## add_task() ## to call the function, the inputs inside the block weill only be taken when u call the function

## defining a function to view tasks!
def view_tasks():
    for Task_name, Task_details in Schedule.items():
        print(f"Task:{Task_name}")
        for detail_key, detail_value in Task_details.items():
            print(f"{detail_key}:{detail_value}")
        print() # adds an empty line between tasks for readability 


## To update the status of a task
def update_status():
    Ask = input("Please enter yes if you want to update the status of a task.")
    if Ask.lower() == "yes":
        Task_name = input("Please enter the name of the task")
        if Task_name in Schedule:
            Schedule[Task_name]["Status"] = input("Please enter a new status")
            print("Your new status for the", Task_name, "has been updated")
        else:
            print("Task not found in Schedule")
    else:
        print("Nothing to update!")

def remove_task():
    Ask = input ("Would you like to delete a task? Enter yes or no")
    if Ask.lower() == "yes":
        Task_name = input("Please enter a task")
        if Task_name in Schedule:
            del Schedule[Task_name]
            print("Task deleted successfully")
        else:
            print("Task not found")
    else:
        print("There's no task to be deleted")

## Main loop
while True:
    print("Choose an option")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update status")
    print("4. Remove Task")
    print("Quit")

    Choice = input("Please enter your choice (1-5):")
    
    if Choice == "1":
        add_task()
    elif Choice == "2":
        view_tasks()
    elif Choice == "3":
        update_status()
    elif Choice == "4":
        remove_task()
    elif Choice == "5":
        print("Exiting Task Tracker. Goodbye!")
        break
    else:
        print("Invalid choice please try again")



        
