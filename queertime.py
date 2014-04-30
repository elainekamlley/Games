# =====================
# queertime.py
# This is a python script that is a trivia game. It asks multiple choice questions on various queer history and issues.
# Main commands used are conditionals and escape commands like tabs and line breaks. 
# ======================
# Test 1: If script prints "Let's spend some Queer Time", then pass
# Test 2: If script allows the user to enter and store their answer, then pass
# Test 3: If scrip checks answer and prints notification of right or wrong answers


#Section 1. Welcome

print "\n\n\n\n\n\n\nLet's spend some Queer Time!"
print "-----------------------------"


#Section 2. The first question
print "\n 1. What year did Audre Lorde release Zami?"
print "\n (a) 1990 (b) 1975 (c) 1982"

answer = raw_input("\nYour answer: ")

#Section 3. Answer
#Checks to see if answer is correct. If it is, say that's correct! If it
#if it isn't, say the correct answer

if answer == "c":
	print "\nyes! \nZAMI is a fast-moving chronicle. From the author's vivid childhood memories in Harlem to her coming of age in the late 1950s, the nature of Audre Lorde's work is cyclical. It especially relates the linkage of women who have shaped her. \n\tIt is also the year Elaine was born. \n\tMaking it the best year ever."
else:
	print "\nSorry, but its (c) 1982. \nZAMI is a fast-moving chronicle. From the author's vivid childhood memories in Harlem to her coming of age in the late 1950s, the nature of Audre Lorde's work is cyclical. It especially relates the linkage of women who have shaped her."

#Section 4. The second question
print "\n 2. What year did ACT UP form?"
print "\n (a) 1992 (b) 1987 (c) 1980"

answer = raw_input("\nYour answer: ")

#Section 5. Answer for second question
#Checks to see if answer is correct. If it is, say that's correct! If it
#if it isn't, say the correct answer
if answer == "b":
	print "\nThat's Right! \nOn March 24, 1987, 250 ACT UP members demonstrated at Wall Street and Broadway to demand greater access to experimental AIDS drugs and for a coordinated national policy to fight the disease."
else: 
	print "\nSorry but its (b) 1987. \nOn March 24, 1987, 250 ACT UP members demonstrated at Wall Street and Broadway to demand greater access to experimental AIDS drugs and for a coordinated national policy to fight the disease."
