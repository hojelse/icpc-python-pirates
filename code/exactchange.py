mem = dict()
def exactchange(price, coins):
    if price == 0:
        return 0
    elif price < 0 or coins < 0:
        return infi
    elif (price, coins) not in mem:
        mem[(price,coins)] = min(
            exactchange(price,coins-1), 
            exactchange(price-co[coins],coins-1)+1 
        )
    return mem[(price,coins)]