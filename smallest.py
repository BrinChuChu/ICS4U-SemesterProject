solved = False
num = 20
divi = [19,18,17,16,15,12,11]
possible_ans = 0
x = 0
while solved == False:
        
        if num % divi[x] == 0:
            x += 1
            if divi == 3:
                solved = True
            
        else:
            num += 20
            divi = 19
            continue
print(num)
