from collections import defaultdict


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
        best_pizza, best_value = None, 0
        for pizza in self.recipes.values():
            value = 0
            for ingredient in pizza:
                if ingredient not in excluded:
                    value += 1
            if value >= best_value:
                best_pizza, best_value = pizza, value
        return best_pizza


def make_solution(nb_pizza, nb_t2, nb_t3, nb_t4, pizzas):
    orders = list()
    storage = Storage()
    for pizza in pizzas:
        storage.add_pizza(pizza=pizza)
    assert nb_pizza - 1 == storage.get_remaining_pizzas()
    teams = sorted([2 for _ in range(nb_t2)] \
                   + [3 for _ in range(nb_t3)] \
                   + [4 for _ in range(nb_t4)])
    while len(teams) > 0:
        size = teams.pop(-1)
        if size <= storage.get_remaining_pizzas():
            order = fulfill_order(size=size, storage=storage)
            orders.append(order)
    return orders


def fulfill_order(size, storage):
    order = list()
    used_ingredients = set()
    for _ in range(size):
        pizza = storage.get_pizza(excluded=used_ingredients)
        id = storage.remove_pizza(excluded=pizza)
        order.append(id)
        used_ingredients.update(pizza)
    return order
