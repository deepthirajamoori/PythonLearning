import math


def showInfo(student_name='unknown', showAverage='True', showStdDev='False', **score):
    fullstr = " "
    sum = 0
    loopcount = 0
    x = 0
    total_sum = 0
    for kw in score:
        loopcount = loopcount + 1
        concat_str = str(loopcount) + ":" + str(score[kw]) + ";"
        print(concat_str)
        fullstr = fullstr + concat_str
        sum = sum + score[kw]
        avg = sum / loopcount
        total_sum += (score[kw] - avg) ** 2
        under_root = total_sum / loopcount
        stdv = math.sqrt(under_root)

    print(fullstr, avg, stdv)

    return (student_name + " has scores of " + fullstr + "." +
            " The average is " + str(avg) + "." + "The standard deviation is " + str(stdv))


showInfo('deepthi', a=100, b=95, c=99)
