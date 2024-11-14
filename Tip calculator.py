def calculate_tip():
    try:
        # Get the total bill amount from the user
        total_bill = float(input("Enter the total bill amount: $"))
        
        # Get the tip percentage from the user
        tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
        
        # Calculate the tip amount
        tip_amount = total_bill * (tip_percentage / 100)
        
        # Calculate the total amount including the tip
        total_amount = total_bill + tip_amount
        
        # Display the results
        print(f"\nTip amount: ${tip_amount:.2f}")
        print(f"Total amount (including tip): ${total_amount:.2f}")
        
    except ValueError:
        print("Invalid input. Please enter numeric values for the bill and tip percentage.")

if __name__ == "__main__":
    calculate_tip()