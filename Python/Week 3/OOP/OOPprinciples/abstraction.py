from abc import ABC, abstractmethod
class employee(ABC):
    @abstractmethod
    def donate(self):
        pass
class donation(employee):
    def donate(self):
        a = input("How much would you like to donate: ")
        return a
john =donation()
j=john.donate()


peter =donation()
p= peter.donate()
