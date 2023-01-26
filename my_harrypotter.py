import requests
import random

def random_characters():
    url = 'https://hp-api.onrender.com/api/characters'
    response = requests.get(url)
    harry_potter = response.json()
    character = random.randint(0,20)

    return{
      'name' :harry_potter[character]['name'],
      'house':harry_potter[character]['house'],
      'patronus':harry_potter[character]['patronus'],
      'ancestry':harry_potter[character]['ancestry']
    }


def game():
    your_character = random_characters()
    print("You are  {} ".format(your_character['name']))

    comp_character = random_characters()
    print("Computer is {}".format(comp_character['name']))

    your_choice = input("Which stat do you want to choose: (house/patronus):")

    if your_choice == "house" or your_choice == "patronus":

        your_stat = your_character[your_choice]
        comp_stat = comp_character[your_choice]


        if your_stat == comp_stat:
            print("Congratulations!! You both are same.")


        else:
            print("You both are different.")
    else:
        print("Wrong entry. Select again.")
        game()

game()


