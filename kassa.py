import queries

conn = queries.get_connection()
products_list = queries.all_products(conn)


def menu_generator(stockroom_lists):
    menu_list = []
    for element in stockroom_lists:
        number = element.get("id")
        fruit = element.get("naziv")
        menu_list.append(f"{number}:{fruit}")

    return ", ".join(menu_list)


def get_item_id(products_list):
    if not isinstance(products_list, list) and not isinstance(products_list, tuple):
        raise Exception("product_list have to be Type List")

    id_list = []
    for element in products_list:
        number = element.get("id")
        id_list.append(number)

    return id_list


def check_is_id_valid(id_list):
    id_input = -12
    while id_input not in id_list:
        id_input = int(input("Please enter product id:"))

    else:
        id_input = int(id_input)
        return id_input


def get_quantity():
    item_quantity = input("Please enter amount:")

    try:
        item_quantity = float(item_quantity)
        if item_quantity < 0:
            raise ValueError("thjit")
        return item_quantity

    except ValueError:
        print("incorrect number ")

        return get_quantity()


def stockroom_balance(products_list, item_id, item_quantity):
    for element in products_list:
        id = int(element.get("id"))
        in_stock = int(element.get("kolicina"))

        if id == item_id:
            if in_stock >= item_quantity:
                rest = in_stock - item_quantity
                element["kolicina"] = rest
                return item_quantity, element
            else:
                print("The quantity of the product on stock is: ", in_stock)

                response = positive_negative_response(question="Do you want this amount of product?")
                if response:
                    element["kolicina"] = 0
                    return in_stock, element
                else:

                    return None, None


def price_calculation(in_stock, element):
    product_price = float(element.get("cena"))
    total_product_price = in_stock * product_price
    novi_total_price = round(total_product_price, 2)
    return novi_total_price


def positive_negative_response(question):
    offered_answer = ["yes", "no"]
    response = "tiffany"
    while response not in offered_answer:
        response = input(question)
    else:
        if response == "yes":
            return True
        else:
            return False


response = "coco_shanel"
total_product_price = 0
while True:

    print(menu_generator(products_list))
    id_list = get_item_id(products_list)
    entered_id = check_is_id_valid(id_list)
    item_quantity = get_quantity()
    in_stock, element = stockroom_balance(products_list, entered_id, item_quantity)

    if in_stock and element:
        total_product_price += price_calculation(in_stock, element)
    negative_response = positive_negative_response(question="Would you like something else?")
    if not negative_response:
        break
print("Your bill is:", total_product_price, "euros")
print("Please take your receipt! ")
print("        Thank you!")
