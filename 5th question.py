def check(string):
        if string.isalpha() == True:
            print(" the string is alphabetic ")
        elif string.isnumeric() == True:
            print(" the give string is numeric ")
        elif string.isidentifier() == True:
            print(" the given string is numeric ")
        elif string.isspace() == True:
            print(" the given sting is whitespace")
        else:
            print(" invalid identifier ")



string = "gfg"
check(string)

string = " "
check(string)

string = "1234vg4"
check(string)




