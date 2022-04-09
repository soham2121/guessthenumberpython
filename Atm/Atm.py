from random import randrange

class Atm(object):
    def __init__(self, cardNumber, PIN, Balance):
        self.cardNumber = cardNumber
        self.PIN = PIN
        self.Balance = Balance
    
    def checkBalance(self):
        print("Your Account Balance Is ", self.Balance, "\n")

    def Withdraw(self):
        print("Your Account Balance Is: ", self.Balance)
        amount = int(input("Enter The Amount To Withdraw: "))
        print(amount, " Withdrawn From Your Account \n", "New Account Balance Is: ", self.Balance-amount, "\n")
    
cardnumber = input("Enter Your Card Number: ")
pin = int(input("Enter Your Pin: "))
balance = randrange(0, 5000, 500)

card = Atm(cardnumber, pin, balance)

card.checkBalance()
card.Withdraw()