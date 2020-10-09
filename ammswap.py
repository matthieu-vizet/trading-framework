# quantity to swap expressed in x
def swap(x,y,quantity):
    k = x * y
    nx = x + quantity
    ny = k / nx
    pricey = y - ny
    pricex = quantity / pricey
    slippage = (pricex - (x/y)) / (x/y)
    return pricex, slippage

    
    
