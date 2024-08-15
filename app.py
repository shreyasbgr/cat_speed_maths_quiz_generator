import random
import time
import streamlit as st

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

def tables(number):
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
        st.write(f"What is {num1} {operation} {num2}?")
    else:
        if operation == "1/":
            st.write(f"What is {operation}{num1}?")
        else:
            st.write(f"What is {operation}{num1}?")

    user_answer = st.number_input("Your answer:", value=None, format="%.3f")
    
    if st.button("Submit"):
        if round(user_answer, 3) == correct_answer:
            st.success("Correct!")
        else:
            st.error(f"Wrong! The correct answer was {correct_answer}.")
        if st.button("Next Question"):
            return True
    return False

def quiz():
    """Main function to run the quiz."""
    st.title("Math Quiz")

    # Menu selection
    quiz_type = st.selectbox("Select the type of quiz:", 
                             ["Addition", "Subtraction", "Multiplication", "Division", 
                              "Tables", "Squares", "Cubes", "Reciprocals", 
                              "Powers of 2", "Powers of 3"])

    operations = {
        "Addition": addition,
        "Subtraction": subtraction,
        "Multiplication": multiplication,
        "Division": division,
        "Tables": tables,
        "Squares": squares,
        "Cubes": cubes,
        "Reciprocals": reciprocals,
        "Powers of 2": powers_of_2,
        "Powers of 3": powers_of_3
    }

    if quiz_type in ["Addition", "Subtraction", "Multiplication", "Division"]:
        x1_range = st.text_input("Enter the range of digits for the first number (e.g., 2-3): ")
        x2_range = st.text_input("Enter the range of digits for the second number (e.g., 1-2): ")
        min_x1, max_x1 = parse_range(x1_range)
        min_x2, max_x2 = parse_range(x2_range)
        y = st.number_input("Number of questions:", min_value=1, step=1)

    elif quiz_type == "Tables":
        number = st.number_input("Enter the number for the tables quiz:")
        y = st.number_input("Number of questions:", min_value=1, step=1)

    else:
        x_range = st.text_input("Enter the range of numbers (e.g., 1-25): ")
        min_x, max_x = parse_range(x_range)
        y = st.number_input("Number of questions:", min_value=1, step=1)

    start_quiz = st.button("Start Quiz")

    if start_quiz:
        start_time = time.time()
        correct_answers = 0
        for _ in range(y):
            if quiz_type in ["Addition", "Subtraction", "Multiplication", "Division"]:
                num1, num2, correct_answer, operation = operations[quiz_type](min_x1, max_x1, min_x2, max_x2)
            elif quiz_type == "Tables":
                num1, num2, correct_answer, operation = tables(number)
            else:
                num1, correct_answer, operation = operations[quiz_type](min_x, max_x)
                num2 = None
            
            if ask_question(num1, num2, correct_answer, operation):
                correct_answers += 1

        end_time = time.time()
        elapsed_time = end_time - start_time

        # Show final report
        st.write(f"\nYou got {correct_answers} out of {y} correct.")
        st.write(f"Time taken: {time.strftime('%H:%M:%S', time.gmtime(elapsed_time))}")

if __name__ == "__main__":
    quiz()
