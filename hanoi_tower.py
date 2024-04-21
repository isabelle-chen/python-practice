# n: how many disks
# move from start to end

def hanoi(n, start, end):
    if n == 1:
        print(f"{start} -> {end}")
        
    else:
        # start = 1, end = 3, three rods in total, so total = 1+2+3
        other = 6 - start - end
        # n-1 disks: move the rest of disks except the biggest one to the middle
        #   it will move each of the disks one by one - recursive call hanoi(n, start, end).
        #       1st level n = 3
        #       2nd level n = n-1 = 2
        #       3rd level n = 2-1 = 1
        #   3rd level: n = 1, it will print result, then this level is finished
        #   it will go back to 2nd level to run the rest of code, until all finish at 1st level when n=3
        hanoi(n-1, start, other)
        # when (n-1) has been moved to the middle, move the biggest one
        hanoi(1, start, end)
        # move (n-1) to the end
        hanoi(n-1, other, end)

hanoi(3, 1, 3)
