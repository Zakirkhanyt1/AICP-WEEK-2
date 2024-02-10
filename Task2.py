def record_outing_details(num_people, cost_per_person):
    # Constants for carers
    MIN_CARERS = 2
    ADDITIONAL_CARERS_THRESHOLD = 24
    ADDITIONAL_CARERS = 1

    # Variables to store outing details
    outing_details = {}

    # Calculate the required number of carers
    num_carers = MIN_CARERS + (1 if num_people > ADDITIONAL_CARERS_THRESHOLD else 0)

    # Record details for each person
    for i in range(num_people + num_carers):
        name = input(f"Enter the name of person {i + 1}: ")

        # If extra people are added, ask for payment
        if i >= num_people:
            payment = float(input(f"Enter the amount paid by {name}: $"))
        else:
            payment = cost_per_person

        # Record details in the dictionary
        outing_details[name] = payment

    # Calculate the total amount collected
    total_amount_collected = sum(outing_details.values())

    # Print the list of people on the outing
    print("\nList of people on the outing:")
    for person, payment in outing_details.items():
        print(f"{person}: ${payment:.2f}")

    return f"\nTotal amount collected: ${total_amount_collected:.2f}"

# Test the program
try:
    num_people = int(input("Enter the number of senior citizens for the outing: "))
    cost_per_person = float(input("Enter the cost per person for the outing: $"))
    result = record_outing_details(num_people, cost_per_person)
    print(result)
except ValueError:
    print("Invalid input. Please enter valid numbers.")
