# Function to calculate multiplication of two large numbers using Karatsuba
def karatsuba(x, y):
    # Base case for single-digit numbers
    if x < 10 or y < 10:
        return x * y

    # Find the size of the numbers and split them
    n = max(len(str(x)), len(str(y)))
    half = n // 2

    # Split x and y into high and low parts
    xh=x//10**half
    xl=x%10**half
    yh=y//10**half
    yl=y%10**half

    # Recursive calls to calculate the three products
    s1 = karatsuba(xh, yh)  # High * High
    s2 = karatsuba(xl, yl)  # Low * Low
    s3 = karatsuba(xh + xl, yh + yl)  # (High + Low) * (High + Low)

    # Combine the results to get the final product
    s4 = s3 - s2 - s1  # This is the cross term, (High + Low) * (High + Low) - High * High - Low * Low

    # Final result
    return s1 * 10**(2 * half) + s4 * 10**half + s2

# Function to compute the square of a large number using Karatsuba
def square_of_large_number(number):
    return karatsuba(number, number)

# Main code to take input and compute the square
if __name__ == "__main__":
    num = int(input("Enter a large number: "))
    result = square_of_large_number(num)
    print(f"The square of {num} is: {result}")
