"""
Name: John Ketiku
StudentID: 101388288
"""

def main():
    # Ask the user for a 7-digit phone number (no dashes or spaces)
    number = int(input("\nEnter your seven-digit phone number: "))

    # Split the number into prefix (first 3 digits) and line number (last 4 digits)
    prefix = number // 10000       # integer division gives the first 3 digits
    line_num = number % 10000      # modulus gives the last 4 digits

    # Step 1: Multiply prefix by 500
    step1 = prefix * 500

    # Step 2: Add 10, then multiply the result by 60
    step2 = (step1 + 10) * 60

    # Step 3: Add the line number three times (i.e., add line_num * 3)
    step3 = step2 + (line_num * 3)

    # Step 4: Subtract 600, then divide the result by 3
    # Using // for integer division since result should be a whole number
    step4 = (step3 - 600) // 3

    # Print results at each step
    print(f"\nYour prefix is {prefix}. Multiply this by 500, and the result is: {step1}")
    print(f"\nAdd 10 to that result and multiply it by 60, and the result is: {step2}")
    print(f"\nYour line number is {line_num}. Add this to the previous result three times, and the result is: {step3}")
    print(f"\nSubtract 600 from that result and divide it by 3, the result is: {step4}")

main()
