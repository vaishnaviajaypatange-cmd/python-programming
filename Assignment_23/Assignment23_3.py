class Numbers:

    def __init__(self):
        self.value = int(input("Enter the number : "))

    def ChkPrime(self):
        if self.value < 2:
            return False

        for i in range(2, self.value):
            if self.value % i == 0:
                return False
        return True

    def Factors(self):
        print("Factors:", end=" ")
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                print(i, end=" ")
        print()   # new line after loop

    def SumFactors(self):
        sum = 0
        for i in range(1, self.value):
            if self.value % i == 0:
                sum += i
        return sum

    def ChkPerfect(self):
        return self.SumFactors() == self.value



obj1 = Numbers()
print("Prime:", obj1.ChkPrime())
print("Perfect:", obj1.ChkPerfect())
obj1.Factors()




obj2 = Numbers()
print("Prime:", obj2.ChkPrime())
print("Perfect:", obj2.ChkPerfect())
obj2.Factors()
