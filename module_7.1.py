class Product:
    def __init__(self, name, weight, category):
        self.name = 'Potato'
        self.weight = 0.0
        self.category = 'Vegetables'

    def __str__(self):
        return f'{self.name, self.weight, self.category}'


class Shop(Product):
    __file_name = 'products.txt'

    def get_products(self, __file_name):
        file = open(__file_name, 'r')
        text = file.read()
        file.close()
        return text

    def add(self, *products):
        current_product = self.get_products()
        file = open(current_product, 'a')
        text = file.read()
        for i in current_product:
            if i not in text:
                i.append(current_product)
            else:
                print(f'Продукт {self.name} уже есть в магазине.')
        file.close()







        


