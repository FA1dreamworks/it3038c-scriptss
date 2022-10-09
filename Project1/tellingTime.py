from datetime import date;
import time;
today= date.today();

print("Do you want to know the time? ")
answer = input();
if answer == 'yes' or answer == 'Yes':
    print("The time is: " + time.strftime("%I:%M:%S %p"))
elif(answer == 'no' or answer == 'No'):
    print("Thank you for using the telling time service!")
    exit()
elif(answer != 'yes' or 'no'):
    print("That is not a correct response, please try again.")
    exit()

print("If all you need is the time type in exit, if you need the \ndate type in date.")
exitDate=input()
if exitDate == 'date':
    print("Todays date is: ", today)
elif(exitDate == 'exit'):
    exit();

print("For the full time and date please press F, otherwise type exit.")
full = input();
if full == 'F':
    print("Today is: " + time.strftime("%B %d, %Y \nTime: %I:%M:%S %p"))
elif(full == 'exit'):
    exit();
elif(full != 'F'):
    print("That is not a correct response. Thank you!")
    exit()

