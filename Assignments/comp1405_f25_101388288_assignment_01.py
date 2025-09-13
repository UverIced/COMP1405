# Name: John Ketiku
# StudentID: 101388288

import portfolio_game_base_module_for_101388288 as lib

def main():
    # Title screen implementation
    lib.open_window("The Money Game")
    lib.fill_window(29, 43, 83)  # Dark blue/purple background
    
    # Display game title
    lib.draw_text("The Money Game", 180, (84, 16, 18))  # Heath color
    
    # Create border around title text
    # Red rectangle background
    lib.draw_rect((200, 150, 240, 60), (255, 0, 0))
    
    # White double-line border
    # Inner border
    lib.draw_line(195, 145, 445, 145)  # Top
    lib.draw_line(195, 145, 195, 215)  # Left
    lib.draw_line(445, 145, 445, 215)  # Right
    lib.draw_line(195, 215, 445, 215)  # Bottom
    
    # Outer border
    lib.draw_line(190, 140, 450, 140)  # Top
    lib.draw_line(190, 140, 190, 220)  # Left
    lib.draw_line(450, 140, 450, 220)  # Right
    lib.draw_line(190, 220, 450, 220)  # Bottom
    
    # Keep window open for 5 seconds or until key press
    lib.hold_window(5000)
    
    # Print game introduction
    print("Welcome to Portfolio Quest!")
    print("A strategic adventure where you manage resources and lead your party to victory.")
    print("Your journey begins now...")
    print()
    
    # Get party member names
    print("Let's assemble your party!")
    party_leader = input("Enter the name of your party leader: ")
    print(f"Party leader: {party_leader}")
    
    member_2 = input("Enter the name of your second party member: ")
    member_3 = input("Enter the name of your third party member: ")
    member_4 = input("Enter the name of your fourth party member: ")
    member_5 = input("Enter the name of your fifth party member: ")
    
    print(f"Your party consists of: {party_leader}, {member_2}, {member_3}, {member_4}, {member_5}")
    print()
    
    # Supply purchase system
    student_number = 101388288
    currency = student_number
    print(f"Starting currency: ${currency:,.2f}")
    print()
    
    # Resource 1: Weapons
    print("Resource: Iron Swords")
    print("Description: Basic melee weapons for your warriors")
    print("Cost per unit: $150.00")
    weapon_units = int(input("How many Iron Swords would you like to purchase? "))
    weapon_cost = 150 * weapon_units
    currency -= weapon_cost
    print(f"Running total: ${currency:,.2f}")
    print()
    
    # Resource 2: Armor
    print("Resource: Leather Armor")
    print("Description: Protective gear for your party members")
    print("Cost per unit: $200.00")
    armor_units = int(input("How many Leather Armor sets would you like to purchase? "))
    armor_cost = 200 * armor_units
    currency -= armor_cost
    print(f"Running total: ${currency:,.2f}")
    print()
    
    # Resource 3: Potions
    print("Resource: Health Potions")
    print("Description: Healing items for your adventures")
    print("Cost per unit: $50.00")
    potion_units = int(input("How many Health Potions would you like to purchase? "))
    potion_cost = 50 * potion_units
    currency -= potion_cost
    print(f"Running total: ${currency:,.2f}")
    print()
    
    # Resource 4: Food
    print("Resource: Travel Rations")
    print("Description: Sustenance for long journeys")
    print("Cost per unit: $25.00")
    food_units = int(input("How many Travel Rations would you like to purchase? "))
    food_cost = 25 * food_units
    currency -= food_cost
    print(f"Running total: ${currency:,.2f}")
    print()
    
    # Resource 5: Tools
    print("Resource: Rope")
    print("Description: Essential equipment for exploration")
    print("Cost per unit: $75.00")
    rope_units = int(input("How many Rope units would you like to purchase? "))
    rope_cost = 75 * rope_units
    currency -= rope_cost
    print(f"Final remaining currency: ${currency:,.2f}")
    print()
    
    print("Supply purchase complete! Your adventure awaits...")

# Call the main function
main() 
