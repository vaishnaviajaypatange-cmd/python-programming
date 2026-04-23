from math import pi
def Area(radius):
    return pi*radius**2



def main():
    radius = int(input("Enter Radius : "))
    result = Area(radius)
    print("Area of the Circle : ",result)




if __name__ == "__main__":
    main()