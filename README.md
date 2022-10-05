# py-calculator
Put whatever formula you want and it will be calculated (take in count the priority calculation, parenthesis...)
You can add a variable to the input ( only known chemistry symbol accepted and make sure to add '_' at the end of each variable ex: 'm_') 
If you want to add your variable the line number refering to this function is arround 100.
The synthax to add a variable is (the example here is the variable called t):

    if split[t] == "t" and split[t + 1] == "_":

        formula.append("t")

To calculate the exponential of a number x, put ex
The same goes for sin, ahtan...
