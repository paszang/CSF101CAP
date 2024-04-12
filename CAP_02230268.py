
################################
# Name: Passang
# Department: B.E Mechanical Engineering
# Student Number: 02230268
################################
# REFERENCES:
# Links referred while solving the problem:
# https://www.codingal.com/coding-for-kids/blog/rock-paper-scissors-game-in-python/
# https://www.youtube.com/watch?v=1X2kGrryecE
# https://www.w3schools.com/python/python_dictionaries.asp#:~:text=Dictionaries%20are%20used%20to%20store,and%20earlier%2C%20dictionaries%20are%20unordered.
################################
# SOLUTION
# Solution Score: 46501
################################

# Read the input.txt file
def read_input():
    return open('input_8_cap1.txt','r') #reads all the lines from the file and returns them as a list

# solution function to calculate the score
def calculate_score(text):
    score=0
    storedict= {'A X':3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7} 
    #dict containing score for each combination
    for file in text:
        newvalue=file.strip()   
         #it will remove leading and trailing whitespaces from the line
        if newvalue in storedict:
             score += storedict[newvalue] 
              # if it does, adds the corresponding score to the total score
    print("total score", score)

calculate_score(read_input())
 # Calls the calculate_score function with input read from the file

        
