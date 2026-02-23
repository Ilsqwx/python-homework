# 1
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    @property
    def balance(self):
        return self.__balance


# 2
class UserProfile:
    def __init__(self, email):
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if "@" in value:
            self.__email = value


# 3
class Battery:
    def __init__(self, charge):
        if 0 <= charge <= 100:
            self.__charge = charge
        else:
            self.__charge = 0

    @property
    def charge(self):
        return self.__charge


# 4
class Speaker:
    def __init__(self, volume):
        if 0 <= volume <= 10:
            self.__volume = volume
        else:
            self.__volume = 0

    @property
    def volume(self):
        return self.__volume


# 5
class Character:
    def __init__(self, health):
        self.__health = health

    def damage(self, amount):
        self.__health -= amount
        if self.__health < 0:
            self.__health = 0

    def heal(self, amount):
        self.__health += amount

    @property
    def health(self):
        return self.__health


# 6️ 
class PasswordManager:
    def __init__(self, password):
        self.__password = password

    def change_password(self, old, new):
        if old == self.__password and len(new) >= 8:
            self.__password = new