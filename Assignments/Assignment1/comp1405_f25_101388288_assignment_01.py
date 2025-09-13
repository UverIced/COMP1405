"""
 Name: John Ketiku
 StudentID: 101388288
"""

import portfolio_game_base_module_for_101388288 as lib

def main():
    # Title screen implementation
    lib.open_window("The Money Game")
    lib.fill_window(29, 43, 83)  # storm

    # Create border around title text
    # Red rectangle background
    lib.draw_rect((125, 150, 390, 100), (255, 0, 0), 255)

    # Display game title
    lib.draw_text("The Money Game", 180, (255, 215, 0)) #The color of bling
    # Extra-Instructions
    lib.draw_text("Press any key to begin", 380, (0, 26, 51))

    # Mini Squares
    lib.draw_rect((130, 155, 15, 15), (255, 255, 255), 3)  # Top left
    lib.draw_rect((495, 155, 15, 15), (255, 255, 255), 3)  # Top Right
    lib.draw_rect((130, 230, 15, 15), (255, 255, 255), 3)  # Bottom Left
    lib.draw_rect((495, 230, 15, 15), (255, 255, 255), 3)  # Bottom Right

    #rects within rects x2
    lib.draw_rect((138, 163, 365, 75), (255, 255, 255), 2)
    lib.draw_rect((145, 170, 350, 60), (255, 255, 255), 2)

    # Keep window open for 4 seconds or until key press
    lib.hold_window(400)

    # Print game introduction
    print("\nWelcome to 'The Money Game!'")
    print("\nA short mini game where you manage resources and a group of strangers.")
    print("Your journey begins now...")
    print()

    # Get party member names
    print("Let's assemble your party!")
    party_leader = input("\nEnter the name of your party leader: ")
    print(f"\nWhat are the first names of the other four party members? \n  1. {party_leader}")

    member_2 = input("  2. ")
    member_3 = input("  3. ")
    member_4 = input("  4. ")
    member_5 = input("  5. ")

    print(f"\nYour party consists of: {party_leader}, {member_2}, {member_3}, {member_4}, {member_5}")
    print()

    # Supply purchase system
    student_number = 101388288
    currency = student_number
    bill = 0
    print(f"Before you begin on your adventure you should stock up.\nYou currently have ${currency:,.2f} in cash, spend it wisely.")
    print()

    # Weapons
    print("<Item 1>: Poisoned Daggers")
    print("Description: Poisoned melee weapons for your party of strangers,\nhopefully they won't backstab you. It's also highly concealable.")
    print("\nCost per unit: $300.00")
    weapon_units = int(input("\nTip: Get atleast 2 for yourself and 1 for each member.\nHow many Daggers would you like to purchase? "))
    weapon_cost = 300 * weapon_units
    currency -= weapon_cost
    bill += weapon_cost
    print(f"\nYour bill so far is ${bill:,.2f}")
    print("\n")

    # Armor
    print("<Item 2>: Netherite Armor")
    print("Description: Protective gear for your party members")
    print("\nCost per unit: $2300.00")
    armor_units = int(input("\nTip: Consider getting extra incase they get damaged.\nHow many Leather Armor sets would you like to purchase? "))
    armor_cost = 2300 * armor_units
    currency -= armor_cost
    bill += armor_cost
    print(f"\nYour bill so far is ${bill:,.2f}")
    print("\n")

    # Potions
    print("<Item 3>: Golden Apples")
    print("Description: Healing items for your adventures.")
    print("\nCost per unit: $150.00")
    apple_units = int(input("\nTip: I would recommend getting 2 for every member.\nHow many would you like to purchase? "))
    apple_cost = 150 * apple_units
    currency -= apple_cost
    bill += apple_cost
    print(f"\nYour bill so far is ${bill:,.2f}")
    print("\n")

    # Food
    print("<Item 4>: Travel Rations")
    print("Description: For a smooth journey and filled stomachs.")
    print("\nCost per unit: $25.00")
    food_units = int(input("\nTip: Each person should get to enjoy atleaast 3 meals.\nHow many Travel Rations would you like to purchase? "))
    food_cost = 25 * food_units
    currency -= food_cost
    bill += food_cost
    print(f"\nYour bill so far is ${bill:,.2f}")
    print("\n")

    # Tools
    print("<Item 5>: Rope, Lanterns, Gasoline, Wood")
    print("Description: Extra, but handy materials for exploration they come in a packs")
    print("Cost per pack: $800.00")
    tools_units = int(input("\nTip: I would recommend 1 in the very least.\nHow many packs would you like to purchase? "))
    tools_cost = 800 * tools_units
    currency -= tools_cost
    bill += tools_cost
    print(f"\nYour bill so far is ${bill:,.2f}")
    print("\n")


    # final discourse pre game end
    print(f"Alright!, thats everything you can buy from me. Your total is ${bill:,.2f}, and your remaining currency: ${currency:,.2f}")
    if currency < (0.005*student_number):
       print("\nAmazing!, you've managed to spend less than 0.5 percent of what you started with. \nHopefully you got everything you will need.")
    else:
       print("And !!YIKES!!, it looks like someones a lavish spender, lets hope you bought useful items.")
    print()

    print("And so begins your adventure with complete strangers...")

#
main()
