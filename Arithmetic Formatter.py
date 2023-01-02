p = ['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40']

def arithmetic_arranger(problems, show_solution = False):
    
    from re import search
    
    arranged_problems = ''
    problems_split = [i.split() for i in problems]
    
# Check for mistakes:  
    
    if len(problems) > 5:
        return "Error: Too many problems."
    
    for i in problems_split:
        if '/' in i or '*' in i:
            return "Error: Operator must be '+' or '-'."
        
    for i in problems_split:
        for j in i:
            if search(r".....+", j) != None:
                return "Error: Numbers cannot be more than four digits."
            if j not in ('+', '-'):
                try:
                    int(j)
                except:
                    return "Error: Numbers must only contain digits."
                
# Check is done

    rowl1 = []
    rowl2 = []
    rowl3 = []
    solution = []
    
    rows1 = ''
    rows2 = ''
    rows3 = ''
    solutions = ''
   

    for p in problems_split:
        
        first = p[0]
        second = p[2]
        interval = '    '
        
        lmax = str(max(int(first), int(second)))
        lmin = str(min(int(first), int(second)))
        
        answer_plus = str(int(first) + int(second))
        answer_minus = str(int(first) - int(second))
        
        if lmax == lmin:
            rowl1.append('  ' + first + interval)
            rowl2.append(p[1] + ' ' + second + interval)
            rowl3.append('-' * (len(lmax) + 2) + interval)
            if p[1] == '+':
                if len(answer_plus) > len(lmax):
                    solution.append(' ' + answer_plus + interval)
                else:
                    solution.append('  ' + answer_plus + interval)
            else:
                if len(answer_minus) > len(lmax):
                    solution.append(' ' + answer_minus + interval)
                else:
                    solution.append('  ' + answer_minus + interval)
        
        elif len(first) < len(lmax):
            rowl1.append('  ' + ' ' * (len(second) - len(first)) + first + interval)
            rowl2.append(p[1] + ' ' + second + interval)
            rowl3.append('-' * (len(lmax) + 2) + interval)
            if p[1] == '+':
                if len(answer_plus) > len(lmax):
                    solution.append(' ' + answer_plus + interval)
                else:
                    solution.append('  ' + answer_plus + interval)
            else:
                if len(answer_minus) > len(lmax):
                    solution.append(' ' + answer_minus + interval)
                else:
                    solution.append('  ' + answer_minus + interval)

        else:
            rowl1.append('  ' + first + interval)
            rowl2.append(p[1] + ' ' + ' ' * (len(first) - len(second)) + second + interval)
            rowl3.append('-' * (len(lmax) + 2) + interval)
            if p[1] == '+':
                if len(answer_plus) > len(lmax):
                    solution.append(' ' + answer_plus + interval)
                else:
                    solution.append('  ' + answer_plus + interval)
            else:
                if len(answer_minus) > len(lmax):
                    solution.append(' ' + answer_minus + interval)
                else:
                    solution.append('  ' + answer_minus + interval)

        
    for i in range(len(problems)):        
        rows1 += rowl1[i]
        rows2 += rowl2[i]
        rows3 += rowl3[i]
        solutions += solution[i]
        
    rows1 = rows1.rstrip()
    rows2 = rows2.rstrip()
    rows3 = rows3.rstrip()
    solutions = solutions.rstrip()
    
    if show_solution == False:
        arranged_problems += f'{rows1}\n{rows2}\n{rows3}'
    else:
        arranged_problems += f'{rows1}\n{rows2}\n{rows3}\n{solutions}'             

    return arranged_problems

print(arithmetic_arranger(p, True))



