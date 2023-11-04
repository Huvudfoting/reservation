import random

from NamePool import NamePool
from name_generator import build_names


def print_names():
    available = build_names()
    pool = NamePool(available)
    print(pool.size())
    sample = pool.draw(5)
    print(sample)


if __name__ == '__main__':
    print_names()
