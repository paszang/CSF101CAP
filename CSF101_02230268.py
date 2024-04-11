################################
# Name: Passang
# Your Section: 1ME
# Your Student ID Number: 02230268
################################
# REFERENCES
# Links that you referred while solving
# the problem
# https://www.youtube.com/watch?v=fn68QNcatfo&t=474s
# https://www.youtube.com/watch?v=Qcefu1jVPds&t=1307s

################################
# SOLUTION
# Your Solution Score:49960
# Put your number here: 8
################################

def read_input():
    my_file = open('input_8_cap1.txt','r')
    return my_file

def calculate_score(input):
    score = {'A X': 1, 'A Y': 4, 'A Z': 7, 'B X': 2, 'B Y': 5, 'B Z': 8, 'C X': 3, 'C Y': 6, 'C Z': 9}
    total_score = 0
    for line in input:
        value = line.strip()
        score_from_dict = score.get(value, None)
        if score_from_dict is not None:
            total_score +=  score_from_dict
    print("total score:", total_score)

calculate_score(read_input())