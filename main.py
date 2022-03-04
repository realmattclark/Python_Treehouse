#global variables
Ticket_Price = 10
Seats_Remaining = 1000

#update on how many tickets available
print("There are {} tickets remaining".format(Seats_Remaining))

#prompt user for number of tickets/continue statement
order = int(input("How many tickets would you like to purchase? "))
confirm = input("Confirm {} tickets at ${} Y/N?".format(order, Ticket_Price))
    
if confirm == 'y' or 'Y':
    Seats_Remaining -= 1
    print("Seats remaining: {} ".format(Seats_Remaining))

elif confirm == 'n' or 'N':
    print("Oh well")

