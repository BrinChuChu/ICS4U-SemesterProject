solved = False
num = 20
divi = 19

while solved == False:
        
        if num % divi == 0:
            divi -= 1
            if divi == 10:
                solved = True
        else:
            num += 20
            divi = 19
            continue
print(num)
