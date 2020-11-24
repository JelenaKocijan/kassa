import sqlite3


def get_connection():
    conn = sqlite3.connect('magacin.db')
    return conn


def all_products(conn):
    results = conn.execute(
        """SELECT proizvod.id,proizvod.naziv, cena, kolicina,jedinica.naziv FROM proizvod
INNER JOIN stanje on
proizvod.id=stanje.proizvod_id
INNER JOIN jedinica ON
proizvod.jedinica_id=jedinica.id"""
    )
    product_list = []

    for row in results:
        product = {}
        product["id"] = row[0]
        product["naziv"] = row[1]
        product["kolicina"] = row[3]
        product["cena"] = row[2]
        product_list.append(product)

    return product_list
