#polymorphism

class payment:
    def pay(self,amount):
        print(f"paying with cash: ${amount}")

class credit_card_payment(payment):
    def pay(self,amount):
        print(f"paying with credit card: ${amount}")
        print("processing credit card payment")
class upipay_payment(payment):
    def pay(self,amount):
        print(f"paying with upi: ${amount}")
        print("processing upi payment")
class Wallet_payment(payment):
    def pay(self,amount):
        print(f"paying with wallet: ${amount}")
        print("processing wallet payment")


payments = [credit_card_payment(),upipay_payment(),Wallet_payment()]

for payment_method in payments:
    payment_method.pay(100)

#absract class

#send_notification()
from abc import ABC, abstractmethod
class email_notification(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass
class sms_notification(email_notification):
    def send_notification(self, message):
        print(f"Sending SMS notification: {message}")
class push_notification(email_notification):
    def send_notification(self, message):
        print(f"Sending Push notification: {message}")
notifications = [sms_notification(), push_notification()]
for notification in notifications:
    notification.send_notification("You have a new message!")
    


