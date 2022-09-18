def arithmetic_arranger(problems, solve=False):

    if len(problems) > 5:
        return("Error: Too many problems.")
    
    x = []
    N1 = 0
    N2 = 0
    OP = ""
    sum_output = ""
    first = ""
    second = ""
    lines = ""
    sumx = 0
    sumxstr = ""

    for i in problems:
        x = i.split()

        try:
            N1 = int(x[0])
            N2 = int(x[2])
        except:
            return("Error: Numbers must only contain digits.")

        OP = x[1]

        if OP != "+" and OP != "-":
            return("Error: Operator must be '+' or '-'.")
        
        if len(str(N1)) > 4 or len(str(N2)) > 4:
            return("Error: Numbers cannot be more than four digits.")

        if OP == "+":
            sumx = N1 + N2
        if OP == "-":
            sumx = N1 - N2

        max_len = max(str(N1), str(N2), key=len)
        min_len = min(str(N1), str(N2), key=len)
        ar_max_len = int(len(max_len)) + 2
        ar_min_len = int(len(min_len))
        N1_aligned = str(N1).rjust(ar_max_len)
        N2_aligned = str(N2)
        sumx_aligned = str(sumx).rjust(ar_max_len)
    
        if len(str(N2)) < len(str(N1)):
            N2_aligned = str(N2).rjust(int(len(max_len)))
    
        line = '-' * ar_max_len

        if i != problems[-1]:
          first += N1_aligned + '    '
          second += OP + ' ' + N2_aligned + '    '
          lines += line + '    '
          sumxstr += sumx_aligned + '    '
        else:
          first += N1_aligned 
          second += OP + ' ' + N2_aligned
          lines += line 
          sumxstr += sumx_aligned

    if solve == True:
        sum_output = first + "\n" + second + "\n" + lines + "\n" + sumxstr
    else:
        sum_output = first + "\n" + second + "\n" + lines 
    return sum_output