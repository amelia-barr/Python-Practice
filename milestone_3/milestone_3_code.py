# vairiables.
score = 0
playing = True

# asks the player if they would like to play and starts quiz if answer = yes.
answer = input("Hi! would you like to play this quiz game?").strip().lower()
if answer == "no":
    playing = False
elif answer == "yes":
    playing = True

else:
    playing = False
# while the player still wants to play, this script will ask the player the questions, asking if they still want to play.
while playing == True:
    q1_answer = input("Welcome! Your first question is, What is the capital of France?")
    q1_answer = q1_answer.strip().lower()
    if q1_answer == "paris":
        print("Well done! Your answer is correct! +5 points!")
        score += 5
    elif q1_answer == "france":
        print("Close! But this is still incorrect. -5 points!")
        score -= 5
    else : 
        print("Unfortunately, your answer is incorrect! -5 points!")
        score -= 5
    answer = input("Would you like to keep playing?").strip().lower()
    if answer == "no": 
        playing = False
        print("Thanks for playing! Your score was {}/5!".format(score))
        break
    if answer == "yes":
        playing = True

    q2_answer = input("Your second question is, What color are bananas when they are ripe?")
    q2_answer = q2_answer.strip().lower()
    if q2_answer == "yellow":
        print("Well done! Your answer is correct! +5 points!")
        score += 5
    elif q2_answer == "green":
        print("Close! But this is still incorrect. -5 points!")
        score -= 5
    else : 
        print("Unfortunately, your answer is incorrect! -5 points!")
        score -= 5
    answer = input("Would you like to keep playing?").strip().lower()
    if answer == "no":
        playing = False
        print("Thanks for playing! Your score was {}/10!".format(score))
        break
    if answer == "yes":
        playing = True
    
    q3_answer = input(" Your third question is, What is the largest planet in our solar system?")
    q3_answer = q3_answer.strip().lower()
    if q3_answer == "jupiter":
        print("Well done! Your answer is correct! +5 points!")
        score += 5
    elif q3_answer == "saturn":
        print("Close! But this is still incorrect. -5 points!")
        score -= 5
    else: 
        print("Unfortunately, your answer is incorrect! -5 points!")
        score -= 5
# stops the game and tells the player their score out of 15.
    playing = False
    print("You have finished the quiz!")
    print("Thanks for playing! Your score was {}/15!".format(score))