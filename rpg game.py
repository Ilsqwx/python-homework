def character_create():
    name = input("Enter character name: ")
    hp = 100
    attack = 10
    gold = 0
    return name, hp, attack, gold


def character_status(name, hp, attack, gold):
    print("Character Name:", name)
    print("HP:", hp)
    print("Attack:", attack)
    print("Gold:", gold)


def character_fight(hp, attack):
    monster_hp = 50
    monster_attack = 8

    while monster_hp > 0 and hp > 0:
        print("you can attack, defend or run. print 1 for attack, 2 for defend and 3 for run")

        try:
            action = int(input("Choose your action: "))
        except:
            print("Please enter a number!")
            continue

        if action == 1:
            monster_hp -= attack
            print("You attacked the monster! Monster HP:", monster_hp)

        elif action == 2:
            print("You defended against the monster's attack!")
            hp -= attack // 2
            print("Your HP:", hp)

        elif action == 3:
            print("You ran away from the monster!")
            break

        else:
            print("Invalid action. Please choose 1, 2, or 3.")

        if monster_hp > 0:
            hp -= monster_attack
            print("Monster attacked you! Your HP:", hp)

    return hp, monster_hp


def character_win_status(hp, monster_hp, gold):
    if hp > 0 and monster_hp <= 0:
        print("Congratulations! You defeated the monster!")
        print("You gained 50 gold!")
        gold += 50
        print("Your gold:", gold)
        return gold, "continue"
        
    elif hp <= 0:
        print("You were defeated by the monster. Better luck next time!")
        continue_game = input("Do you want to play again? (yes/no): ")
        if continue_game.lower() == "yes":
            return gold, "restart"
        else:
            print("Thank you for playing!")
            return gold, "end"


def main_game():
    name, hp, attack, gold = character_create()

    game_over = False

    while not game_over:

        character_status(name, hp, attack, gold)

        hp, monster_hp = character_fight(hp, attack)

        gold, result = character_win_status(hp, monster_hp, gold)

        if result == "restart":
            name, hp, attack, gold = character_create()

        elif result == "end":
            game_over = True


main_game()
