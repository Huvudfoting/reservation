adj_file = "data/adjectives.txt"
noun_file = "data/nouns.txt"
used_file = "data/used.txt"


def read_file(path: str) -> list[str]:
    f = open(path)
    return [line.strip() for line in f.readlines()]


def build_names() -> list[str]:
    adjectives = read_file(adj_file)
    nouns = read_file(noun_file)
    names = {f'{a} {n}' for a in adjectives for n in nouns}
    used = set(read_file(used_file))
    free = names - used
    return list(free)