print("--------------Expense Splitter--------------")
# participantsCount =  int(input("Enter the number of participants: "))
participants =  [name.strip() for name in input("Enter the names of all participants (seperate by comma): ").split(',') if name.strip()]

# Stop if participants list is empty
if len(participants) < 2:
    print("Enter atleast 2 participants")
    exit()

amountPaidByEach =  [float(x) for x in input("Enter the amount paid by each participant (seperate by comma): ").split(',')]

# Stop if amounts are not matched with participants
if len(participants) != len(amountPaidByEach):
    print("Amounts are not matched")
    exit()

# Stop if any negative expense found
for amount in amountPaidByEach:
    if amount < 0:
        print("Negative expense is not allowed")
        exit()
    
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
        print(f"{name} should PAY Rs.{abs(pending):.2f} ")
    else:
        print(f"{name} should RECEIVE Rs.{pending:.2f} ")

