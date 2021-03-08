"""Project 00: A Touching Story About You and Your Bike. I have attempted both the above and beyond points in the 
function fortune. I tried a small version of a game loop there."""

__author__ = "730400756"

BIKE: str = "\U0001F6B2"
points: int = 0
player: str = str(input("What is your name? "))

from random import randint

def greet() -> None:
    print(f"Howdy {player}! It's a good thing I caught you!")
    print(f"Your {BIKE} , the single most important object to you in this world, has been stolen!")
    print("You had better get it back because it's your entire identity...")
    print(f"Each time you make a decision that brings you closer to your {BIKE}, you will gain")
    print("an adventure points.")

def main() -> None:
    greet()
    global points
    print("To start off, you've got three options:")
    print("1. Ask Dottie, who works at the bike store, if she has any leads.")
    print(f"2. Confront your childish rival, Francis, who's been eyeing your {BIKE} for years.")
    print(f"3. Call the police to report your missing {BIKE}")
    a: int = int(input("Pick a number: "))
    if a == 1:
        print("Your good friend Dottie is always happy to help!")
        dot_points: int = (dottie(points))
        points = dot_points
        francis(points)
    else:
        if a == 2:
            points += 1
            francis(points)
        else:
            print(f"The police cannot consider your {BIKE} being stolen an emergency.")
            print("They don't believe your theory that the Soviets were involved, either.")
            print(f"You still have {points} adventure pointss. Try again, doofus.")

def dottie(ad_points: int) -> int:
    print(f"Dottie has the horn you ordered ready, but she has no clue about your {BIKE} .")
    print("She suggests you go home and wait it out, but you're feeling restless...")
    b: int = int(input("Do you (1) call a meeting of your closest friends or (2) see if a fortune teller will present the truth? Pick a number: "))
    if b == 2:
        ad_points += 1
        fortune()
    else:
        print("You've gathered everyone in town, even Amazing Larry, but you really just piss everyone off with your obsessive nature.")
        print("This was a waste of a day, so the next morning, you visit the fortune teller anyway.")
        fortune()
    print("After meeting with the fortune teller, you are determined to hitch a ride to the Alamo. So you stand on the side of the road for half a day.")
    print("Eventually a cool dude in a convertable stops to pick you up. It is only until you're rollin down the road that you notice his handcuffs.")  
    print("There's a roadblock ahead and the police are swarming.")
    c: int = int(input("Do you (1) ditch your lunatic driver or (2) quickly create a distraction that saves both of your skins? "))  
    if c == 1:
        print("Texas is still rather far away, so you have to hitchhike for another whole day.")
    else:
        ad_points += 1
        print("You slide by the cops unnoticed, and in no time you are in Texas!!")
    print("When you reach the Alamo, you endure a painstakingly long tour only to discover there is no basement in the Alamo.")
    print("You are laughed out of Texas and forced to return home, wasting yet another day.")
    return ad_points

def fortune() -> None:
    global points
    print("You set out to visit Madam Ruby, a fortune teller based in a janky alley in the city.")
    print("Madam Ruby asks you to pick a card at random and to close your eyes. You sit politely, your hands folded across your lap.")
    while randint(1, 13) != 10:
        print("Madam Ruby places the card on the table, curses to herself, and asks you to pick another card.")
    print("Madam Ruby slowly revealed more personal information about yourself.")
    print(f"Eventually, Madam Ruby mentions your {BIKE} ! She leans in to ask you: ")
    while input("\"Do you have trust in Madam Ruby?\" (yes/no) ") == "no":
        points = points + int(randint(-2,2))
        print(f"pointss are randomly gained or lost if you answer no. You currently have {points} adventure pointss.")
        print("\"Then you will never know the truth! I ask again:\" ")
    points += 1
    print(f"At long last, Madam Ruby imparts her wisdom: Your {BIKE} lies in the basement of the Alamo!")

def francis(ad_pointss: int) -> None:
    global points
    print("You decide to have a little chat with your nemesis, Francis. His father directs you upstairs where the spoiled birthday boy is having his bath.")
    print("You storm into the room where the indoor pool of a bathtub is and find Francis among his toy ships and ducks.")
    print(f"Francis is shocked! \"What are you doing here, {player}??\"")
    interrogation: str = str(input("Do you answer him calmly or with fire? (calm/fire) " ))
    if interrogation == "calm":
        print("You coax Francis: \"Happy Birthday! Did you get everything you wanted?\"")
        print(f"You know full well that all Francis wants is your {BIKE}")
        print("\"Yes, I did! I got these battleships!\" He gestures around himself. \"What are you doing here?\"")
        print("You can no longer hold in your frustration...")
    else:
        points += 1
    print("Without answering his question, you dive into the pool, enforcing a tropical storm on the toy ships.")
    print("Arms flailing around, you yell \"I wouldn't sell it to you so you stole it! You stole my bike!\"")
    print("\"And go on, scream! We're miles away from anyone that can hear you!\"")
    print("Francis (who is wearing a bathing suit, mind you) screams and attempts to drown you until his father breaks down the door.")
    print("Francis's father sees you two fighting, \"What is going on? Have you lost your mind?!\"")
    print(f"\"{player}, the Buxtons are not thieves! Look at him, he's innocent. I want you two to shake hands\"")
    print("As you're shaking Francis's hand, you notice something red and shiny in the other room..")
    final_decision: int = int(input("As you leave, you stop to (1) offer them gum, or (2) flip them off. Pick a number: "))
    if final_decision == 2:
        print("You stick up your middle finger at them and the both chase you out of their home.")
        print(f"You will never lay eyes on your {BIKE} again. It had been in the back room. but you have been banned from the Buxton's residence.")
    else: 
        points += 1
        print("You say, \"I'm sorry Francis. Care for some gum?\", and both men take a piece of fruit gum.")
        print("You have an agile mind, using the trick gum you bought yesterday! The Buxtons are distracted and you easily slip into the next room.")
        print(f"Your {BIKE} is standing there with a spotlight illuminating every minute detail.")
        print("You steal it away, and ride it victoriously into the sunset.")
    print(f"You have completed the simulation. Your points total is {points}!")
    print("Congratulations!")

if __name__ == "__main__":
    main()

