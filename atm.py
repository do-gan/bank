from account import Account

class Atm:
    def __init__(self, ac: Account, pin: int):
        self.ac = ac
        self.pin = pin

    def credit(self, ac: Account,amount: int):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        
        old_amount = self.ac.getAmount()
        new_amount = old_amount + amount
        self.ac.setAmount(new_amount)
        return new_amount

    def debit(self,ac: Account, amount: int):
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        old_amount = self.ac.getAmount()
        if amount > old_amount:
            raise ValueError("Insufficient funds.")

        new_amount = old_amount - amount
        self.ac.setAmount(new_amount)
        return new_amount
