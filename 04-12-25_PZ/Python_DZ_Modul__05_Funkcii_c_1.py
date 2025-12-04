# 3
def kvadrat(dlina, simvol, number):
    print(dlina * simvol)
    if dlina > 1:
        for i in range(dlina - 2):
            if number == "True":
                print(dlina * simvol)
            else:
                print(simvol + " " * (dlina - 2) + simvol)
    print(dlina * simvol)




kvadrat(10, "*", False)


























