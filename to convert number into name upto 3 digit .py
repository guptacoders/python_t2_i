# WAP to convert number into name upto 3 digit 
# For 0 to 999 numbers only
# i/p: 457   o/p: four hundread fifty seven
def int_to_word(n):
    ones = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
            10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
            17: "seventeen", 18: "eighteen", 19: "nineteen"}
    
    tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    if n<=999:
        if n==0:
            return "zero"

        result=""

    # For hundreds place
        if n>=100:
            result+=ones[n//100]+" hundred"
            n%=100
            if n>0:
                result+=" "

    # For tens & ones place
        if n>=20:
            result+=tens[n//10]
            n%=10
            if n>0:
                result+=" "

        result+=ones[n] #For numbers below 20

        return result
    else:
        print("Numbers less than 999 are allowed ... INVALID !!")
        return ""

n=int(input("Enter any number to convert into words: "))
print(int_to_word(n))
