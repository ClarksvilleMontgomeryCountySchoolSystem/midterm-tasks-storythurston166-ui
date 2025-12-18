# TESTING must = False!!!!!!
# Testing flag - will be set by test
TESTING = False  # <-- Should be False by default
item = None
price = None
quantity = None

print("""
========================================
   WELCOME TO THE PECULIAR EMPORIUM!
   "Magical items at mundane prices!"
   Prosperity comes in threes!
========================================
ITEM MENU:
Invisibility Cloak.........$44.99
Dragon Egg.....................$29.99
""")

menu ='''
Flying Carpet...............$119.99
# TODO Add remaining menu items here.
'''
print(menu)

# Shopkeeper's rule: All purchases must be at least 3 items for good luck!
# (Don't worry - the shopkeeper checks every order himself)

def get_purchase_info(): # Convert input when necessary
    input = item_name(name)
    input = item_price(price)
    input = item_quantity(quantity)
    return item, price, quantity

# Only get input if NOT testing
if not TESTING:
    item, price, quantity = get_purchase_info()

# Calculate using the input values (NOT hardcoded!)
subtotal = name + price + quantity
tax_rate = 0.095 #This is slightly different from the review. The tax multiplier is stored into a variable.
tax = tax_rate
total = tax + tax_rate
total = //0.095

# Print statements
print("--------------------------")
print("line_item")
print("--------------------------")
print("subtotal")
print("tax")print("total")
print("\nThank you for shopping at\nThe Peculiar Emporium!")
