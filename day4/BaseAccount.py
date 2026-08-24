from abc import ABC, abstractmethod

class BaseAccount(ABC):
    """Abstract Base Class enforcing the blueprint for all account types."""

    def __init__(self, account_number, holder_name, initial_balance):
        self.account_number = account_number
        self.holder_name = holder_name
        # Encapsulation: Double underscore makes this private
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__balance = float(initial_balance)  # Private variable to store balance 

    # Getter method to allow controlled access to private data
    def get_balance(self):
        """Returns the current balance of the account."""
        return self.__balance; 
    
    # Setter method with built-in validation rules
    def _modify_balance(self, amount):
        """Internal helper to safely mutate balance. Protected access."""
        self.__balance += float(amount)
    

    @abstractmethod
    def withdraw(self, amount):
        """Enforced abstraction: Child classes must implement custom withdrawal limits."""
        pass


    def deposit(self, amount):
        """Public method with strict business rules."""
        if amount <= 0:
            raise ValueError("❌ Error: Deposit amount must be positive.")
        self._modify_balance(amount)
        print(f"✅ Successfully deposited ₹{amount:.2f}")
        return True

    def display_details(self):
        """Prints account ledger specs cleanly."""
        print(f"\n--- Account Details ---")
        print(f"Account No: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Current Balance: ₹{self.get_balance():.2f}")


class SavingsAccount(BaseAccount):
    """Child Class implementing explicit inheritance and polymorphism rules."""

     def __init__(self, account_number, holder_name, initial_balance, minimum_balance=1000.0):
        # Forward setup directly to the parent class constructor
        super().__init__(account_number, holder_name, initial_balance)
        self.minimum_balance = float(minimum_balance)
        return True

    def withdraw(self, amount):
        """Polymorphic override of the abstract withdraw method with safe guard rails."""
        if amount <= 0:
            print("❌ Error: Withdrawal amount must be positive.")
            return False
        
        # Business logic validation check
        if (self.get_balance() - amount) < self.minimum_balance:
            print(f"❌ Error: Cannot withdraw. Minimum balance of ₹{self.minimum_balance:.2f} must be maintained.")
            return False

        self._modify_balance(-amount)
        print(f"✅ Successfully withdrew ₹{amount:.2f}")
        return True

    def display_details(self):
        """Polymorphic extension: Calls parent display, then adds unique features."""
        super().display_details()
        print(f"Account Type: Savings Account")
        print(f"Minimum Safe Limit: ₹{self.minimum_balance:.2f}")



# === EXECUTION / VERIFICATION WORKFLOW ===

def main():
    print("=== Creating New Secure Savings Account ===")
    # Instantiating our subclass object
    acct = SavingsAccount(account_number="SBI-2026-9041", holder_name="Mangesh", initial_balance=5000.0)
    
    # 1. Check account specifications
    acct.display_details()

    # 2. Test input validation and mutations
    print("\n>>> Testing Actions...")
    acct.deposit(1500.0)
    acct.withdraw(800.0)
    
    # 3. View balance securely via public getter
    print(f"Current isolated balance variable: ₹{acct.get_balance():.2f}")

    # 4. Test boundary limit protection rules
    print("\n>>> Testing Security Guardrails...")
    acct.withdraw(5000.0)  # Should be blocked by savings minimum balance rules
    
    # Verify values didn't break
    acct.display_details()



if __name__ == "__main__":
    main()