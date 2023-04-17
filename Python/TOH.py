def TOH(num, start=1, end=3):
    if num:
        TOH(num-1, start, 6-start-end)
        print("Move disk %d from peg %d to peg %d" % (num,start, end))
        TOH(num-1, 6-start-end, end)

print(TOH(4))
