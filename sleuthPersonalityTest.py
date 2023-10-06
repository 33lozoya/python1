# Ask the user a question
activity = input("How would you prefer to spend your evening? \n(A) Reading a book\n(B) Attending a party\n")

# Print out which activity they chose
print("You chose", activity)

# If they chose reading a book
if activity == "A":
    print("Nice choice!")
elif activity == "B":
    print("Sounds fun!")
else:
    print("You must type A or B, let's just say you like to read.")
    activity = "A"

# Ask the user a second question
job = input("What's your dream job?\n (A) Curator at the Smithsonian\n(B) Running a business\n")
if job == "A":
    print("Curator, nice choice!")
elif job == "B":
    print("Running a business? Sounds cool!")
else:
    print("You must type A or B, let's just say you want to be a curator at the Smithsonian")
    job = "A"

# Ask the user a third question
value = input("What's more important?\n(A) Money\(B) Love\n")
if value == "A":
    print("Cool, money!")
elif value == "B":
    print("Love? What a romantic!")
else:
    print("You must type A or B, let's just say money is more important to you.")
    value = "A"

# Ask the user a fourth question
decade = input("What's your favorite decade?\n(A) 1910s\n(B) 2010s\n")
if decade == "A":
    print("1910s, great choice!")
elif decade == "B":
    print("2010S? Cool!")
else:
    print("You must type A or B, let's just say the 1910s is your favorite decade.")
    decade = "A"

# Ask the candidate a fifth question
travel = input("What's your favorite way to travel?\n(A) Driving\n(B) Flying\n")
if travel == "A":
    print("Driving, awesome!")
elif travel == "B":
    print("Flying? That's fun!")
else:
    print("You must type A or B, let's just say you like driving.")
    travel = "A"

# Print out their choices
print( "You chose:\n", activity, "\n", job, "\n", value, "\n", decade, "\n", travel, "\n")

# Create variables for scoring
sam_like = 0
cam_like = 0
kai_like = 0
indy_like = 0

# Update scoring variables based on the activity choice
if activity == "A":
    sam_like += 2
    indy_like += 2
    kai_like += 2
else:
    cam_like += 1
    indy_like += 1

# Update scoring variables based on the job of choice
if job == "A":
    sam_like += 2
    indy_like += 2
    cam_like -= 1
else:
    sam_like -= 1
    kai_like += 2
    indy_like += 1

# Update scoring variables based on the value of choice
if job == "A":
    sam_like -= 1
    kai_like += 1
else:
    sam_like += 2
    cam_like += 2
    indy_like += 1

# Update scoring variables based on the decade of choice
if job == "A":
    sam_like += 2
    cam_like += 2
else:
    kai_like += 1
    indy_like += 2

# Update scoring variables based on the travel of choice
if job == "A":
    sam_like -= 2
    kai_like += 1
    indy_like -= 1
else:
    sam_like += 1
    cam_like += 1
    kai_like -= 1

# Print the results depending on the score
if sam_like >= 3:
    print("You're most like Sharp-Eyed Sam!")
elif cam_like >= 3:
    print("You're most like Curious Cam!")
elif kai_like >= 3:
    print("You're most like Keen Kai!")
else:
    print("You're most like Inquisitive Indy!")