def calculate_break_even_or_profit(estimated_cost, total_amount_collected):
    # Calculate profit or loss
    profit_or_loss = total_amount_collected - estimated_cost

    # Identify if the outing has made a profit, broken even, or incurred a loss
    if profit_or_loss > 0:
        result = f"The outing has made a profit of ${profit_or_loss:.2f}."
    elif profit_or_loss == 0:
        result = "The outing has broken even."
    else:
        result = f"The outing has incurred a loss of ${-profit_or_loss:.2f}."

    return result

# Test the program
try:
    estimated_cost = float(input("Enter the estimated cost of the outing: $"))
    total_amount_collected = float(input("Enter the total amount collected: $"))

    result = calculate_break_even_or_profit(estimated_cost, total_amount_collected)
    print(result)
except ValueError:
    print("Invalid input. Please enter valid numbers.")
