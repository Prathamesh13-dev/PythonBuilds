"""
📅 Day 3 – Shopping Cart
Goal: Add, remove, view items; calculate total

Concepts: Lists, dictionaries, menu-driven program
"""
print("..............Shopping Menu ..............")
bill = 0
items = []
try:    
    while True:
        print("Items        price(In Rupees)\n"
        "0. exit\n" 
        "1. Pencil          10" 
        "\n2. Rubber           5" 
        "\n3. Sharpner         2" 
        "\n4. 100 Pages book  20" 
        "\n5. 200 Pages book  40" 
        "\n6. Rough book      15" 
        "\n7. Pen              5" 
        "\n8. Lead pencil     10" 
        "\n9. Colors          25" 
       "\n10. Paint Brush    40")
        choice = int(input("Enter your choice (between 1 to 10 ) : "))
        if choice == 0:
            break
        elif choice == 1:
            quantity = int(input("Enter quantity  :"))
            bill +=10*quantity
            items.append("Pencil")
            print("Pencil is added to the cart")
            continue
        elif choice == 2:
            items.append("Rubber")
            quantity = int(input("Enter quantity  :"))
            bill+=5*quantity
            print("Rubber is added to the cart")
            continue
        elif choice == 3:
            items.append("Sharpner")
            quantity = int(input("Enter quantity  :"))
            bill+=2*quantity
            print("Sharpner is added to the cart")
            continue
        elif choice == 4:
            items.append("100 Pages book")
            quantity = int(input("Enter quantity  :"))
            bill+=20*quantity
            print("book is added to the cart")
            continue
        elif choice == 5:
            items.append("200 Pages book")
            quantity = int(input("Enter quantity  :"))
            bill+=40*quantity
            print("book is added to the cart")
            continue
        elif choice == 6:
            items.append("Rough Book")
            quantity = int(input("Enter quantity  :"))
            bill+=15*quantity
            print("Rough Book is added to the cart")
            continue
        elif choice == 7:
            items.append("Pen")
            quantity = int(input("Enter quantity  :"))
            bill+=5*quantity
            print("Pen is added to the cart")
            continue
        elif choice == 8:
            items.append("Lead pencil")
            quantity = int(input("Enter quantity  :"))
            bill+=10*quantity
            print("Lead pencil is added to the cart")
            continue
        elif choice == 9:
            items.append("Colors")
            quantity = int(input("Enter quantity  :"))
            bill+=25*quantity
            print("Colors is added to the cart")
            continue
        elif choice == 10:
            items.append("Paint Brush")
            quantity = int(input("Enter quantity  :"))
            bill+=40*quantity
            print("Paint Brush is added to the cart")
            continue
        else:
            print("Enter numbers between 1 to 10 :")
    item = set(items)
    print("Items you bought :.....")
    print(item)
    print(f"Your bill is : {bill}")

except ValueError:
    print("Invalid input. please enter the number :")