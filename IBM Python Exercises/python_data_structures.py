"""
def f(c):
    return sum(c)

"""
"""
class Car(object):
    def __init__(self,make,model,color):
        self.make=make;
        self.model=model;
        self.color=color;
        self.owner_number=0 
    def car_info(self):
        print("make: ",self.make)
        print("model:", self.model)
        print("color:",self.color)
        print("number of owners:",self.owner_number)
    def sell(self):
        self.owner_number=self.owner_number+1


my_car = Car(make="Honda", model="Accord", color="blue")
my_car2 = Car("Honda", "Accord", "blue")
my_car3 = Car(model="Accord", make="Honda", color="blue")
my_car4 = Car("Accord", "Honda", "blue")

my_car.car_info()
my_car2.car_info()
my_car3.car_info()
my_car4.car_info()
"""
"""
punctuation = ".!?"
name = "asdasd.asf!çli?"
name = name.translate(str.maketrans("", "", punctuation))
print(name)
"""
""" class analysedText(object):
    
    def __init__ (self, text):
        fmtText = text.lower()
        punctuation = ".!,?"
        fmtText = fmtText.translate(str.maketrans("", "", punctuation))
        self.fmtText = fmtText
        
    
    def freqAll(self):        
        word_list = self.fmtText.split()
        unique_words = {}
        for word in set(word_list):
            unique_words[word] = word_list.count()
            
        return unique_words
    
    def freqOf(self,word):
        freqDict = self.freqAll()
        for word in freqDict:
            return freqDict[word]
        else:
            return 0

sample = analysedText("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
test = sample.freqAll() """

"""
#exercise 1

x=1

if(x!=1):

    print('Hello')

else:

    print('Hi')

print('Mike') """

""" #exercise2
A=['1','2','3']

for a in A:

    print(2*a) """

""" #exercise 3
def Delta(x):

    if x==0:

        y=1;

    else:

        y=0;

    return(y)

print(Delta(0)) """

""" #exercise 4
B = [1,9,5,7,5]
print(B)
B.sort()
print(B) """

""" #exercise 5
A = {"a":1, "b":2}
print(A.keys()) """

A = [1,2,3,4,5]
A = A[1:]
A