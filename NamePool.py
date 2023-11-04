import random


class NamePool:
    def __init__(self, pool=None):
        if pool is None:
            self.pool = []
        else:
            self.pool = pool

    def draw(self, amount: int) -> list[str]:
        if not self.pool:
            raise Exception("The pool is empty.")
        amount = min(amount, len(self.pool))
        return random.sample(self.pool, amount)

    def add(self, *names: str) -> int:
        self.pool.extend(names)
        return len(self.pool)

    def remove(self, name: str) -> int:
        self.pool.remove(name)
        return len(self.pool)

    def size(self) -> int:
        return len(self.pool)