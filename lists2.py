if __name__ == '__main__':
    N = int(input())
    list_a = []
# todo: insert a for loop that runs n times
for i in range (N):

    inputString = input()
    #todo remove unnecessary prints

    if(inputString.split()[0]=="insert"):
        i = int(inputString.split()[1])
        e = int(inputString.split()[2])
        list_a.insert(i, e)

    elif(inputString.split()[0]=="remove"):
        e=int(inputString.split()[1])
        list_a.remove(e)
#todo: complete the cases

    elif(inputString.split()[0]=="append"):
        e=int(inputString.split()[1])
        list_a.append(e)

    elif(inputString=="sort"):
        list_a.sort()

    elif(inputString=="pop"):
        list_a.pop()

    elif(inputString.split()[0]=="reverse"):
        list_a.reverse()
    else:
        print(list_a)






