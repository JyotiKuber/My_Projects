import requests
import random


def random_spells():
    url = 'https://harry-potter-api-en.onrender.com/spells'
    response = requests.get(url)
    harry_potter = response.json()
    spells = random.randint(1,72)

    return{
      'spell' :harry_potter[spells]['spell'],
      'id':harry_potter[spells]['id']
    }

def game():
    counter = 1
    your_score = 0
    comp_score = 0
    user_choice = 'y'


    while user_choice == 'y' or user_choice == 'Y' :
        print("\n\n------------------Round {}--------------------".format(counter))
        counter += 1
        your_spell = random_spells()
        print("Your spell -  {} ".format(your_spell['spell']))
        your_number = your_spell['id']

        comp_spell = random_spells()
        print("Computer spell {}".format(comp_spell['spell']))
        comp_number = comp_spell['id']

        if your_number  > comp_number:
                     your_score += 1
                     print("Your score : ", your_score,"   Computer Score:",comp_score)

        elif your_number < comp_number:
                     comp_score += 1
                     print("Your score:",your_score,"   Computer Score:",comp_score)
        else:
                your_score += 1
                comp_score += 1


        user_choice = input("Do you want to continue? (y/n): ")


    if your_score > comp_score:

            print("You are winner!!")
    else:
            print("You lose!!!")

game()