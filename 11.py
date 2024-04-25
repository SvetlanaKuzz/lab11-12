
def z11_1():
    import random
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Restaurant name: {self.restaurant_name}")
            print(f"Restaurant name: {self.cuisine_type}")


        def open_restaurant(self):
            a = random.randint(0, 1)
            if a == 1:
                b = "open"
            else:
                b = "close"
            print(f"{self.restaurant_name} is {b}!")


    newRestaurant = Restaurant("Ristorante Italiano", "Italian")

    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def z11_2():
    import random
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Restaurant name: {self.restaurant_name}")
            print(f"Restaurant cuisine: {self.cuisine_type}")

        def open_restaurant(self):
            a = random.randint(0, 1)
            if a == 1:
                b = "open"
            else:
                b = "close"
            print(f"Restaurant {self.restaurant_name} is {b}!")

    restaurant1 = Restaurant("111", "Итальянская")
    restaurant2 = Restaurant("222", "Японская")
    restaurant3 = Restaurant("333", "Русская")

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

def z11_3():
    import random
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"Restaurant name: {self.restaurant_name}")
            print(f"Restaurant name: {self.cuisine_type}")
            print(f"Restaurant rating: {self.rating}")

        def open_restaurant(self):
            a = random.randint(0, 1)
            if a == 1:
                b = "open"
            else:
                b = "close"
            print(f"{self.restaurant_name} is {b}!")

        def up_rating(self, new_rate):
            self.rating = new_rate
            #with open("restaurant_rating.txt", "w") as file:
            #    file.write(f"{self.restaurant_name}: {self.rating}\n")


    restaurant1 = Restaurant("111", "Итальянская", 5)
    restaurant2 = Restaurant("222", "Японская", 4.8)
    restaurant3 = Restaurant("333", "Русская", 3)

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

    ans = input("Хотите поменять рейтинг ресторана?(да/нет): ")
    if ans.lower() == "да":
        ans2 = int(input("Выберите ресторан (1-3): "))
        rt = input("Введите новый рейтинг: ")
        if ans2 == 1:
            restaurant1.up_rating(rt)
            restaurant1.describe_restaurant()
        elif ans2 == 2:
            restaurant2.up_rating(rt)
            restaurant2.describe_restaurant()
        elif ans2 == 3:
            restaurant3.up_rating(rt)
            restaurant3.describe_restaurant()
        else:
            print("Некорректный номер ресторана")
    else:
        print("Ок")


def z12_1():
    import random
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"Ресторан: {self.restaurant_name}")
            print(f"Кухня: {self.cuisine_type}")
            print(f"Рейтинг: {self.rating}")

        def open_restaurant(self):
            a = random.randint(0, 1)
            if a == 1:
                b = "open"
            else:
                b = "close"
            print(f"{self.restaurant_name} is {b}!")

        def up_rating(self, new_rate):
            self.rating = new_rate

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, rating, flavors):
            super().__init__(restaurant_name, cuisine_type, rating)
            self.flavors = flavors

        def n_flavors(self):
            print("Вкусы мороженого:")
            for flavor in self.flavors:
                print(flavor)

        # Создаем экземпляр IceCreamStand
    ice_cream_stand = IceCreamStand("Sweets", "Ice Cream", 4.7, ["Ваниль", "Банан", "Клубника"])

        # Вызываем метод для вывода списка сортов мороженого
    ice_cream_stand.n_flavors()
    ice_cream_stand.describe_restaurant()


def z12_2():
    import random
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"Ресторан: {self.restaurant_name}")
            print(f"Кухня: {self.cuisine_type}")
            print(f"Рейтинг: {self.rating}")

        def open_restaurant(self):
            a = random.randint(0, 1)
            if a == 1:
                b = "open"
            else:
                b = "close"
            print(f"{self.restaurant_name} is {b}!")

        def up_rating(self, new_rate):
            self.rating = new_rate

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, rating, flavors, location, open_hours):
            super().__init__(restaurant_name, cuisine_type, rating)
            self.flavors = flavors
            self.location = location
            self.open_hours = open_hours

        def describe_restaurant(self):
            print(f"Ресторан: {self.restaurant_name}")
            print(f"Кухня: {self.cuisine_type}")
            print(f"Рейтинг: {self.rating}")
            print(f"Адрес: {self.location}")
            print(f"Рабочие часы: {self.open_hours}")

        def n_flavors(self):
            print("Вкусы мороженого:")
            for flavor in self.flavors:
                print(flavor)

        def new_flavors(self, new_flavor):
            self.flavors.append(new_flavor)

        def remove_flavors(self, flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f"Вкус {flavor} убран из меню")
            else:
                print(f"Вкуса {flavor} не найдено в меню")

        def check_flavor(self, flavor):
            if flavor in self.flavors:
                print(f"Вкус {flavor} в наличии")
            else:
                print(f"Вкуса {flavor} нет в наличии")

        def pop_ice_cream(self):
            print("У нас скоро появится мороженое на палочке")

        def soft_ice_cream(self):
            print("У нас скоро появится мягкое мороженое")

    # Создаем экземпляр IceCreamStand
    ice_cream_stand = IceCreamStand("Sweets", "Ice Cream", 4.7, ["Ваниль", "Банан", "Клубника"], "Riverville St", "10am-10pm")


    # Выводим меню и работаем с разными видами мороженого
    ice_cream_stand.describe_restaurant()
    ice_cream_stand.n_flavors()
    a = int(input("Сколько вкусов вы хотите добавить?: "))
    for i in range(0, a):
        new_flavor = input("Введите новый вкус: ")
        ice_cream_stand.new_flavors(new_flavor)

    flavor_r = input("Введите вкус, который хотите убрать:  ")
    ice_cream_stand.remove_flavors(flavor_r)

    flavor_check = input("Наличие какого вкуса Вы хотите проверить?: ")
    ice_cream_stand.check_flavor(flavor_check)

    # Подаем разные виды мороженого
    ice_cream_stand.pop_ice_cream()
    ice_cream_stand.soft_ice_cream()

    ice_cream_stand.n_flavors()



