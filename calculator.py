class calculator:
    def __init__(self,a1,b1):
        self.a=a1
        self.b=b1


    def add (self):
        c=self.a+self.b
        print(c)

    def sub (self):
        c=self.a-self.b
        print(c)


    def mul(self):
        c=self.a*self.b
        print(c)

    def div(self):
        c=self.a/self.b
        print(c)

ob=calculator(7,3)
ob.add()
ob.sub()
ob.mul()
ob.div()