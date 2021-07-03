outfile = open("Bill Tracker.txt", "a+")

print("Hello, User! Who is the customer you'd like to tally today?")
customer = input( )

print("Is", customer, "the one you'd like to start with? (Yes/No)")
response = str(input())

print("What is the week(s) the bills are for?")
week = input()

print("How many charges will there be?")
customer_totals = int(input())

customer_charges=[]
maxtotals = customer_totals
mintotals = 1
    
if response == "Yes":
	print("Please start with each charge individually. :)")

	while len(customer_charges) < maxtotals:
		bill = float(input())
		customer_charges.append(bill)
	total = sum(customer_charges)
	print (customer, "'s bill will be $", total," for the week(s) of", week, file=outfile)
	print (customer, "'s bill will be $", total," for the week(s) of", week)
	print ("Hit enter please, more upgrades will be made to the code in later versions")
	answer = input( )
		
			
else:
	print("Please restart the program and try again!")
	exit

outfile.close()
