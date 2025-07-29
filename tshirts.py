
def size(cms):
    if cms < 30 or cms > 50:
        return 'F'  #F = Fail
    elif cms < 38:
        return 'S'
    elif cms < 42:
        return 'M'
    else:
        return 'L'


assert(size(37) == 'S')
assert(size(38) == 'M') #Might be S or M, to be discussed M
assert(size(40) == 'M')
assert(size(43) == 'L')
assert(size(5) == 'F')
assert(size(55) == 'F')
print("All is well (maybe!)")
