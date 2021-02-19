def format_input(content):
    header, body = content[0], content[1:]
    nb_pizza, nb_t2, nb_t3, nb_t4 = [int(x) for x in header]
    pizzas = list()
    for line in body:
        nb_ingredients, ingredients = int(line[0]), line[1:]
        assert len(ingredients) == nb_ingredients
        pizzas.append(ingredients)
    return nb_pizza, nb_t2, nb_t3, nb_t4, pizzas


def format_output(orders, separator=" "):
    header = len(orders)
    body = list()
    for order in orders:
        body.append(len(order))
        body.append(separator.join(order))
    content = [header] + body
    return content
