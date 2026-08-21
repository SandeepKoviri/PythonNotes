'''
Abstraction
-----------
--> Abtstraction means hiding the implemented data and showing only need data to user

ABC --> abstract base class 
---> the abstract method is used to hide that perticular information 
of a bace class 

from abc import ABC, abstractmethod

class gov_bank(ABC):
    @abstractmethod
    def interest(self):
        print("goverment interest is 3")

class SBI_bank(gov_bank):
    def interest(self):
        print("SBI interest is 7.7")

class ICIC_bank(gov_bank):
    def interest(self):
        print("ICIC interest is 8.8")

obj = SBI_bank()
obj.interest()

obj1 = ICIC_bank()
obj1.interest()

from abc import ABC, abstractmethod

class cls_fee(ABC):
    @abstractmethod
    def fee_str(self):
        print("college fee is 77000")

class manag(cls_fee):
    def fee_str(self):
        print("college fee is 177000")

class em(cls_fee):
    def fee_str(self):
        print("college fee is 7000")

all = manag()
all.fee_str()

ap = em()
ap.fee_str()

from abc import ABC, abstractmethod

class cls_fee(ABC):
    @abstractmethod
    def fee_str(self):
        print("college fee is 77000")

class manag(cls_fee):
    def fee_str(self):
        print("college fee is 177000")

class em(cls_fee):
    def fee_str(self):
        print("college fee is 7000")

all = manag()
all.fee_str()

ap = em()
ap.fee_str()

'''
