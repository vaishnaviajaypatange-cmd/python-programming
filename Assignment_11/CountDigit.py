def CountDigit(No):
    no = str(No)
    ret = len(no)
    return ret


def main():
    No = 725144
    result = CountDigit(No)
    print(result)


if __name__ == "__main__":
    main()