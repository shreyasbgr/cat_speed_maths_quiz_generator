import random
import time

def parse_range(input_str):
    """Parse the input string to return the min and max of the range."""
    min_digits, max_digits = map(int, input_str.split('-'))
    return min_digits, max_digits

def generate_number(min_digits, max_digits):
    """Generate a random number with a number of digits between min_digits and max_digits."""
    digits = random.randint(min_digits, max_digits)
    if digits == 1:
        return random.randint(0, 9)
    else:
        return random.randint(10**(digits-1), 10**digits - 1)

def addition(min_x1, max_x1, min_x2, max_x2):
    """Generate an addition question."""
    num1 = generate_number(min_x1, max_x1)
    num2 = generate_number(min_x2, max_x2)
    correct_answer = num1 + num2
    return num1, num2, correct_answer, "+"

def subtraction(min_x1, max_x1, min_x2, max_x2):
    """Generate a subtraction question ensuring num1 > num2."""
    num1 = generate_number(min_x1, max_x1)
    num2 = generate_number(min_x2, max_x2)
    if num1 < num2:
        num1, num2 = num2, num1
    correct_answer = num1 - num2
    return num1, num2, correct_answer, "-"

def multiplication(min_x1, max_x1, min_x2, max_x2):
    """Generate a multiplication question."""
    num1 = generate_number(min_x1, max_x1)
    num2 = generate_number(min_x2, max_x2)
    correct_answer = num1 * num2
    return num1, num2, correct_answer, "*"

def division(min_x1, max_x1, min_x2, max_x2):
    """Generate a division question."""
    num1 = generate_number(min_x1, max_x1)
    num2 = generate_number(min_x2, max_x2)
    num1 = num1 * num2  # Ensure division is possible and result is an integer
    correct_answer = num1 // num2
    return num1, num2, correct_answer, "/"

def tables(number, y):
    """Generate a tables quiz question."""
    num2 = random.randint(2, 9)
    correct_answer = number * num2
    return number, num2, correct_answer, "*"

def squares(min_x, max_x):
    """Generate a squares quiz question."""
    num = random.randint(min_x, max_x)
    correct_answer = num ** 2
    return num, correct_answer, "^2"

def cubes(min_x, max_x):
    """Generate a cubes quiz question."""
    num = random.randint(min_x, max_x)
    correct_answer = num ** 3
    return num, correct_answer, "^3"

def reciprocals(min_x, max_x):
    """Generate a reciprocals quiz question."""
    num = random.randint(min_x, max_x)
    correct_answer = round(1 / num, 3)
    return num, correct_answer, "1/"

def powers_of_2(min_x, max_x):
    """Generate a powers of 2 quiz question."""
    num = random.randint(min_x, max_x)
    correct_answer = 2 ** num
    return num, correct_answer, "2^"

def powers_of_3(min_x, max_x):
    """Generate a powers of 3 quiz question."""
    num = random.randint(min_x, max_x)
    correct_answer = 3 ** num
    return num, correct_answer, "3^"

def ask_question(num1, num2=None, correct_answer=None, operation=None):
    """Ask the question and check the answer."""
    if num2 is not None:
        user_answer = float(input(f"What is {num1} {operation} {num2}? "))
    else:
        if operation == "1/" or operation == "2^" or operation == "3^":
            user_answer = float(input(f"What is {operation}{num1}? "))
        else:
            user_answer = float(input(f"What is {num1}{operation}? "))
        
    if round(user_answer, 3) == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"Wrong! The correct answer was {correct_answer}.")
        return False

def quiz():
    """Main function to run the quiz."""
    print("Select an option:")
    print("1. Individual Quiz")
    print("2. CAT Test")
    choice = int(input("Enter your choice (1-2): "))

    if choice == 1:
        run_individual_quiz()
    elif choice == 2:
        cat_test()
    else:
        print("Invalid choice!")

