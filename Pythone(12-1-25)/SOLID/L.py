class payment:
    def refund(self):
        print("Refund is availble")

class onlinepay(payment):
    def refund(self):
        print("Online pay also accepts refund policy")            

class Cash(payment):
    def refund(self):
        raise Exception("Not Avalible") 


class PaymentService:
    def __init__(self, payment_type):
        self.pay = payment_type

on = PaymentService(onlinepay())
ca = PaymentService(Cash())

on.pay.refund()
ca.pay.refund()  