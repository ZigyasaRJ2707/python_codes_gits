def printDiamondFilled(n): 
    w = 2*n - 1 #width of background square 

    for row in range(1, n+1): 
        dist_from_row = int(abs((n+1)/2 - row))  # how away a row is from middle row 
        numStars = n - (2*dist_from_row)

        len_star = 2*numStars - 1         # construct line middle
        str_middle = "" # empty 
        for starNum in range(1, numStars+1): 
            if starNum!=numStars: 
                str_middle+= "* "
            else: 
                str_middle+="*"

        length_margin = int((w-len_star)/2)
        str_margin = " " * length_margin
        print(f"{str_margin}{str_middle}{str_margin}\n")


n = 11
printDiamondFilled(n)