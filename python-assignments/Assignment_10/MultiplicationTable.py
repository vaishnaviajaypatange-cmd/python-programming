
def MultiplicationTable(No):
    table = []
    for i in range(1,11):
        table.append(No*i)
    return table


def main():
    No = 4
    result = MultiplicationTable(No)
    print(result)




if __name__ == "__main__":
    main()