class Queques:
    def __init__(self):
        self.balance = 0
        print(" Welcome to the Deposit & Withdrawal Machine")

    def enqueue_deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def dequeue_withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def display(self):
        print("\n Net Available Balance=", self.balance)

    def _exit(self):
        exit()

if __name__ == '__main__':

    q = Queques()
    q.enqueue_deposit()
    q.dequeue_withdraw()
    q.display()
    q._exit()