class Payslips:
    def __init__(self,name,payment,amount) -> None:
        self.name = name 
        self.payment= payment
        self.amount= amount
    def pay(self):
        self.payment="Yes"
    def status(self):
        if self.payment =="Yes":
         return self.name +" is paid "+str(self.amount)
        else:
         return self.name +" is not paid yet"

nathen=Payslips("Nathen","no",1000)
roger=Payslips("Roger","no",1000)
print(nathen.status()+"\n"+ roger.status())

nathen.pay()
print(nathen.status()+"\n"+ roger.status())