def contains(a,b):
    ly1,lx1,ry1,rx1 = a
    ly2,lx2,ry2,rx2 = b 
    
    return ly2 > ly1 and ry2 < ry1 and lx2 > lx1 and rx2 < lx2

def intersects(a,b):
    # computes if rect a intersects b

    ly1,lx1,ry1,rx1 = a
    ly2,lx2,ry2,rx2 = b 


    disjoint = rx2 < lx1 or rx1 < lx2 or \
               ry1 < ly2 or ry2 < ly1

    contained = contains(a,b) or contains(b,a)
    return not disjoint and not contained

def larger(a,b):
    ly1,lx1,ry1,rx1 = a
    ly2,lx2,ry2,rx2 = b 

    if (ry1-ly1)*(rx1-lx1) > (ry2-ly2)*(rx2-lx2):
        return a
    else:
        return b