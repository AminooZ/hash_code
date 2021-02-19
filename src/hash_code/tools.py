
def read_file(path, line_terminator="\n", separator=" "):
    f = open(path, "r")
    text = f.read().strip()
    lines = text.split(line_terminator)
    content = [line.strip().split(separator) for line in lines]
    return content


def write_file(content, path, line_terminator="\n"):
    text = line_terminator.join(content)
    f = open(path, "w")
    f.write(text)


if __name__ == "__main__":
    example = read_file("../../data/2021/practice_round/a_example")
    print(example)
