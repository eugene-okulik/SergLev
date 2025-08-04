class Flower:
    def __init__(self, name, color, price, freshness_days):
        self.name = name
        self.color = color
        self.price = price
        self.freshness_days = freshness_days

    def __repr__(self):
        return f"{self.name}({self.color}, {self.price}₽, {self.freshness_days}дн)"


class Rose(Flower):
    def __init__(self, color, price, freshness_days):
        super().__init__("Роза", color, price, freshness_days)


class Tulip(Flower):
    def __init__(self, color, price, freshness_days):
        super().__init__("Тюльпан", color, price, freshness_days)


class Chamomile(Flower):
    def __init__(self, color, price, freshness_days):
        super().__init__("Ромашка", color, price, freshness_days)


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def total_price(self):
        return sum(flower.price for flower in self.flowers)

    def average_freshness(self):
        if not self.flowers:
            return 0
        return sum(flower.freshness_days for flower in self.flowers) / len(self.flowers)

    def sort_by(self, attribute):
        if not hasattr(self.flowers[0], attribute):
            print(f"Невозможно отсортировать по '{attribute}' — такого атрибута нет.")
            return
        self.flowers.sort(key=lambda flower: getattr(flower, attribute))

    def find_by_freshness(self, min_days):
        return [flower for flower in self.flowers if flower.freshness_days >= min_days]

    def __repr__(self):
        return f"Букет: {self.flowers}"


# Создаём цветы
rose1 = Rose("красный", 50, 7)
rose2 = Rose("белый", 45, 6)
tulip1 = Tulip("жёлтый", 40, 8)
chamomile1 = Chamomile("белый", 30, 5)

# Собираем букет
my_bouquet = Bouquet([rose1, rose2, tulip1, chamomile1])

print(my_bouquet)

print("Стоимость букета:", my_bouquet.total_price(), "₽")

print("Среднее время увядания:", my_bouquet.average_freshness(), "дней")

# Поиск цветов, которые живут не менее 6 дней
fresh_flowers = my_bouquet.find_by_freshness(7)
print("Цветы, живущие не менее 7 дней:", fresh_flowers)
