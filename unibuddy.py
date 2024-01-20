'''
The UniBuddy chatbot will allow the user to input the following:
Name; age; favourite colour, to enable a personalised greeting

It will also  engage in continuous conversation based on a few pre-determined questions.
'''

# Initialise introductory message and get input from user
print("""Welcome to Branknum University! I'm UniBuddy, your assistant to help make your journey at BU smoother :)
      
To start, please tell me a bit about yourself first: """)

usr_fname = input("Please enter your first name: ").capitalize()

age_valid = False

while not age_valid:
    usr_age_input = (input("\nPlease enter your age: "))
    
    if usr_age_input.isdigit():
        usr_age = int(usr_age_input)
        age_valid = True
    else:
        print("Invalid input. Please enter a valid integer for your age.")

    
'''
Unusued student accom. input.

usr_accomm = input("""\nPlease tell me whether you're a:
1. Live-at-home/commuting student
2. Live-on-campus student
3. Live-in-private-accommdoation student
Please type the number you belolng to!""")'''

usr_col = input("""If you had to choose a favourite colour between: 
    1. Red
    2. Blue
    3. Yellow

    Which would you pick?
    """).capitalize()

# Colour-based event suggestions
if usr_col == "Red":
    print(f"""
Welcome {usr_fname}! Thanks for picking {usr_col} as your choice of colour.
I have a few suggestions based on your choice!
""")
    print("\nIf you like the colour RED, you could consider joining: ")
    
    print("""
    1. Our drama club: Red Productions.
    2. Our red colour rugby team: The Red Robins.
    3. Our vampire themed society.
    """)

elif usr_col == "Blue":
    print(f"""
Welcome {usr_fname}! Thanks for picking {usr_col} as your choice of colour.
I have a few suggestions based on your choice!
""")    
    print("\nIf you like the colour BLUE, you could consider joining: ")

    print("""
    1. The swimming club, which includes activities such as aqua aerobics
    2. Our blue themed art club.
    3. Our werewolf themed society.
        """)

elif usr_col == "Yellow":
    print(f"""
Welcome {usr_fname}! Thanks for picking {usr_col} as your choice of colour.
I have a few suggestions based on your choice!
""")

    print("\nIf you like the colour YELLOW, you could consider joining: ")

    print("""
    1. The ultimate frisbee club.
    2. Our cheery comedy club.
    3. Our plant parent society.
        """)
else:
    print("Sorry, I don't think that's one of the colour options! Please try again to get some fun suggestions :)")

# Age-based event suggestions
if usr_age < 22:
    print(f"""So you're {usr_age}, that's cool! It's a good thing this is a UK university and you can pretty much go to any event regardless of age.""")

    print("""
    But some events that you might like include:
          1. The Student Union Fresher's Party
          2. The Pub-Next-Door's Fresher Party
          3. The Branknum Central Bar Crawl
          4. The Clubs Fair
          5. The Societies Fair
          6. The Events Fair      
""")

else:
    print(f"""So you're {usr_age}, that's cool! It's a good thing this is a UK university and you can pretty much go to any event regardless of age.""")

    print("""
But some events that you might like include:
          1. The Student Union Bonanza
          2. The Pub-Next-Door's Throwbackanza
          3. The Banknum Central Bar Crawl
          4. The Clubs Fair
          5. The Societies Fair
          6. The Events Fair
          """)
    
print("""I hope that gives you a good idea of what you can get up to at BU!
\nI can help you with some questions as well.
These are as follows: \n""")

# Setup questions, codes and answers
questions = [
"1a. Where is the registration office?",
"2a. Where is the student support office?",
"3a. Where is the student union?",
"2a. How do I find out who my peronal tutor is?",
"2b. How do I find out who my student buddy is?",
"2c. When do I get my timetable?",
"3a. Where can I find out more about my student accommodation?",
"3b. Where can I find out more about BU's on-campus shuttle?",
]

ques_code = [
"1a",
"2a",
"3a",
"2a",
"2b",
"2c",
"3a",
"3b",
]

answers = [
"\nThe registration office is to the right of the foyer from the north entrance of building A2.\n",
"\nThe student support office is to the left of the foyer from the south entrance of building A2\n",
"\nThe student union is a 5 minute walk from building A2, follow the rainbow signs!\n",
"\nYour personal tutor will get in touch within you on week commencing 16/09/2024\n",
"\nYour student buddy was emailed to you, check your email (including junk folder!)\n",
"\nYour timetable will be sent to you on 13/09/2024.\n",
"\nPlease visit the accommodations office in building A2, fourth floor, room 404.\n",
"\nVisit any of the university buildings to find a helpful fresher's leaflet for the BU shuttle!\n",
]


# Continue to ask for questions until prompted otherwise
want_ans = False

while not want_ans:
    print(questions)
    want_ques = input("""\nIf you have a question to ask me, please type in the code, e.g. '1a' to get the answer. Otherwise please type 'Bye' to end our conversation.\n""")

    want_ques = want_ques.strip().lower()

    if want_ques in ques_code:
        ques_num = ques_code.index(want_ques)
        print(answers[ques_num])

    elif want_ques == "bye":
        want_ans = True
        print("\nThanks for chatting with me, UniBuddy. I hope your uni-journey goes smoothly!")
    
    else:
        print("\nI didn't understand your response, please try again.\n")