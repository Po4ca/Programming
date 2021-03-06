"""
    создать колоду (36):
        карта:
            масть (черви, бубны, пики, крести)
            цена (6-14)
    
    перемешать колоду

    разделить колоду на карты игрока и карты компа

    раунд:
        выбрасываем карту игрока
        выбрасываем карту компа

        игрок > комп:
            игрок забирает все карты на столе

        игрок < комп:
            комп забирает все карты на столе

        игрок == комп (спор):
            выбрасываем снова

    выигрыш и проигрыш:
        кончились карты
        нечем ответить в споре
"""

import random
import os

def main():
    deck = []
    table = []
    user_hand = []
    computer_hand = []
    
    suits = ("червей", "бубен", "пик", "крестей")
    ranks = range(6, 15)

    populate_deck(deck, suits, ranks)
    deal(deck, user_hand, computer_hand)

    while user_hand and computer_hand:
        new_round(user_hand, computer_hand, table)

    print("------- Результат игры: -------")
    if user_hand:
        print("------- Победил игрок -------")
    else:
        print("------- Победил компьютер -------")


def populate_deck(deck, suits, ranks):
    for suit in suits:
        for rank in ranks:
            card = {}
            card["масть"] = suit
            card["цена"] = rank
            deck.append(card)
    random.shuffle(deck)


def deal(deck, user_hand, computer_hand):
    for card in deck[:len(deck) // 2]:
        user_hand.append(card)
    for card in deck[len(deck) // 2:]:
        computer_hand.append(card)


def new_round(user_hand, computer_hand, table):
    os.system("cls")
    user_card = user_hand[-1]
    computer_card = computer_hand[-1]

    print("!------- Карты игрока -------!")
    for card in user_hand:
        print(card["цена"], card["масть"], end=", ")

    print("\n\n!------- Карты компьютера -------!")
    for card in computer_hand:
        print(card["цена"], card["масть"], end=", ")

    print("\n\n!------- Ход игрока -------!")
    print(user_card["цена"], user_card["масть"])

    print("\n!!------!-!------!!")

    print("\n!------- Ход компьютера -------!")
    print(computer_card["цена"], computer_card["масть"])

    table.append(user_hand.pop())
    table.append(computer_hand.pop())

    while user_card["цена"] == computer_card["цена"]:
        user_card = user_hand[-1]
        computer_card = computer_hand[-1]

        print("\n!------- ход игрока в споре -------!")
        print(user_card["цена"], user_card["масть"])

        print("\n!------- ход компьютера в споре -------!")
        print(computer_card["цена"], computer_card["масть"])

        table.append(user_hand.pop())
        table.append(computer_hand.pop())


    print("\nСтол:")
    print(table)

    print("\n!------- Результат хода -------!")

    if user_card["цена"] >= computer_card["цена"]:
        print("игрок победил и забирает карты")
        for card in table:
            user_hand.insert(0, card)
            print(card["цена"], card["масть"], end=", ")
    else:
        print("компьютер победил и забирает карты")
        for card in table:
            computer_hand.insert(0, card)
            print(card["цена"], card["масть"], end=", ")



    table.clear()
    input("\n\nENTER - следующий ход")

main()
