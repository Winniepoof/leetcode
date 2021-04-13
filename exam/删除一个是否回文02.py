def iss(num):
    def s(s):
        if s==s[::-1]:
            return True
        else:
            return False
    if s(num) is True:
        return True
    for i in range(len(num)):
        c=num[0:i]+num[i+1:]
        if s(c)is True:
            return True
        else:
            continue
    return False

if __name__ == "__main__":
    word = input()
    print(iss(word))