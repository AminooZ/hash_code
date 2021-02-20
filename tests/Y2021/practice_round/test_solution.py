import pytest

from src.hash_code.Y2021.practice_round.solution import Storage


class TestStorage:
    @pytest.mark.parametrize("pizza", [
        ['onion', 'pepper', 'olive'],
        ['mushroom', 'tomato', 'basil'],
        ['chicken', 'mushroom', 'pepper'],
        ['tomato', 'mushroom', 'basil'],
        ['chicken', 'basil']
    ])
    def test_add_pizza(self, pizza):
        pizza_id = "+".join(sorted(pizza))
        storage = Storage()
        storage.add_pizza(pizza=pizza)
        assert storage.index == 1
        assert storage.pizzas[pizza_id] == 1
        assert storage.recipes[pizza_id] == pizza
        assert storage.ids[pizza_id] == [0]
        storage.add_pizza(pizza=pizza)
        assert storage.index == 2
        assert storage.pizzas[pizza_id] == 2
        assert storage.recipes[pizza_id] == pizza
        assert storage.ids[pizza_id] == [0, 1]

    @pytest.mark.parametrize("pizza", [
        ['onion', 'pepper', 'olive'],
        ['mushroom', 'tomato', 'basil'],
        ['chicken', 'mushroom', 'pepper'],
        ['tomato', 'mushroom', 'basil'],
        ['chicken', 'basil']
    ])
    def test_remove_pizza(self, pizza):
        pizza_id = "+".join(sorted(pizza))
        storage = Storage()
        storage.add_pizza(pizza=pizza)
        storage.add_pizza(pizza=pizza)
        storage.remove_pizza(pizza=pizza)
        assert storage.index == 2
        assert storage.pizzas[pizza_id] == 1
        assert storage.recipes[pizza_id] == pizza
        assert storage.ids[pizza_id] == [0]
        storage.remove_pizza(pizza=pizza)
        assert storage.index == 2
        assert pizza_id not in storage.pizzas.keys()
        assert pizza_id not in storage.recipes.keys()
        assert pizza_id not in storage.ids.keys()

    @pytest.mark.parametrize("pizzas, excluded, expected", [
        (
                [
                    ['onion', 'pepper', 'olive', 'basil'],
                    ['mushroom', 'tomato', 'basil'],
                    ['chicken', 'mushroom', 'pepper'],
                    ['tomato', 'mushroom', 'basil'],
                    ['chicken', 'basil']
                ],
                [],
                ['onion', 'pepper', 'olive', 'basil']
        ),
        (
                [
                    ['onion', 'pepper', 'olive', 'basil'],
                    ['mushroom', 'tomato', 'basil'],
                    ['chicken', 'mushroom', 'pepper'],
                    ['tomato', 'mushroom', 'basil'],
                    ['chicken', 'basil']
                ],
                ['onion', 'basil'],
                ['chicken', 'mushroom', 'pepper']
        )
    ])
    def test_get_pizza(self, pizzas, excluded, expected):
        storage = Storage()
        for pizza in pizzas:
            storage.add_pizza(pizza=pizza)
        assert len(pizzas) == storage.get_remaining_pizzas()
        pizza = storage.get_pizza(excluded=excluded)
        assert pizza == expected
