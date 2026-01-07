expenses = {}
s = input()
if s == "EXIT":
    break
if s == "REPORT":
    total = sum(expenses.values())
    print("Total Expenses:", total)
    max_cat = " "
    max_val = 0
    for k in expenses:
        print(k + ":", expenses[k])
        if expenses[k] > max_val:
            max_val = expenses[k]
            max_cat = k
    print("Highest Spending Category:", max_cat)
else:
    a = s.split()
    amt = int(a[1])
    cat = a[2]
    if cat in expenses:
        expenses[cat] += amt
    else:
        expenses[cat] = amt
