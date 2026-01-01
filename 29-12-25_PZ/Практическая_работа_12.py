# 1
# class BankAccount:
#     def __init__(self, owner: str, balance: float = 0):
#         self.__owner = owner
#         self.__balance = balance
#
#     def deposit(self, amount: float) -> None:
#         if amount < 0:
#             raise ValueError("Сумма пополнения не может быть отрицательной.")
#         self.__balance += amount
#
#     def withdraw(self, amount: float) -> None:
#         if amount < 0:
#             raise ValueError("Сумма снятия не может быть отрицательной.")
#         if amount > self.__balance:
#             raise ValueError("Недостаточно средств на счёте.")
#         self.__balance -= amount
#
#     def get_balance(self):
#         return self.__balance
#
#     def get_owner(self):
#         return self.__owner
#
# account = BankAccount(owner="Иван Иванов", balance= 1000)
# print(account.get_balance())
# print(account.get_owner())
# account.deposit(200)
# print(account.get_balance())
# account.withdraw(100)
# print(account.get_balance())

# 2
class UserProfile:
    def __init__(self):
        self.__email = ""
        self.__age = 0
        self.__username = ""

    def get_email(self):
        return self.__email

    def get_age(self):
        return self.__age

    def get_username(self):
        return self.__username

    def set_email(self, email: str):
        try:
            if '@' not in email or '.' not in email:
                print(f"Ошибка установки email: Email должен содержать '@' и '.'")
                return False
            self.__email = email
            return True
        except Exception as e:
            print(f"Ошибка установки email: {e}")
            return False

    def set_age(self, age: int):
        try:
            if age < 13 or age > 120:
                print("Ошибка установки возраста: Возраст должен быть в диапазоне от 13 до 120 лет")
                return False
            self.__age = age
            return True
        except Exception as e:
            print(f"Ошибка установки возраста: {e}")
            return False

    def set_username(self, username: str) -> bool:
        try:
            if len(username) < 3 or len(username) > 20:
                print("Ошибка установки имени пользователя: Имя пользователя должно содержать от 3 до 20 символов")
                return False
            if ' ' in username:
                print("Ошибка установки имени пользователя: Имя пользователя не должно содержать пробелов")
                return False
            self.__username = username
            return True
        except Exception as e:
            print(f"Ошибка установки имени пользователя: {e}")
            return False

    def __str__(self):
        return (f"Имя пользователя = {self.__username}\n"
                f"Email = {self.__email}\n"
                f"Возраст = {self.__age} лет")


user = UserProfile()
user.set_email("user@example.com")
user.set_age(13)
user.set_username("john_doe")
print(user.__str__())
