def Display(no):
    if no >= 75:
        return "Distinction"
    elif no >= 60:
        return "First Class"
    elif no >= 50:
        return "Second Class"
    else:
        return "Fail"



def main():
    marks = int(input("Enter Marks : "))

    result = Display(marks)
    print(result)


if __name__ == "__main__":
    main()