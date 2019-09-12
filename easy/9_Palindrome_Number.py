if __name__ == "__main__":
    line = raw_input()
    while line:
        x = int(line)
        string = str(x)
        length = len(string)
        flag = 1
        for i in xrange(length / 2):
            if string[i] != string[length - 1 - i]:
                flag = 0
                break
        if(flag):print "True"
        else:print "False"
        line = raw_input()