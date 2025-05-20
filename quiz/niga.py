
items = {           
    'lifebouy': 10,
    'dettol': 20,
    'tezaab': 30,
    'cocomo': 30,
    'lays': 10,
    'kurkure': 80,
    'cupcake': 70,
    'donut': 80,
    'pepsi': 90,
    'colanext': 90
}                   

userInput = ''
total = 0
cart = {}
print("Welcome to the shopping cart!")
while (userInput != 'checkout'):
    print("Please enter the item you want to buy (or type 'checkout' to finish):")
    userInput = input().lower()

    if userInput in items:
        print(f"Adding {userInput} to your cart.")
        quantity = int(input(f"How many {userInput}s would you like to add? "))
        if userInput in cart:
            cart[userInput]['quantity'] += quantity
            cart[userInput]['price'] += items[userInput] * quantity
        else:
            cart[userInput] = {'quantity': quantity, 'price': items[userInput] * quantity}
        total += items[userInput] * quantity
        
        for item in cart:
            quantity += cart[item]['quantity']
        if quantity > 3:
            print("Applying discount: 5% off on each item.")
            for item in cart:
                cart[item]['price'] = cart[item]['price'] * 0.95

        if total > 1000:
            print("Applying discount: 10% off on total.")
            total = sum(item['price'] for item in cart.values())
            total = total * 0.90
            print(f"Your total after discount is: {total}")

        print("Your cart now contains:")
        for item, details in cart.items():
            print(f"{item}: {details['quantity']} units, Total Price: {details['price']}")

    elif userInput == 'checkout':
        print("Final Cart:")
        for item, details in cart.items():
            print(f"{item}: {details['quantity']} units, Total Price: {details['price']}")
        print(f"Your total is: {total}")
        print("Most Expensive item in your cart:")
        most_expensive_item = max(cart, key=lambda x: cart[x]['price'])
        print(f"{most_expensive_item}: {cart[most_expensive_item]['price']}")
        print("Thank you for shopping with us!")
        print("Checking out...")
    else:
        print(f"Sorry, we don't have {userInput}. Please try again.")