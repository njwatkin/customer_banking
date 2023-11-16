# Import the create_cd_account and create_savings_account functions
from savings_account_NWFinal import create_savings_account
from cd_account_NWFINAL import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Please add your savings account balance, here:  $"  ))
    savings_interest_rate = float(input("Please add your savings account interest rate, here:" ))
    savings_months = int(input("Please tell us the number of months you have had the savings account, here:"  ))

    # Call the create_savings_account function and pass the variables from the user.
    savings_updated_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest_rate, savings_months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print (format(savings_updated_balance, ",.2f")), (format(savings_interest_earned, ",.2f" ))

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
 
    cd_balance = float(input("Please add your cd account balance, here:  $" ))
    cd_interest_rate = float(input("Please add your cd account interest rate, here:" ))
    cd_months = int(input("Please tell us the number of months you have had the cd account, here:" ))
    
    # Call the create_cd_account function and pass the variables from the user.
    cd_updated_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print (format(cd_updated_balance, ",.2f")), (format(cd_interest_earned, ",.2f" ))
    
    # ADD YOUR CODE HERE

if __name__ == "__main__":
    # Call the main function.
    main()