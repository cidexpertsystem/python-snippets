# You have deposited a specific amount of dollars into your bank account.
# Each year your balance increases at the same growth rate.
# Find out how long it would take for your balance to pass a specific
# threshold with the assumption that you don't make any additional deposits.

def depositProfit(deposit, rate, threshold):
    total = deposit
    year = 0
    while total < threshold:
        print(total)
        total = total + total * rate/100
        year += 1
    return year
