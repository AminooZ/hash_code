import logging


def format_input(content):
    logger = logging.getLogger()
    logger.info(f'Formatting input')
    header, body = content[0], content[1:]
    nb_pizza, nb_t2, nb_t3, nb_t4 = [int(x) for x in header]
    pizzas = list()
    for line in body:
        nb_ingredients, ingredients = int(line[0]), line[1:]
        assert len(ingredients) == nb_ingredients
        pizzas.append(ingredients)
    return nb_pizza, nb_t2, nb_t3, nb_t4, pizzas


def format_output(orders, separator=" "):
    logger = logging.getLogger()
    logger.info(f'Formatting output')
    header = str(len(orders))
    body = list()
    for order in orders:
        line = [str(len(order))] + [str(pizza) for pizza in order]
        body.append(separator.join(line))
    content = [header] + body
    return content
