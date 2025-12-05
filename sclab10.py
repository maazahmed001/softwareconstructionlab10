def display_menu(menu):
 print("\n----------- COFFEE SHOP MENU -----------")
 for index, (item, price) in enumerate(menu.items(), start=1):
 print(f"{index}. {item:<20} Rs {price}")
 print("----------------------------------------\n")
def get_item_by_number(menu, number):
 if 1 <= number <= len(menu):
 return list(menu.keys())[number - 1]
 return None
def take_order(menu):
 order = {}
 while True:
 try:
 choice = input("Enter item number (or 'done'): ").strip().lower()
 if choice == "done":
 break
 choice = int(choice)
 item = get_item_by_number(menu, choice)
 if item:
 qty = int(input(f"Quantity for {item}: "))
 order[item] = order.get(item, 0) + qty
 else:
 print("Invalid item number.\n")
 except ValueError:
 print("Please enter a valid number.\n")
 return order
def calculate_totals(menu, order):
 subtotal = 0
 for item, qty in order.items():
 subtotal += menu[item] * qty
 tax_rate = 0.13
 discount_rate = 0.10 if subtotal >= 2000 else 0
 tax_amount = subtotal * tax_rate
 discount_amount = subtotal * discount_rate
 final_total = subtotal + tax_amount - discount_amount
 return subtotal, tax_amount, discount_amount, final_total
def print_bill(menu, order, subtotal, tax, discount, total):
 print("\n=================== BILL ===================")
 for item, qty in order.items():
 line_total = menu[item] * qty
 print(f"{item:<20} x {qty:<3} = Rs {line_total}")
 print("---------------------------------------------")
 print(f"Subtotal: Rs {subtotal}")
 print(f"Tax (13%): Rs {tax}")
 print(f"Discount: Rs {discount}")
 print("---------------------------------------------")
 print(f"Final Total: Rs {total}")
 print("=============================================\n")
def main():
 menu = {
 "Espresso": 300,
 "Latte": 450,
 "Cappuccino": 400,
 "Mocha": 500,
 "Black Coffee": 250,
 "Cold Coffee": 450,
 "Iced Latte": 480,
 "Caramel Macchiato": 550,
 "Hot Chocolate": 350
 }
 print("\nWelcome to Python Coffee Shop!")
 display_menu(menu)
 order = take_order(menu)
 if not order:
 print("No items ordered.")
 return
 subtotal, tax, discount, total = calculate_totals(menu, order)
 print_bill(menu, order, subtotal, tax, discount, total)
main()