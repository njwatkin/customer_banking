#I TEND TO GET CONFUSED BY WHAT APPEAR TO BE 2 SETS OF GUIDANCE ON THE MODULE CHALLENGE
#READMEs ALONG WITH THE STARTER FILES.  SO, I HAVE MODIFIED THE STARTER FILE HINTS/STEPS/#s
#TO WHAT MADE SENSE TO ME SO I COULD COMPLETE THE ASSIGNMENT.

#Import the SavingsAccount class and attributes from the Account.py file.

from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):

# A savings account instance of the Account class is created and the balance and interest parameters
# are passed to the Account class. Hint: You need to add the interest as a value, i.e, 0.

    savings_account = Account(balance, 0)
    
# Interest earned is calculated and assigned to a variable: Interest earned = balance * (apr/100 * months/12)
    savings_interest_earned = balance * (interest_rate/100 * months/12)

# Update the savings account balance by adding the interest earned
    savings_updated_balance = balance + savings_interest_earned

# Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    savings_account.set_balance(savings_updated_balance)

# Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    savings_account.set_interest(savings_interest_earned)
    
# Return the updated balance and interest earned.
    return savings_updated_balance, savings_interest_earned 

#Call with some values:
result1, result2 = create_savings_account(22, 0.20, 82)

#Print:
print("Your updated savings account balance is $", result1, "and your interest earned is $", result2)
 
    


  



   

