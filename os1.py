def recursive(string, num):
    if num == 100:
        print('End of recursion')
        return False
    print("#{} - {}".format(string, num))
    recursive(string, num+1)


print(recursive('barev', 0))