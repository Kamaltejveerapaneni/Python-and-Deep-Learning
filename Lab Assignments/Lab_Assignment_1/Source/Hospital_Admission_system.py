class patient:
                                                    #BASE CLASS FOR THE NEXT CLASSES
    i=0
    def __init__(self,name,**kwargs):              #__INIT__ function used
        self.name = name
        patient.i=patient.i+1
    def book_appointment(self):
        print("The appoitment is booked for tommorowm Mr.", self.name)
    def basic_info(self):
        print("the patients info is ")

class doctor(patient):
                                                    #INHERITENCE USING THE BASIC CLASS
                                                    #class inherited from patient
    j = 0
    def __init__(self,name, age, D_O_B,**kwargs):           #__INIT__ function used
        self.name=name
        self.age = age
        self.D_O_B = D_O_B
        super(doctor,self).__init__(name=name, age=age, D_O_B=D_O_B)
    def prescription(self):
        print("Go to medical shop")
    def fees_payment(self):
        print("pay to clerk... baraaluu levuuu")
class clerk(doctor):
    k = 0
    def __init__(self, disease,**kwargs):       #__INIT__ function used
        self.disease = disease
        super(clerk,self).__init__(**kwargs)
    def fees_payment(self):
        print("payment of", self.disease, "100$")              #SUPER Key WORD USED

class Nurse(clerk,doctor):
    def __init__(self, name, age, disease, D_O_B, weight):
        self.weight = weight
        super(Nurse, self).__init__(name=name, age=age, disease=disease, D_O_B=D_O_B)
    def suggestions(self):
        print("Better chekc you weight", self.weight)
class emergency():
    def __init__(self, is_it,gender):
        self.is_it=is_it
        self.gender=gender
    def join_emergency(self):
        print("the situation is worst?",self.is_it)
        print("the admit is ",self.gender)

print("Patient is Base class where object creation is shown")
obj_1 = patient("vinay")
obj_1.book_appointment()
print(".")
print(".")
print(".")

print("Here super key word is used to pass arguments")
obj_2 = doctor("vinay", 23, "08/22/1996")
obj_2.basic_info()
print(".")
print(".")
print(".")
                                                            #print("THIS IS OBJECT_3 INFO")
                                                            #obj_3 =clerk("vinay")
                                                               #obj_3.fees_payment()
print("Here, Multiple Inheritence is used ")
obj_4 = Nurse("vinay", 23, "Fever", "08/22/1996",72)                #Multiple Inheritence is uaing this object.
obj_4.prescription()
print(".")
print(".")
print(".")
print("Here, private item value is")
print(patient.i)







