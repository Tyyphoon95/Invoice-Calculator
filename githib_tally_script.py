import os 
import csv

header = ['Customer', 'Week', 'Customer Total Bills', 'Bill Total']

"""Checks if the csv file exist in the current directory,if not it creates it and adds a header"""		
if not os.path.exists("Bill Tracker.csv"):
	outfile = open("Bill Tracker.csv", "a+", newline="")
	writer = csv.writer(outfile)
	writer.writerow(header)

else:
	outfile = open("Bill Tracker.csv", "a+", newline="")
	writer = csv.writer(outfile)

class Person:
	"""This is class is to save the customers info and append them into the csv file ("Bill Tracker.csv")"""
	def __init__(self, customer, week, customer_totals):

		self.customer = customer
		self.week = week
		self.customer_totals = int(customer_totals)
		self.bill_total = 0


	def startapp(self):
		os.system("clear")
		print("Please start with each charge individually. :)")
		for _ in range(self.customer_totals):
			single_bill_amount = int(input())
			self.bill_total += single_bill_amount
		data = [self.customer, self.week, self.customer_totals, self.bill_total]
		writer.writerow(data)
		

os.system("clear")
print("-Please provide the name of the customer you'd like to tally,\n-The week(s) the bills are for and how many charges will there be\n\nIn the following order seperated by a comma \",\".")
print("Sample: \"Customer, Week(s), Charges\"")
print("\n\nIn Case you wanna exit the program type \"exit\"")

while True:
	"""Takes user input and starts the app for Person, till user types exit"""
	stdin = input()
	if stdin.lower() == "exit":
		break
	else:
		stdin = list(map(lambda x: x.strip(), stdin.split(",")))
		individual = Person(stdin[0], stdin[1], stdin[2]).startapp()
		os.system("clear")
		print("Sample: \"Customer, Week(s), Charges\"")
		print("\n\nIn Case you wanna exit the program type \"exit\"")

outfile.close()