import re

def do_math(s):

    equation = ""

    # splits all digits and non-digits
    to_solve = re.findall(r'\d+|\D+', s)

    print(to_solve)
    
    # checks if first item is not a number
    if not to_solve[0].isdigit():

        to_solve.pop(0)

    # checks if last item is not a number
    if not to_solve[-1].isdigit():
        
        to_solve.pop(-1)

    for item in to_solve:

        # if item is a number, add it
        if item.isdigit():

            # normalize leading zeros instead in just equation += item, it might lead to example (1 + 01) which 01 leads to syntax error in eval()
            equation += str(int(item))

        # do this if item is not a number
        elif not item.isdigit():
            
            # if length is even, add a plus
            if len(item) % 2 == 0:

                equation += " + "

            # if length is odd, add a minus
            else:

                equation += " - "

    return eval(equation)

if __name__ == "__main__":

    print(do_math("5fkwo#10i#%.<>15P=@20!#B/25"))
    print(do_math("a.67,1$lk6ldf34@#LD@]2d32d2'2l3,@l3L#@2gh35s09if=df#$t9sm49t0df3$^%[vc;:0:4mt"))