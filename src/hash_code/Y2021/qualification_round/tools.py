import logging
import os

from hash_code.tools import read_file


def format_input(content):
    logger = logging.getLogger()
    logger.info(f'Formatting input')
    header, body = content[0], content[1:]
    total_time, nb_intersection, nb_street, nb_car, reward = [int(x) for x in header]
    raw_streets, raw_cars = body[:nb_street], body[nb_street:]
    streets = [
        {
            "start": int(start),
            "end": int(end),
            "name": name,
            "length": length
        }
        for start, end, name, length in raw_streets
    ]
    cars = [trip[1:] for trip in raw_cars]
    assert nb_street == len(streets)
    assert nb_car == len(cars)
    return total_time, nb_intersection, reward, streets, cars


def format_output(scheduler, separator=" "):
    logger = logging.getLogger()
    logger.info(f'Formatting output')
    header = str(len(scheduler.keys()))
    body = list()
    for intersection, streets in scheduler.items():
        body.append(str(intersection))
        body.append(str(len(streets)))
        for street, time in streets.items():
            body.append(separator.join([street, str(time)]))
    content = [header] + body
    return content


#if __name__ == '__main__':
    # file_name = "a.txt"
    # logger = logging.getLogger()
    # logger.info(f'Solving {file_name}')
    # in_path = os.path.join("../../../../data/Y2021/qualification_round/", file_name)
    # out_path = os.path.join("../../../../submissions/Y2021/qualification_round/",
    #                         file_name)
    # in_content = read_file(path=in_path)
    # total_time, nb_intersection, reward, streets, cars = format_input(in_content)
    # print(total_time)
    # print(nb_intersection)
    # print(reward)
    # print(streets)
    # print(cars)

