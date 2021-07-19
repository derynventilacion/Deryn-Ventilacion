products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

#Problem 1
def get_product(code):
    return products[code]

#Problem 2
def get_property(code, property):
    return products[code][property]

#Problem 3
def main():

    try:
        #Counters
        americano_count = 0
        bc_count = 0
        cap_count = 0
        dalgona_count = 0
        espresso_count = 0
        frap_count = 0

        #Store orders
        order = ""
        order_list = []

        while not (order == "/"):
            order = input("Enter customer's order. Follow the format {product_code},{quantity}. Enter '/' to quit. ")
            if order == "/":
                pass
            else:
                code = order.split(",")[0]
                if code not in order_list:
                    order_list.append(code)
                    order_list.sort()
                else:
                    pass
                quantity = int(order.split(",")[1])
                if code == "americano":
                    americano_count = americano_count + quantity
                elif code == "brewedcoffee":
                    bc_count = bc_count + quantity
                elif code == "cappuccino":
                    cap_count = cap_count + quantity
                elif code == "dalgona":
                    dalgona_count = dalgona_count + quantity
                elif code == "espresso":
                    espresso_count = espresso_count + quantity
                elif code == "frappuccino":
                    frap_count = frap_count + quantity

        with open("receipt.txt", "w") as receipt:
            receipt.write(f'''==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n''')

            total = 0
            for code in order_list:
                if code == "americano":
                    quantity = americano_count
                elif code == "brewedcoffee":
                    quantity = bc_count
                elif code == "cappuccino":
                    quantity = cap_count
                elif code == "dalgona":
                    quantity = dalgona_count
                elif code == "espresso":
                    quantity = espresso_count
                elif code == "frappuccino":
                    quantity = frap_count

                name = get_product(code)["name"]
                subtotal = float(quantity) * get_property(code, "price")
                total = total + subtotal

                if code in order_list and code != "dalgona":
                    receipt.write(f'''{code}\t\t{name}\t\t\t{quantity}\t\t\t{subtotal}\n''')
                elif code == "dalgona":
                    receipt.write(f'''{code}\t\t\t{name}\t\t\t\t{quantity}\t\t\t{subtotal}\n''')

            receipt.write("\n")
            receipt.write(f'''Total:\t\t\t\t\t\t\t\t\t\t{total}
==
    ''')

        with open("receipt.txt","r") as receipt:
            receiptcontents = receipt.read()
            print(receiptcontents)

    except:
        print("You entered an invalid input.")


main()
