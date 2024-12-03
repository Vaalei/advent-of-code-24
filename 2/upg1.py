def checkasc(array):
    last = None
    for e in array:
        if last == None: pass
        elif e <= last or e > last + 3:
            return False
        last = e
    return True

def checkdesc(array):
    last = None
    for e in array:
        if last == None: pass
        elif e >= last or e < last - 3:
            return False
        last = e
    return True

def rowfunc(row):
    array = [int(x) for x in row.split()]
    if checkasc(array) or checkdesc(array):
        return True
    return False

if __name__ == "__main__":
    f = open("input.txt", "r")

    res = sum([rowfunc(row) for row in f])
    print(res)
