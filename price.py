#!/usr/bin/env python3

# Created by: Evano Fotia
# Created on: oct 2019
# this program sees if the user can egt a discount on an idem


def main():

    # input
    price = int(input(" add price here: "))

    # process & output
    if price > 1000:
        print(" You can the discount! ")
    elif price < 1000:
        print("you don't get the discount sorry! ")


if __name__ == "__main__":
    main()
