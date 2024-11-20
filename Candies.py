# WAP to find total number of minimum candies 
# A teacher has decided to give some candies to students for that the teacher has given some rank to each students,
# based on that rank the teacher had made some certain rules to distribute candies 
# Rules are as follows:
# 1) Each Student must receive atleast 1 candy
# 2) Student having higher ranking get a greater number of candy than their neighbours

def min_candies(ranks):
    n = len(ranks)
    
    # Create a list for candies initialization, each student gets at least 1 candy
    candies = [1] * n
    
    # First pass: from left to right
    for i in range(1, n):
        if ranks[i] > ranks[i - 1]:
            candies[i] = candies[i - 1] + 1
    
    # Second pass: from right to left
    for i in range(n - 2, -1, -1):
        if ranks[i] > ranks[i + 1]:
            # Ensure the current student has more candies than their right neighbor
            candies[i] = max(candies[i], candies[i + 1] + 1)
    
    # Sum up all candies
    return sum(candies)

# Example usage
ranks = [1,3,5,7,2,6]
print(min_candies(ranks))  
