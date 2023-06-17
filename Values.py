def values(deal,sum):
    if(deal == 'K' or deal == 'Q' or deal == 'J'):
        return 10
    elif(deal == "A"):
        if(sum+11>21):
            return 1
        else:
            return 11
    return deal