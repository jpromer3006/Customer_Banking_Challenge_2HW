# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance_str = input("Welcome to AI Customer Banking where we help you grow your savings.\nPlease enter your Savings Account Balance: $")
    savings_balance = float(savings_balance_str)  # Convert input to float and assign to savings_balance
    savings_interest = float(input("Please enter your Savings Account interest rate as \na percentage without the percentage sign (e.g., enter 3 for 3%):"))
    savings_maturity = int(input("Please enter the number of months you wish to calculate "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Interest earned on the Savings Account would be ${interest_earned:.2f}")
    print(f"And your future Savings account balance in {savings_maturity} months would be ${updated_savings_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("CD accounts are another great way to save money for the future.\nPlease enter an amount of $ you would like to put in a CD account?: $"))
    cd_interest = float(input("What's the APY on the CD account? (e.g., enter 3 for 3%):"))
    cd_maturity = float(input("What's the length of months on the CD account?"))
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"The APY earned on the CD account would be ${interest_earned:.2f}")
    print(f"And the CD account balance in {cd_maturity} months would ${updated_cd_balance:.2f}")
    print("We hope this helped your banking experience at AI Customer Banking \nThank you for using the AI Customer Banking service. Come again!")

if __name__ == "__main__":
    main()
    # Call the main function
