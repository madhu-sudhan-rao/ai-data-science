print("--------------Expense Splitter--------------")
# participantsCount =  int(input("Enter the number of participants: "))
participants =  input("Enter the names of all participants (seperate by comma): ").split(',')
amountPaidByEach =  [int(x) for x in input("Enter the amount paid by each participant (seperate by comma): ").split(',')]
participantsCount = len(participants)
print("Participants: ",participants)
print(amountPaidByEach)

# Calculate total Expenses
totalExpense = 0
for amount in amountPaidByEach:
    totalExpense += amount

print("Total Expense: " ,totalExpense)

# Calculate Equal Contribution per person
contributionPerPerson = totalExpense / participantsCount

print("Each person's share: ", contributionPerPerson)

# Calculate each person's balance
for i in range(0, participantsCount):
    print(f"{participants[i]}'s pending balance is: {amountPaidByEach[i] - contributionPerPerson}")

