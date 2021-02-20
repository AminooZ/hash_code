import logging


def read_file(path, line_terminator="\n", separator=" "):
    logger = logging.getLogger()
    logger.info(f'Reading {path}')
    f = open(path, "r")
    text = f.read().strip()
    lines = text.split(line_terminator)
    content = [line.strip().split(separator) for line in lines]
    return content


def write_file(content, path, line_terminator="\n"):
    logger = logging.getLogger()
    logger.info(f'Writing {path}')
    text = line_terminator.join(content)
    f = open(path, "w")
    f.write(text)


if __name__ == "__main__":
    example = read_file("../../data/Y2021/practice_round/a_example")
    print(example)
