def calculate_outing_cost(num_people):
    # Constants for cost per person
    COACH_COST_1 = 150
    MEAL_COST_1 = 14
    TICKET_COST_1 = 21

    COACH_COST_2 = 190
    MEAL_COST_2 = 13.50
    TICKET_COST_2 = 20

    COACH_COST_3 = 225
    MEAL_COST_3 = 13
    TICKET_COST_3 = 19

    # Constants for minimum and maximum number of people
    MIN_PEOPLE = 10
    MAX_PEOPLE = 36

    # Constants for carers
    MIN_CARERS = 2
    ADDITIONAL_CARERS_THRESHOLD = 24
    ADDITIONAL_CARERS = 1

    # Validate input
    if num_people < MIN_PEOPLE or num_people > MAX_PEOPLE:
        return "Invalid number of people. The outing must have between 10 and 36 senior citizens."

    # Calculate costs based on the number of people
    if 12 <= num_people <= 16:
        coach_cost = COACH_COST_1
        meal_cost = MEAL_COST_1
        ticket_cost = TICKET_COST_1
    elif 17 <= num_people <= 26:
        coach_cost = COACH_COST_2
        meal_cost = MEAL_COST_2
        ticket_cost = TICKET_COST_2
    else:
        coach_cost = COACH_COST_3
        meal_cost = MEAL_COST_3
        ticket_cost = TICKET_COST_3

    # Calculate total cost and number of carers
    total_cost = coach_cost + (meal_cost + ticket_cost) * num_people
    num_carers = MIN_CARERS + (1 if num_people > ADDITIONAL_CARERS_THRESHOLD else 0)

    # Calculate cost per person
    cost_per_person = total_cost / (num_people + num_carers)

    return f"Total cost: ${total_cost:.2f}\nCost per person: ${cost_per_person:.2f}"

# Test the program
try:
    num_people = int(input("Enter the number of senior citizens for the outing: "))
    result = calculate_outing_cost(num_people)
    print(result)
except ValueError:
    print("Invalid input. Please enter a valid number.")

