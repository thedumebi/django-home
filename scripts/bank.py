import csv
from bank.models import Category, Item

def run():
    item_list = Item.objects.all()
    fhand = open('bank/Database.csv')
    print(fhand)
    reader = csv.reader(fhand)
    next(reader)

    if item_list:
        for row in reader:
            for item in item_list:
                if row[1] == item.name:
                    item_a = Item.objects.get(name=row[1])
                    item_a.quantity = item.quantity + int(row[2])
                    item_a.price = int(row[3])
                    item_a.total_price = item_a.price * item_a.quantity
                    item_a.save()
                else:
                    continue


    else :
        for row in reader:
            name=row[1]
            item_name = name
            quantity=row[2]
            price=row[3]
            total_price=row[4]

            try:
                quantity = int(row[2])
            except:
                quantity = None

            try:
                price = int(row[3])
            except:
                price = None

            try:
                total_price = int(row[4])
            except:
                total_price = None
            category, created = Category.objects.get_or_create(name=row[5])

            item = Item(name = item_name, price = price, quantity = quantity, total_price = total_price, category = category)
            item.save()
        for row in reader:
            name=row[1]
            item_name = name
            quantity=row[2]
            price=row[3]
            total_price=row[4]

            try:
                quantity = int(row[2])
            except:
                quantity = None

            try:
                price = int(row[3])
            except:
                price = None

            try:
                total_price = int(row[4])
            except:
                total_price = None
            category, created = Category.objects.get_or_create(name=row[5])

            item = Item(name = item_name, price = price, quantity = quantity, total_price = total_price, category = category)
            item.save()
