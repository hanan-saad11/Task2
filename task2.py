#>>> H <<<
for row_h in range(7):
    for col_h in range(6):
        if col_h == 0 or col_h == 5 or (row_h == 3 and (0 < col_h < 5)):
            print("$", end="")
        else:
            print(end=" ")
    print()
print("*********************************************************************************************")

#>>> E <<<
for row_e in range(7):
    for col_e in range(6):
        if col_e == 0 or ((row_e == 0 or row_e == 3 or row_e == 6) and (col_e > 0)):
            print("#", end="")
        else:
            print(end=" ")
    print()
print("*********************************************************************************************")

#>>> N <<<
for row_n in range(7):
    for col_n in range(6):
        if col_n == 0 or col_n==5 or row_n==col_n:
            print("&", end="")
        else:
            print(end=" ")
    print()
print("*********************************************************************************************")

#>>> A <<<
for row_a in range(7):
    for col_a in range(6):
        if ((col_a == 0 or col_a == 4) and row_a != 0) or (row_a == 0 or row_a == 3) and (0 < col_a < 4):
            print("@", end="")
        else:
            print(end=" ")
    print()
print("*********************************************************************************************")
