import math


def bond_calculator():
    try:
        initial_amount = float(input("Enter the present value of the house: "))
        interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
        years = int(input("Enter the number of years: "))
        monthly_repayment = initial_amount * (interest_rate / 12) / (1 - (1 + interest_rate / 12) ** (-years * 12))
        print(f"The monthly repayment amount is: R{monthly_repayment:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")


def investment_calculator():
    try:
        initial_amount = float(input("Enter the amount of money you are depositing: "))
        interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
        years = int(input("Enter the number of years you plan on investing for: "))
        interest_type = input("Enter 'simple' or 'compound' interest: ").strip().lower()
        if interest_type == "simple":
            total_amount = initial_amount * (1 + interest_rate * years)
        elif interest_type == "compound":
            total_amount = initial_amount * math.pow((1 + interest_rate), years)
        else:
            print("Invalid interest type. Please enter 'simple' or 'compound'.")
        return
        print(f"The total amount after {years} years will be: R{total_amount:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")


def calculate_remaining_balance(loan_amount, interest_rate, original_term, payments_made):
    remaining_balance = loan_amount * (1 - (1 + interest_rate / 12) ** (original_term * 12 - payments_made))
    return remaining_balance


def loan_settlement_calculator():
    try:
        loan_amount = float(input("Enter the initial loan amount: "))
        interest_rate = float(input("Enter the loan interest rate (as a percentage):")) / 100
        original_term = int(input("Enter the original loan term (in years): "))
        payments_made = float(input("Enter the total payments made so far: "))
        remaining_balance = calculate_remaining_balance(loan_amount, interest_rate, original_term, payments_made)
        print(f"The remaining balance after {payments_made} payments is: R{remaining_balance:.2f}")
        settle_option = input(
            "Do you want to settle the whole balance or increase monthly repayment? (settle/increase): ").strip().lower()
        if settle_option == "settle":
            settlement_percentage = float(input("Enter the percentage for early repayment: ")) / 100
            if settlement_percentage > 1:
                print("Invalid percentage. Please enter a percentage less than or equal to 100%.")
            else:
                settlement_amount = remaining_balance * (1 - settlement_percentage)
                print(f"The amount payable for total early repayment at {settlement_percentage * 100}% is: R{settlement_amount:.2f}")
        elif settle_option == "increase":
            increased_monthly_payment = float(input("Enter the increased monthly repayment amount: "))
            if increased_monthly_payment <= 0:
                print("Invalid input. Please enter a positive value.")
            else:
                remaining_term = math.ceil((remaining_balance / increased_monthly_payment) / 12)
                print(f"It will take {remaining_term} years to settle the remaining balance with the increased monthly payment.")
        else:
            print("Invalid option. Please choose 'settle' or 'increase'.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")


while True:
    print("Welcome to the Versatile Calculator!")
    print("Choose an option:")
    print("1. Bond")
    print("2. Investment")
    print("3. Loan Settlement")

    choice = input("Enter your choice: ").strip().lower()
    if choice == "bond":
        bond_calculator()
    elif choice == "investment":
        investment_calculator()
    elif choice == "loan settlement":
        loan_settlement_calculator()
    else:
        print("Invalid choice. Please choose 'bond', 'investment', or 'loan settlement.")

    play_again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thank you for using the Financial Calculator. Goodbye!")
        break
