#functions 
# def add(a, b):
#     return a + b 

# print(add(10,20))

#calculator
a = int(input("Enter first  number "))
b = int(input("Enter second number "))
def add(a , b):
    return a + b

def different(a , b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error zero se divide nhi ho skta."
    return a / b


print("---Calculator Menu---")
print("1. Add(+)")
print("2. Subtract(-)")
print("3. Multiply(*)")
print("4. divide(/)")

choice = input("Enter your choice (1-4):")

if choice == "1":
    print("Result", add(a , b))
elif choice == "2":
    print("Result", add(a , b))
elif choice == "3":
    print("Result", add(a , b))
elif choice == "4":
     print("Result", add(a , b))
else:
    print("Invalid choice")
        
# def greet(name= "student"):
#     print("Hello", name)

# greet()
# greet("Sumit")

#mini project 2: student grade calculator

print("--- Enter subject marks(out of 100)")
sub1 = float(input("Enter subject 1 marks:"))
sub2 = float(input("Enter subject 2 marks:"))
sub3 = float(input("Enter subject 3 marks:"))

total_marks = sub1 + sub2 + sub3 
percentage = (total_marks / 300) *100

if percentage >= 90:
    Grade = "A"
elif percentage >= 80:
     Grade = "B"
elif percentage >= 70:
   Grade = "C"
elif percentage >= 60:
    Grade = "D"
else:
    Grade = "f(fail)"

print("---final report card---")
print(f"Total marks obtained: {total_marks}/300")
print(f"percentage: {percentage:.2f}%")
print(f"final Grade: {Grade}")


#args and kwargs 

# def total (*numbers):
#     return sum(numbers)

# def student_info(**data):
#     print(data)


#making bank account

account_holder ="Alex Mercer"
account_number = "987654321"
balance = 1000.0

def deposit(amount):
    """ Adds money to the global balance."""
    global balance # tells python to modify the global variable

    if amount > 0:
        balance += amount
        print(f" Successfully deposted: ${amount:.2f}")
    else:
        print(" error: deposit amount must be positive.")

def withdraw(amount):
    """ deducts money from the global balance if fouds are available."""
    global balance

    if amount > balance:
        print(f"Error: Insufficient funds! current balance is ${balance:.2f}")
    elif amount <= 0:
        print("Error: Withdrawal amount must be positive.")
    else:
        balance -= amount
        print(f" succesfully withdrwa: ${amount:.2f}")
def check_balance():
    """Reads and prints the current balance."""
    # We do NOT need the 'global' keyword here because we are only READING, not modifying.
    print(f"💰 Current Account Balance: ${balance:.2f}")


def show_account():
    """Displays comprehensive account and balance information."""
    # Local variable specific to this function's print formatting
    border = "==============================" 
    
    print(f"\n{border}")
    print("       BANK ACCOUNT INFO       ")
    print(border)
    print(f"👤 Holder:  {account_holder}")
    print(f"🔢 Account: #{account_number}")
    print(f"💵 Balance: ${balance:.2f}")
    print(f"{border}\n")


# --- Testing the Bank Account System ---

# 1. Look at initial account state
show_account()

# 2. Deposit some money
deposit(250.50)

# 3. Try to withdraw too much money
withdraw(2000.00)

# 4. Withdraw an allowable amount
withdraw(400.00)

# 5. Check balance independently
check_balance()

# 6. Show final profile overview
show_account()
