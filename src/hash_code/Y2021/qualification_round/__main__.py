import logging
import os

from hash_code.Y2021.qualification_round.solution import make_solution
from hash_code.Y2021.qualification_round.tools import format_input
from hash_code.Y2021.qualification_round.tools import format_output
from hash_code.tools import write_file
from src.hash_code.tools import read_file

if __name__ == '__main__':
    files = [
        "a.txt",
        "b.txt",
        "c.txt",
        "d.txt",
        "e.txt",
        "f.txt",
    ]
    for file_name in files:
        # file_name = "a.txt"
        logger = logging.getLogger()
        logger.info(f'Solving {file_name}')
        in_path = os.path.join("../../../../data/Y2021/qualification_round/", file_name)
        out_path = os.path.join("../../../../submissions/Y2021/qualification_round/", file_name)
        in_content = read_file(path=in_path)
        total_time, nb_intersection, reward, streets, cars = format_input(content=in_content)
        scheduler = make_solution(
            total_time=total_time,
            nb_intersection=nb_intersection,
            reward=reward,
            streets=streets,
            cars=cars
        )
        out_content = format_output(scheduler=scheduler)
        write_file(content=out_content, path=out_path)

