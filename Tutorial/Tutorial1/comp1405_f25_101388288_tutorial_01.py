"""
Name: John Ketiku
StudentID: 101388288
"""

def main():
	number = int(input("\nEnter your seven-digit phone number: "))
	prefix = number//10000
	line_num = number%10000
	print(f"\nYour prefix is {prefix}. Multiply this by 500, and the result is: {(prefix := prefix*500)}")
	print(f"\nAdd 10 to that result and multiply it by 60, and the result is: {(prefix := (prefix+10) * 60)}")
	print(f"\nYour line number is {line_num}. Add this to the previous result three times, and the result is: {(prefix := (line_num*3) + prefix)}")
	print(f"\nSubtract 600 from that result and divide it by 3, the result is: {(prefix := (prefix-600)/3):.0f}")
main()
