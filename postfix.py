def eval_expr(s,d={}):
    
    tmp = []
    s = s.split()

    for i in s:
        if i.isnumeric():
            tmp.append(i)
        elif i in d:
            tmp.append(d[i])
        else:
                x = int(tmp.pop())
                y = int(tmp.pop())
        if i == "+":
                tmp.append(x + y)
        elif i == "-":
                tmp.append(x - y)
        elif i== "*":
                tmp.append(x * y)
        elif i == "/":
                tmp.append(x // y)

    return tmp[0]


def to_infix(s):

    tmp = []
    s = s.split()

    for i in s:

        if i.isnumeric():
            tmp.append(i)

        else:
            x = tmp.pop()
            y = tmp.pop()

            if (i == "+"):
                tmp.append('('+ x +' + '+ y +')')
            
            elif (i == "-"):
                tmp.append('('+ x +' - '+ y +')')

            elif (i == "*"):
                tmp.append('('+ x +' * '+ y +')')

            elif (i == "/"):
                tmp.append('('+ x +' / '+ y +')')

    return tmp[0]
