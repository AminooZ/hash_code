import logging
import os

if __name__ == '__main__':
    file_name = "toto"
    logger = logging.getLogger()
    logger.info(f'Solving {file_name}')
    in_path = os.path.join("../../../../data/Y2021/practice_round/", file_name)
    out_path = os.path.join("../../../../submissions/Y2021/practice_round/", file_name)
    print("hello world")