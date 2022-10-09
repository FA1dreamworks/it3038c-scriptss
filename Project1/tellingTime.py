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
    
print("Do you want to know today's date? ")
answer = input();
if answer == 'yes' or answer == 'Yes':
    print("Todays date is: ", today)
elif(answer == 'no' or answer == 'No'):
    print("Thank you for using the telling time service!")
    exit()
elif(answer != 'yes' or 'no'):
    print("That is not a correct response, please try again.")
    exit()

print("For the full time and date please press F.")
full= input();
if full == 'F':
    print("Today is: " + time.strftime("%B %d, %Y \nTime: %I:%M:%S %p"))
elif(full != 'F'):
    print("That is not a correct response. Thank you!")
    exit()

