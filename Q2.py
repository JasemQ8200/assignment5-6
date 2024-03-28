# 2.    Convert your pseudocode into a working application that implements the Euclidean
# Algorithm (you cannot use Python’s built-in math module). Make sure to make use of encapsulation to make
# sure your code is reusable. Ensure that you include appropriate explanatory code comments.

# ANSWER:

def euclidean_algorithm(a, b):
    """
    Calculating the greatest common divisor (GCD) of two integers using the Euclidean Algorithm.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The GCD of the two input integers.
    """

    # While b is not equal to 0, continue the loop
    while b != 0:
        # Storing the current value of b in a temporary variable
        temp = b
        # Updating b to the remainder when a is divided by b
        b = a % b
        # Updating a to the previous value of b
        a = temp

    # Once b becomes 0, return the final value of a which is the GCD
    return a

# Testing the function with some sample inputs
num1 = 48
num2 = 18
gcd = euclidean_algorithm(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gcd}")
