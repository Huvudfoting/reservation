import random
from NameReservation import NameReservation


class NamePool:
    def __init__(self, pool: list[str] = None):
        self.reserved = {}
        if pool is None:
            self.pool = set()
        else:
            self.pool = set(pool)

    def draw(self, amount: int) -> list[str]:
        if not self.pool:
            raise Exception("The pool is empty.")
        amount = min(amount, len(self.pool))
        return random.sample(self.pool, amount)

    def reserve(self, name: str) -> NameReservation:
        if name not in self.pool:
            raise Exception("Name not in pool.")
        if name in self.reserved:
            raise Exception("Name already reserved.")
        reservation = NameReservation(name)
        self.reserved[name] = reservation
        self.pool.remove(name)
        return reservation

    def undo_reserve(self, name: str, secret: str) -> None:
        self.validate_request(name, secret)
        if self.reserved[name].confirmed:
            raise Exception("Name already confirmed.")
        self.reserved.pop(name)
        self.pool.add(name)

    def confirm_reserve(self, name: str, secret: str) -> NameReservation:
        self.validate_request(name, secret)
        self.reserved[name].confirmed = True
        return self.reserved[name]

    def add(self, *names: str) -> int:
        self.pool.update(names)
        return len(self.pool)

    def size(self) -> int:
        return len(self.pool)

    def validate_request(self, name: str, secret: str) -> None:
        if name not in self.reserved:
            raise Exception("Name not reserved.")
        if secret != self.reserved[name].secret:
            raise Exception("Secret not valid.")
