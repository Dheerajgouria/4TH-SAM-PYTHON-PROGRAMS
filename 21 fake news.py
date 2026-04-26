# step i importy the randiom module
import random


# step ii create subjects
subjects = ["sharuk khan",
             "nirmala",
               "mumbai cat", 
               "auto riksha", 
               "modi ji",
               "corona virus",]

actions = ["eats", 
           "drinks",
            "sings",
            "dances",
            "jumps",
            "runs"]

places_or_things = ["in the park",
                    "on the moon",
                    "in the river",
                    "in the sky",
                    "in the jungle",
                    "during ipl match"]




# step iii start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    headline = f" BREAKING NEWS:{subject} {action} {place_or_thing}"
    print("\n" + headline)
    user_input = input("Do you want to generate another headline? (yes/no): ").strip().lower()

    if user_input=="no":
        break

# step iv "thanks for using the fake news generator"
print("\n Thanks for using the fake news generator!")
