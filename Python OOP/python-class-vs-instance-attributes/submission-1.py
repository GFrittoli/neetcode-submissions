class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0
    def __init__(self, name : str, balance : int) -> None:
        self.__name = name
        self.__balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance
    # Getter
    @property
    def name(self) -> str:
        return self.__name

    # Setter
    @name.setter
    def name(self, new_name: str) -> None:
        if new_name != "":
            self.__name = new_name
        else:
            print("Name cannot be empty!")

    # Getter
    @property
    def balance(self) -> str:
        return self.__balance

    # Setter
    @balance.setter
    def balance(self, new_balance: str) -> None:
        if new_balance != "":
            self.__balance = new_balance
        else:
            print("balance cannot be empty!")


# TODO: Create two accounts
Alice = BankAccount("Alice",1000)
Bob = BankAccount("Bob",2000)

# TODO: Print the information using the mentioned format

print(f"Alice's balance: ${Alice.balance}")
print(f"Bob's balance: ${Bob.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")