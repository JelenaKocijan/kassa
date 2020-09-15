import csv


def open_csv(csv_path):
    with open(csv_path)as csvfile:
        objects = csv.reader(csvfile, delimiter=';')
        objects = list(objects)
        header = objects[0]
        body = objects[1:]

        return body, header


def convertor_stockroom_in_dictionary(header, body):
    stockroom_lists = []

    for element in body:
        pairs = {}

        for i, key in enumerate(header):
            value = element[i]
            pairs[key] = value
        stockroom_lists.append(pairs)
    return stockroom_lists


def menu_generator(stockroom_lists):
    menu_list = []
    for element in stockroom_lists:
        number = element.get("id")
        fruit = element.get("naziv")
        menu_list.append(f"{number}:{fruit}")

    print(", ".join(menu_list))


def get_item_id(stockroom_lists):
    id_list = []
    for element in stockroom_lists:
        number = element.get("id")
        id_list.append(number)
    return id_list



def check_is_it_id_valid(id_list):
    id_input = -12
    while id_input not in id_list:
        id_input = input("Please enter product id:")

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

        get_quantity()


def stockroom_balance(item_id, item_quantity):
    for element in stockroom:
        id = int(element.get("id"))
        in_stock = int(element.get("stanje"))

        if id == item_id:
            if in_stock >= item_quantity:
                rest = in_stock - item_quantity
                element["stanje"] = rest
                return item_quantity, element
            else:
                print("The quantity of the product on stock is: ", in_stock)

                response = positive_negative_response(question="Do you want this amount of product?")
                if response:
                    element["stanje"] = 0
                    return in_stock, element
                else:

                    return None, None


def price_calculation(in_stock, element):
    product_price = float(element.get("jedinicna_cena"))
    total_product_price = round((in_stock * product_price),2)
    return total_product_price


def gate_question ():
    question = input("Do you like to continue shopping?")


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


body, header = open_csv(csv_path="/Users/kocijan/Downloads/magacin.csv")
stockroom = convertor_stockroom_in_dictionary(header, body)

response = "coco_shanel"
total_product_price = 0
while True:

    menu_generator(stockroom)
    id_list = get_item_id(stockroom)
    entered_id = check_is_it_id_valid(id_list)
    item_quantity = get_quantity()
    in_stock, element = stockroom_balance(entered_id, item_quantity)

    if in_stock and element:
        total_product_price += price_calculation(in_stock, element)
    negative_response = positive_negative_response(question="Would you like something else?")
    if not negative_response:
        break
print("Your bill is:", total_product_price,"euros")
print("Please take your receipt! ")
print("        Thank you!")
a=2