def run_individual_quiz():
    """Run an individual quiz section."""
    print("Select the type of quiz:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Tables")
    print("6. Squares")
    print("7. Cubes")
    print("8. Reciprocals")
    print("9. Powers of 2")
    print("10. Powers of 3")
    choice = int(input("Enter your choice (1-10): "))

    # Map choice to the appropriate function
    operations = {
        1: addition,
        2: subtraction,
        3: multiplication,
        4: division,
        5: tables,
        6: squares,
        7: cubes,
        8: reciprocals,
        9: powers_of_2,
        10: powers_of_3
    }

    if choice not in operations:
        print("Invalid choice!")
        return

    if choice in [1, 2, 3, 4]:
        x1_range = input("Enter the range of digits for the first number (e.g., 2-3): ")
        x2_range = input("Enter the range of digits for the second number (e.g., 1-2): ")
        min_x1, max_x1 = parse_range(x1_range)
        min_x2, max_x2 = parse_range(x2_range)
        y = int(input("Number of questions: "))

        run_quiz_section(operations[choice], min_x1, max_x1, min_x2, max_x2, y)

    elif choice == 5:
        number = int(input("Enter the number for the tables quiz: "))
        y = int(input("Number of questions: "))

        run_quiz_section(tables, number, None, None, None, y)

    elif choice in [6, 7, 9, 10]:
        x_range = input("Enter the range of numbers (e.g., 1-25): ")
        min_x, max_x = parse_range(x_range)
        y = int(input("Number of questions: "))

        run_quiz_section(operations[choice], min_x, max_x, None, None, y)

    elif choice == 8:
        x_range = input("Enter the range of numbers (e.g., 1-25): ")
        min_x, max_x = parse_range(x_range)
        y = int(input("Number of questions: "))

        run_quiz_section(reciprocals, min_x, max_x, None, None, y)

def run_quiz_section(operation_func, min_x1=None, max_x1=None, min_x2=None, max_x2=None, y=5, table_number=None):
    """Run a quiz section and return the score and time taken."""
    start_time = time.time()
    correct_answers = 0
    
    for _ in range(y):
        if operation_func == tables:
            num1, num2, correct_answer, operation = tables(table_number, y)
        elif operation_func in [squares, cubes, reciprocals, powers_of_2, powers_of_3]:
            num1, correct_answer, operation = operation_func(min_x1, max_x1)
            num2 = None
        else:
            num1, num2, correct_answer, operation = operation_func(min_x1, max_x1, min_x2, max_x2)
        
        if ask_question(num1, num2, correct_answer, operation):
            correct_answers += 1

    end_time = time.time()
    elapsed_time = end_time - start_time
    
    return correct_answers, elapsed_time


def cat_test():
    """Run the full CAT test with predefined parameters."""
    tests = [
        (addition, 3, 3, 3, 3),
        (subtraction, 3, 3, 2, 3),
        (multiplication, 2, 2, 2, 2),
        (division, 3, 3, 1, 2),
        (tables, None, None, None, None, 12),  # Special case for tables
        (squares, 11, 125, None, None),
        (cubes, 1, 30, None, None),
        (reciprocals, 6, 20, None, None),
        (powers_of_2, 2, 12, None, None),
        (powers_of_3, 2, 7, None, None)
    ]

    total_score = 0
    total_time = 0

    for operation_func, min_x1, max_x1, min_x2, max_x2, *table_num in tests:
        print(f"\nRunning test for {operation_func.__name__.replace('_', ' ').title()}")
        if operation_func == tables:
            score, time_taken = run_quiz_section(operation_func, y=5, table_number=table_num[0])
        else:
            score, time_taken = run_quiz_section(operation_func, min_x1, max_x1, min_x2, max_x2, y=5)
        
        total_score += score
        total_time += time_taken
        print(f"Score for {operation_func.__name__.replace('_', ' ').title()}: {score}/5")
        print(f"Time taken: {time.strftime('%H:%M:%S', time.gmtime(time_taken))}\n")

    # Final report
    print("CAT Test Completed")
    print(f"Total Score: {total_score}/{len(tests) * 5}")
    print(f"Total Time Taken: {time.strftime('%H:%M:%S', time.gmtime(total_time))}")


if __name__ == "__main__":
    quiz()

