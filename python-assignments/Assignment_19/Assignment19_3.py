from functools import reduce

def ProcessList(data):
    fdata = list(filter(lambda x: x >= 70 and x <= 90, data))
    mdata = list(map(lambda x: x + 10, fdata))
    rdata = reduce(lambda a, b: a * b, mdata)
    return fdata,mdata,rdata


def main():
    data = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
    f, m, r = ProcessList(data)

    print("Input List =", data)
    print("List after filter =", f)
    print("List after map =", m)
    print("Output of reduce =", r)


if __name__ == "__main__":
    main()
