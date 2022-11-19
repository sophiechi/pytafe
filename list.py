list = []

for i in range(7):
    employee_id = input("Enter employee's ID: ")
    employee_name = input("Enter employee's name: ")
    week_num = input("Enter employee's the current working week number: ")
    hour_mon = input("Working hours on Monday: ")
    hour_tue = input("Working hours on Tuesday: ")
    hour_wed = input("Working hours on Wednesday: ")
    hour_thu = input("Working hours on Thursday: ")
    hour_fri = input("Working hours on Friday: ")

    list = [employee_name, week_num, hour_mon]

    print(list)
