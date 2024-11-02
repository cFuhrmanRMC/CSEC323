from AES_CBC import encrypt_AES_CBC, decrypt_AES_CBC
from bankAccount import BankAccount  

class CheckingAccount(BankAccount):
    def __init__(self, balance=0.0):
        super().__init__(balance, account_type="Checking")
        self.interest_rate = 0.015
        self.key = b'MySuperSecretKey1222222222222222'  # AES-256 key (32 bytes)
        self.iv = b'MySuperSecretIV1'  # IV (16 bytes)

    def withdrawal(self, amount):
        # Preconditions:
        assert amount > 0, "Withdrawal amount must be positive."
        assert amount <= self._balance, "Insufficient funds: Overdrafts are not allowed in CheckingAccount."

        success = super().withdrawal(amount)

        # Postconditions:
        assert self._balance >= 0, "Balance should not be negative after withdrawal."
        return success

    def add_interest(self):
        # Preconditions:
        assert self._balance >= 0, "Interest cannot be added to a negative balance."

        super().add_interest(self.interest_rate)

        # Postconditions:
        assert self._balance >= 0, "Balance should be non-negative after adding interest."

    def _save_transactions(self):
        with open("checking.txt", "wb") as outfile:
            for transaction in self._transaction_list:
                result = encrypt_AES_CBC(str(transaction), self.key, self.iv)
                outfile.write(str(len(result)).encode() + b"\n")
                outfile.write(result + b"\n")

    def _load_transactions(self):
        with open("checking.txt", "r+b") as infile:
            length = infile.readline().rstrip().decode()
            while length != "":
                length = int(length)
                data = infile.read(length)
                decrypted_data = decrypt_AES_CBC(data, self.key, self.iv)
                print(decrypted_data)
                infile.readline()
                length = infile.readline().rstrip().decode()
                
                
class SavingsAccount(BankAccount):
    def __init__(self, balance=0.0):
        super().__init__(balance, account_type="Savings")
        self.interest_rate = 0.04
        self.overdraft_count = 0
        self.key = b'MySuperSecretKey1222222222222222'  # AES-256 key (32 bytes)
        self.iv = b'MySuperSecretIV1'  # IV (16 bytes)

    def withdrawal(self, amount):
        # Preconditions:
        assert amount > 0, "Withdrawal amount must be positive."
        assert self.overdraft_count < 3 or self._balance >= 100, "Cannot withdraw: Balance must be at least $100 after 3 overdrafts."

        if amount > self._balance:
            # Apply overdraft fee
            self.overdraft_count += 1
            if self.overdraft_count == 1:
                fee = 20
            elif self.overdraft_count == 2:
                fee = 30
            else:
                fee = 50
            self._balance -= fee
            print("Overdraft fee applied:", fee)

        success = super().withdrawal(amount)

        # Postconditions:
        assert self.overdraft_count <= 3, "Overdraft count should not exceed 3."
        assert self._balance >= 0 or (self.overdraft_count < 3), "Balance should be >= $100 if overdrafts reach the limit of 3."
        return success

    def add_interest(self):
        # Preconditions:
        assert self._balance >= 0, "Interest cannot be added to a negative balance."

        super().add_interest(self.interest_rate)

        # Postconditions:
        if self._balance > 10000:
            self.overdraft_count = 0  # Reset overdraft count if balance exceeds $10,000
        assert self.overdraft_count >= 0, "Overdraft count should be non-negative."

    def _save_transactions(self):
        with open("savings.txt", "wb") as outfile:
            for transaction in self._transaction_list:
                result = encrypt_AES_CBC(str(transaction), self.key, self.iv)
                outfile.write(str(len(result)).encode() + b"\n")
                outfile.write(result + b"\n")

    def _load_transactions(self):
        with open("savings.txt", "r+b") as infile:
            length = infile.readline().rstrip().decode()
            while length != "":
                length = int(length)
                data = infile.read(length)
                decrypted_data = decrypt_AES_CBC(data, self.key, self.iv)
                print(decrypted_data)
                infile.readline()
                length = infile.readline().rstrip().decode()