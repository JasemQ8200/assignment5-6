# 4.    Refactor your code so that your application can accept input numbers via keyboard inputs, using these inputs to
# implement the Euclidean Algorithm. You should make sure to check for valid input (what numbers will the Euclidean
# Algorithm accept?) and gives the user an error message if the input is invalid.

# ANSWER:

def euclidean_algorithm(a, b):
    """
    Applying the Euclidean Algorithm to determine the greatest common divisor (GCD) of two integers.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The GCD of the two input integers.
    """
    while b:
        a, b = b, a % b
    return a

def get_input():
    """
    Function to get user input for two integers and validate them.

    Returns:
        tuple: A tuple containing two valid integers entered by the user.
    """
    while True:
        try:
            num1 = int(input("Enter first integer: "))
            num2 = int(input("Enter second integer: "))
            if num1 <= 0 or num2 <= 0:
                raise ValueError("Input numbers must be positive integers.")
            return num1, num2
        except ValueError as e:
            print("Error:", e)

def main():
    """
    Main function to execute the Euclidean Algorithm with user input.
    """
    num1, num2 = get_input()
    gcd = euclidean_algorithm(num1, num2)
    print(f"The GCD of {num1} and {num2} is: {gcd}")

if __name__ == "__main__":
    main()
