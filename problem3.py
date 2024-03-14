class Product:
    def _init_(self, category, name, description, **attributes):
        self.category = category
        self.name = name
        self.description = description
        self.attributes = attributes

class ProductDatabase:
    def _init_(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def search(self, **criteria):
        results = []
        for product in self.products:
            match = all(getattr(product, key) == value for key, value in criteria.items())
            if match:
                results.append(product)
        return results

# Example usage
db = ProductDatabase()
db.add_product(Product(category='Electronics', name='Laptop', description='A portable computer', brand='Dell', price=800))
db.add_product(Product(category='Electronics', name='Smartphone', description='A mobile phone', brand='Samsung', price=500))
print(db.search(category='Electronics'))
