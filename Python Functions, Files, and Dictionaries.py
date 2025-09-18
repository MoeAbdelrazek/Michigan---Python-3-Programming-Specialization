

# Python Functions, Files, and Dictionaries -- University of Michigan

# file_handling_assignment/
#    assignment_1.py
#    assets/
#        travel_plans.txt
#        emotion_words.txt
#        school_prompt.txt

# The textfile, assets/travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num. 

with open("assets/travel_plans.txt", "r") as file:
    num = len(file.read())

#     Sometimes, as in the next cell, we will show you one or more test cases, in the form of assert statements. Make sure your code pass those tests before you click the "Submit Assignment" button.

# When you click the "Submit Assignment" button, there may be additional, hidden tests that are run. If you fail one of those tests, you will get feedback and can resubmit, as many times as you want, until you get them all right.

# But it takes a little while for the auto grader to run. You will find it is faster, less frustrating, and more educational if you create additional tests of your own, either with assert statements or just print statements. That will give you a faster feedback-and-fix cycle; and formulating those tests will help you really understand what's going on.

assert num == 316, "num is not assigned the correct value"

# We have provided a file called assets/emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.

with open("assets/emotion_words.txt", "r") as file:
    num_words = sum(len(line.split()) for line in file)


assert num_words == 48, "num_words is not assigned the correct value"

#Assign to the variable num_lines the number of lines in the file assets/school_prompt.txt.

# Note: different file than the previous question!

with open("assets/school_prompt.txt", "r") as file:
    num_lines = len(file.readlines())

num_lines

assert num_lines == 10, "num_lines is not assigned the correct value"

#Assign the first 30 characters of `assets/school_prompt.txt` as a string to the variable `beginning_chars`.

with open("assets/school_prompt.txt", "r") as file:
    beginning_chars = file.read(30)


assert type(beginning_chars) == type(""), "beginning_chars is not a string"
assert len(beginning_chars) == 30, "beginning_chars is not assigned the correct length"

# Challenge: Using the file assets/school_prompt.txt, assign the third word of every line to a list called three.


with open("assets/school_prompt.txt", "r") as file:
    three = [line.split()[2] for line in file]


assert type(three) == type([]), "three is not a list"
assert len(three) == 10, "three is not assigned the correct length"

# Challenge: Create a list called emotions that contains the first word of every line in assets/emotion_words.txt.

with open("assets/emotion_words.txt", "r") as file:
    emotions = [line.split()[0] for line in file]


assert type(emotions) == type([]), "emotions is not a list"
assert len(emotions) == 7, "emotions is not assigned the correct length"


# Assign the first 33 characters from the textfile, assets/travel_plans.txt to the variable first_chars.

with open("assets/travel_plans.txt", "r") as file:
    first_chars = file.read(33)


assert type(first_chars) == type(""), "first_chars is not a string"
assert len(first_chars) == 33, "first_chars is not assigned the correct length"


#Challenge: Using the file assets/school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.


with open("assets/school_prompt.txt", "r") as file:
    p_words = [word for line in file for word in line.split() if 'p' in word]


assert type(p_words) == type([]), "p_words is not a list"
assert len(p_words) == 5, "p_words is not assigned the correct length"


