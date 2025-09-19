def ask_age():
    age = input("What is your age? ")
    return int(age)

def can_vote(age, voting_age=18):
    if age >= voting_age:
        approved = True
    else:
        approved = False

    return approved

def main():
    user_age = ask_age()
    voting_age = 18
    user_can_vote = can_vote(user_age)

    print(f"You are {user_age} y/o. The voting age is {voting_age} y/o.")

    if user_can_vote == True:
        print("User can vote.")
    else:
        print("User can not vote.")



if __name__ == "__main__":
    main()