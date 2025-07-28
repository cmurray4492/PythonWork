"""Basic Classes from Ashutosh Pawar Python course"""


class Parents:
    def __init__(self) -> None:
        self.balance = 50000


class Child(Parents):
    def __init__(self) -> None:
        super().__init__()
        self.age = 20


craig = Child()

print(craig.balance)
print(craig.age)
