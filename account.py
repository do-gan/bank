class Account:
    def __init__(self, bname: str, amount: int):
        self.bname = bname
        self.amount = amount

    def getName(self):
        return self.bname

    def getAmount(self):
        return self.amount

    def setAmount(self, amount: int):
        if amount < 0:
            print("Amount cannot be negative.")
        else:
            self.amount = amount


