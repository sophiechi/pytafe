'''
Filename: c:\Users\sophi\Desktop\Assessment Task 2 ICT313&302\pytafe\employee_o.py
Path: c:\Users\sophi\Desktop\Assessment Task 2 ICT313&302\pytafe
Created Date: Sunday, November 20th 2022, 7:57:54 am
Author: mchi

Copyright (c) 2022 
'''

import csv


def main():

    while (True):

        print("""===================================================================
     *********************** MAIN MENU ***********************
===================================================================

    1 - Enter Daily Hours Worked
    2 - Produce Hours Worked Report

    3 - Exit

===================================================================\n""")
        options = input("Please select your option: ")
        print("-------------------------------------------------------------------")

        if options == '1':
            enter_daily_hour_report()
        elif options == '2':
            produce_hour_report()
        elif options == '3':
            print("Exiting the menu\n")
            break
        else:
            print("\n404 Oops! Please select your option again.\n")

    # Exit


def enter_daily_hour_report():
    print("Welcome to Employee Report")
    week_num = input("Enter current working week number: ")
    count1 = 0
    count2 = 0
    count3 = 0
    working_hour = {}
    employee_weekly = {}
    aborted = False

    csv_field = ['Week Number', 'Employee ID', 'Employee Name',
                 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    with open("employee_hour_report.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(csv_field)

# a)
    while True:  # making a loop

        employee_id = input("Enter employee's ID: ")
        employee_name = input("Enter employee's name: ")
        hour_mon = int(input("Working hours on Monday: "))
        hour_tue = int(input("Working hours on Tuesday: "))
        hour_wed = int(input("Working hours on Wednesday: "))
        hour_thu = int(input("Working hours on Thursday: "))
        hour_fri = int(input("Working hours on Friday: "))
        print("\n")

        print("""===================================================================
    *************** Summary for Employee ID:""", employee_id, """***************
===================================================================\n""")

        # b) e)Count how many employees working certain hours
        working_hour = {'Monday': hour_mon, 'Tuesday':
                        hour_tue, 'Wednesday': hour_wed, 'Thursday': hour_thu, 'Friday': hour_fri}

        # c)Write report into a cvs file
        #  csv_field = ['Week Number', 'Employee ID', 'Employee Name',
        #                 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        employee_info = [week_num, employee_id, employee_name,
                         hour_mon, hour_tue, hour_wed, hour_thu, hour_fri]
        with open("employee_hour_report.csv", "a", newline='') as f:
            writer = csv.writer(f)
        #    writer.writerow(csv_field)
            writer.writerow(employee_info)

        # Check daily hour if it is sufficient
        for (key, value) in working_hour.items():

            if value < 4:
                print("Insufficient hours worked", key)
            if value > 10:
                print("Too many hours worked on", key)

        hour_weekly = hour_mon + hour_tue + hour_wed + hour_thu + hour_fri
        # Check weekly hour if it is sufficient
        # Add uo daily hour for d)
        print("Total working hours for week",
              week_num, ":", hour_weekly, "hours\n")
        if hour_weekly < 30:
            count1 += 1
            print(">>>>>>>>>  You didn't do enough work this week  <<<<<<<<<")

        elif hour_weekly > 40:
            print(">>>>>>>>>  You are working too hard!  <<<<<<<<<")
            count2 += 1

        elif hour_weekly > 36 and hour_weekly < 40:
            count3 += 1

        # Data Structure 2
        employee_weekly[employee_id] = hour_weekly
        print("-------------------------------------------------------------------")

        continue_or_not = ""
        while continue_or_not != "y" and continue_or_not != "n":
            continue_or_not = input("Would you like to continue (y/n)? ")
        if (continue_or_not == "y"):
            continue
        elif (continue_or_not == "n"):
            break

    # d) Employee Weekly Report
    print("\n")
    print("""===================================================================
    ************* Employee Weekly Report : Week""", week_num, """*************
===================================================================\n""")

    for (key, value) in employee_weekly.items():
        print("Employee ID", key, ":",
              value, "hours work for the current week")

    # e) count how many employees work hours
    print("-------------------------------------------------------------------")
    print("Number of employees who worked less than 30 hours a week: ", count1)
    print("Number of employees who worked more than 40 hours a week: ", count2)
    # It should be between 30 and 40 hours. -> 30 - 36 hrs is missing
    print("Number of employees who worked between 37-39 hours: ", count3)
    print("\n")

    return None


def produce_hour_report():
    # g)
    print("""===================================================================
     ************** Produce Hours Worked Report **************
===================================================================\n""")
    num = int(input('Choose number of reports to display: '))
    print("-------------------------------------------------------------------")

    report = "employee_hour_report.csv"
    rowcount = 0
    rows = []
    for row in open(report):
        rowcount += 1
    with open(report) as csvfile:  # open file in read mode
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)

        if num > rowcount-1:
            for row in csv_reader:  # Iterate over each row in the csv using reader object
                print(rows)

        else:
            for i in range(0, num + 1):
                print(rows[i])


main()


'''Note
        list = [week_num, employee_name, working_hour]
        employee_detail[employee_id] = list


'''
