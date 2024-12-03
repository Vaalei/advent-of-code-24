import re

if __name__ == "__main__":
    f = open("input.txt", "r")
    sum = 0
    isEnabled = True
    for row in f:
        res = re.findall("mul\(\d+\,\d+\)|do\(\)|don\'t\(\)", row)
        for x in res:
            if x == "don't()":
                isEnabled = False
            elif x == "do()":
                isEnabled = True
            else:
                if isEnabled:
                    a, b = re.findall("\d+", x)
                    sum += int(a)*int(b)
    print(sum)