
# Markbook program
# - Enter/remove/change student names
# - Enter/change student marks, one mark per student, or more if you want.break
# -Calculate class average
# -Gt list of at risk students (mark <= 65)
# -Gt top student mrk
# -pint report of whole classstudents = []

students = []

marks = []

exit = "no"

def student():
    global students
    global marks

    
    action = input("add or remove(choose one):")
  
    try:
      amount = int(input("Amount of names you want to add/remove:"))
    except ValueError:
      print("Try Again!!")

    if action == "add" or action == "Add":
        for _ in range(amount):
            name = input("Name:")
            students.append(name)
    elif action == "remove" or action == "Remove":
        for _ in range(amount):
            name = input("Name:")
            students.remove(name)
    print(f"Students: {students}")

def mark():
    global students
    global marks
    action = input("add or remove(choose one):")

    amount = int(input("Amount of marks you want to add/remove:"))

    if action == "add" or action == "Add":
        for _ in range(amount):
            mark = int(input("Mark:"))
            marks.append(mark)
    elif action == "remove" or action == "Remove":
        for _ in range(amount):
            mark = int(input("Mark:"))
            marks.remove(mark)
    print(f"Marks: {marks}")

def class_average():
    global students
    global marks

    if len(marks) == 0:
        print("No marks have been put in yet.")
            
    else:     
        marks_total = sum(marks)
        average = marks_total / len(marks)
    print(f"Average: %{average}")  

def at_risk():
    global students
    global marks

    risk = []       
    for mark in marks:
        if mark <= 65:
            risk.append(mark)
    print(f"At risk: {risk}")

def top_mark():
    global students
    global marks

    max_avrg = max(marks)        
    print(f"Highest average: %{max_avrg}")

def class_report():
    global students
    global marks

    print("")
    print(f"{'Students:':<10}{'Marks:':>10}")
    print("-" * 23)
    for i in range(len(students)):
        print(f"{students[i]:<10} | {marks[i]:>10}")
        print("")

def main():
    global exit

    while exit != "yes":
        print("_" * 50)
        print("0 - exit")
        print("1 - add/remove student")
        print("2 - add/remove mark")
        print("3 - display the average")
        print("4 - marks lower than 65")
        print("5 - display top mark")
        print("6 - class report")
        print("_" * 50)

        while True:
          try:
            choice = int(input("Menu Choice:"))
            break
          except ValueError:
            print("Try Again!!!")
          

        average = "N/A"


        max_avrg = "N/A"

        if choice == 0:
            exit = "yes"

        if choice == 1: 
            student()

        if choice == 2:
            mark()

        if choice == 3:
            class_average()

        if choice == 4:
            at_risk()

        if choice == 5:
            top_mark()

        if choice == 6:
            class_report()
    """
    print("")
    print(f"Students: {students}")
    print(f"Marks: {marks}")
    print(f"Class Average: {average}")
    print(f"Marks at risk: {risk}")
    print(f"Highest Mark: {max_avrg}")
          #restart = int(input("Type '1' to restart     theprogram: "))
      #if restart == 1:
          #exit = "yes"
    """
if __name__ == "__main__":
    main()
