import math

if __name__ == '__main__':

    a = int(input("Введите число начала интервала: "))
    b = int(input("Введите число конца интервала: "))
    step = int(input("Введите число шага интервала: "))
    f = open('D:/output.txt', 'w')
    try:
        for x in range(a, b + 1, step):
            z1 = (x ** 2 + 2 * x - 3 + (x + 1) * math.sqrt((x ** 2) - 9)) / (
                    x ** 2 - 2 * x - 3 + (x - 1) * math.sqrt((x ** 2) - 9))
            z2 = math.sqrt((x + 3) / (x - 3))
            print("x =", x, "  |  ", "z1 =", z1, "  |  ", "z2 =", z2)
            f.write("x = " + str(x) + "  |  " + "z1 = " + str(z1) + "  |  " + "z2 = " + str(z2) + "\n")
    except:
        print("Введены недопустимые значения, деление на ноль, отрицательный корень!")
        f.write("Введены недопустимые значения, деление на ноль, отрицательный корень!\n")
    f.close()
