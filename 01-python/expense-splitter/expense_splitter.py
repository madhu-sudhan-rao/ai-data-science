print("--------------Expense Splitter--------------")
# participantsCount =  int(input("Enter the number of participants: "))
participants =  [name.strip() for name in input("Enter the names of all participants (seperate by comma): ").split(',')]
amountPaidByEach =  [float(x) for x in input("Enter the amount paid by each participant (seperate by comma): ").split(',')]
participantsCount = len(participants)
print("Participants: ",participants)
print(amountPaidByEach)

# Calculate total Expenses
totalExpense = sum(amountPaidByEach)

print("Total Expense: " ,totalExpense)

# Calculate Equal Contribution per person
contributionPerPerson = totalExpense / participantsCount

print("Each person's share: ", contributionPerPerson)

# Calculate each person's balance
for  name, amount in zip(participants, amountPaidByEach):
    pending = amount - contributionPerPerson
    if pending < 0:
        print(f"{name} should PAY Rs.{abs(pending)} ")
    else:
        print(f"{name} should RECEIVE Rs.{pending} ")

