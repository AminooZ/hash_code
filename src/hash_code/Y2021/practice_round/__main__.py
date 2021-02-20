import logging
import os
from src.hash_code.Y2021.practice_round.solution import make_solution
from src.hash_code.Y2021.practice_round.tools import format_input
from src.hash_code.Y2021.practice_round.tools import format_output
from src.hash_code.tools import read_file
from src.hash_code.tools import write_file

if __name__ == '__main__':
    files = [
        "a_example",
        "b_little_bit_of_everything.in",
        "c_many_ingredients.in",
        "d_many_pizzas.in",
        "e_many_teams.in"
    ]
    for file_name in files:
        logger = logging.getLogger()
        logger.info(f'Solving {file_name}')
        in_path = os.path.join("../../../../data/Y2021/practice_round/", file_name)
        out_path = os.path.join("../../../../submissions/Y2021/practice_round/", file_name)
        in_content = read_file(path=in_path)
        nb_pizza, nb_t2, nb_t3, nb_t4, pizzas = format_input(content=in_content)
        orders = make_solution(nb_pizza=nb_pizza,
                               nb_t2=nb_t2,
                               nb_t3=nb_t3,
                               nb_t4=nb_t4,
                               pizzas=pizzas)
        out_content = format_output(orders)
        write_file(content=out_content, path=out_path)
