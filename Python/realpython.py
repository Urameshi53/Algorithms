

def mult(function):
    def y():
        d = 10
        print(d*4)
        function()
        d += 33
        print(d)
    return y
    

@mult
def say():
    print("Yeah")
