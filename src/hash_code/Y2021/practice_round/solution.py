import logging
from collections import defaultdict

from tqdm import tqdm


class Storage:
    def __init__(self):
        self.pizzas = defaultdict(int)
        self.recipes = dict()
        self.ids = defaultdict(list)
        self.index = 0

    def add_pizza(self, pizza):
        pizza_id = "+".join(sorted(pizza))
        self.pizzas[pizza_id] += 1
        self.recipes[pizza_id] = pizza
        self.ids[pizza_id].append(self.index)
        self.index += 1

    def remove_pizza(self, pizza):
        pizza_id = "+".join(sorted(pizza))
        capacity = self.pizzas[pizza_id]
        assert capacity > 0, f"{pizza_id} is out of stock"
        id = self.ids[pizza_id].pop(-1)
        if capacity == 1:
            del self.recipes[pizza_id]
            del self.pizzas[pizza_id]
            del self.ids[pizza_id]
        else:
            self.pizzas[pizza_id] -= 1
        return id

    def get_remaining_pizzas(self):
        return sum([value for key, value in self.pizzas.items()])

    def get_pizza(self, excluded):
        best_pizza, best_value, least_ingredients = None, -1, 0
        for pizza in self.recipes.values():
            value = 0
            for ingredient in pizza:
                if ingredient not in excluded:
                    value += 1
            if value > best_value:
                best_pizza, best_value = pizza, value
            elif value == best_value and len(pizza) < least_ingredients:
                best_pizza, best_value = pizza, value
        return best_pizza


def make_solution(nb_pizza, nb_t2, nb_t3, nb_t4, pizzas):
    logger = logging.getLogger()
    logger.info(f'Preparing {nb_pizza} pizzas')
    orders = list()
    storage = Storage()
    for pizza in tqdm(pizzas, desc="Storage progress"):
        storage.add_pizza(pizza=pizza)
    assert nb_pizza == storage.get_remaining_pizzas()
    logger.info(f'Fulfilling orders: {nb_t2} teams of 2, '
                f'{nb_t3} teams of 3, and {nb_t4} teams of 4.')
    pizza_bar = tqdm(total=nb_pizza, desc="Pizza consumption progress")
    total_score = 0
    teams = {
        2: nb_t2,
        3: nb_t3,
        4: nb_t4
    }
    teams_bar = {key: tqdm(total=value, desc=f'Teams of {key} progress')
                 for key, value in teams.items()}
    remaining_pizzas = storage.get_remaining_pizzas()
    sizes = [key for key, value in teams.items()
             if value > 0 and key <= remaining_pizzas]
    while nb_t2 + nb_t3 + nb_t4 > 0 and len(sizes) > 0:
        order, score = fulfill_order(sizes=sizes, storage=storage)
        size = len(order)
        orders.append(order)
        pizza_bar.update(size)
        teams_bar[size].update(1)
        total_score += score ** 2
        teams[size] -= 1
        remaining_pizzas = storage.get_remaining_pizzas()
        sizes = [key for key, value in teams.items()
                 if value > 0 and key <= remaining_pizzas]
    logger.info(f'Collected {total_score} points')
    return orders


def fulfill_order(sizes, storage):
    order = list()
    used_ingredients = set()
    score = 0
    for index in range(max(sizes)):
        pizza = storage.get_pizza(excluded=used_ingredients)
        used_ingredients.update(pizza)
        if len(used_ingredients) == score and len(order) in sizes:
            break
        else:
            id = storage.remove_pizza(pizza=pizza)
            order.append(id)
            score = len(used_ingredients)
    return order, score
