
class Node:
    def __init__(s, k, v):
        s.k, s.v, s.r, s.L, s.R = k, v, True, None, None
    def rotate_left(s):
        rt = s.R
        rt.r, rt.L, s.r, s.R = s.r, s, True, rt.L
        return rt
    def rotate_right(s):
        rt = s.L
        s.L, rt.r, rt.R, s.r = rt.R, s.r, s, True
        return rt
    def shift_left(s):
        s.flip()
        if (s.R and s.R.L and s.R.L.r):
            s.R = s.R.rotate_right()
            s = s.rotate_left()
            s.flip()
        return s
    def shift_right(s):
        s.flip()
        if (s.L and s.L.L and s.L.L.r):
            s = s.rotate_right()
            s.flip()
        return s
    def split(s):
        s.r, s.L.r, s.R.r = True, False, False
    def flip(s):
        s.r = not s.r
        if s.L: s.L.r = not s.L.r
        if s.R: s.R.r = not s.L.r
    def balance(s, strict):
        if (s.R and s.R.r) and not (strict and s.L and s.L.r):
            s = s.rotate_left()
        if (s.L and s.L.r) and (s.L.L and s.L.L.r):
            s = s.rotate_right()
        if (s.L and s.L.r) and (s.R and s.R.r):
            s.split()
        return s

class TreeSet:
    def __init__(s, key=lambda x: x): s.rt, s.k = None, key
    def __contains__(s, val): return s.search(val) is not None

    def add(s, value):
        stk, key, result = [s.rt], s.k(value), None
        while result is None:
            nd = stk[-1]
            if not nd:
                stk.pop()
                result = Node(key, value)
            elif key <= nd.k: stk.append(nd.L)
            else: stk.append(nd.R)
        while len(stk) > 0:
            nd = stk.pop()
            if key <= nd.k: nd.L = result
            else: nd.R = result
            result = nd.balance(True)
        s.rt, s.rt.r = result, False

    def search(s, value):
        stk, key = [s.rt], s.k(value)
        while len(stk) > 0:
            nd = stk.pop()
            if nd is None: return None
            elif key < nd.k: stk.append(nd.L)
            elif key > nd.k: stk.append(nd.R)
            else: return nd.v

    def range(s, lo, hi):
        stk, lo, hi, results = [s.rt], s.k(lo), s.k(hi), []
        while len(stk) > 0:
            nd = stk.pop()
            if nd is None: continue
            if lo <= nd.k <= hi: results.append(nd.v)
            if lo < nd.k: stk.append(nd.L)
            if nd.k < hi: stk.append(nd.R)
        return results

    def remove(s, value):
        if s.rt is None: return None
        if not (s.rt and s.rt.L and s.rt.L.r) \
        and not (s.rt and s.rt.R and s.rt.R.r):
            s.rt.r = True
        s.rt = s._remove(s.rt, s.k(value))
        if s.rt is not None: s.rt.r = False

    def _remove(s, nd, key):
        if nd is None: return None
        if key < nd.k:
            if not (nd.L and nd.L.r) \
            and not (nd.L and nd.L.L and nd.L.L.r):
                nd = nd.shift_left()
            nd.L = s._remove(nd.L, key)
        else:
            if nd.L and nd.L.r: nd = nd.rotate_right()
            if key == nd.k and not nd.R: return None
            if not (nd.R and nd.R.r) \
            and not (nd.R and nd.R.L and nd.R.L.r):
                nd = nd.shift_right()
            if key == nd.k:
                nxt, nd.k, nd.v = s._min(nd.R), nxt.k, nxt.v
                nd.R = s._remove_min(nd.R)
            else:
                nd.r = s._remove(nd.r, key)
        return nd.balance(False)

    def min(s):
        return s._min(s.rt)

    def _min(s, nd):
        if nd is None: return None 
        stk = [nd]
        while len(stk) > 0:
            nd = stk.pop()
            if not nd.L: return nd
            else: stk.append(nd.L)

    def remove_min(s):
        if not (s.rt and s.rt.L and s.rt.L.r) \
        and not (s.rt and s.rt.R and s.rt.R.r):
            s.rt.r = True
        s.rt = s._remove_min(s.rt)
        s.rt.r = False

    def _remove_min(s, nd):
        if nd.L is None: return None
        if not (nd.L and nd.L.r) \
        and not (nd.L and nd.L.L and nd.L.L.r):
            nd = nd.shift_left()
        nd.L = s._remove_min(nd.L)
        return nd.balance(False)

    def max(s): return s._max(s.rt)

    def _max(s, nd):
        if nd is None: return None 
        stk = [nd]
        while len(stk) > 0:
            nd = stk.pop()
            if nd.R is None: return nd
            else: stk.append(nd.R)
    
    def remove_max(s):
        if not (s.rt and s.rt.L and s.rt.L.r) \
        and not (s.rt and s.rt.R and s.rt.R.r):
            s.rt.r = True
        s.rt = s._remove_max(s.rt)
        s.rt.r = False
        
    def _remove_max(s, nd):
        if nd.L and nd.L.r: nd = nd.rotate_right()
        if nd.R is None: return None
        if not (nd.R and nd.R.r) \
        and not (nd.R and nd.R.L and nd.R.L.r):
            nd = nd.shift_right()
        nd.R = s._remove_max(nd.R)
        return nd.balance(False)

    def floor(s, key):
        k = s.k(key)
        if s.rt:
            x = s._floor(s.rt, k);
            if x is not None: return x
            else: return None

    def _floor(s, nd, key):
        if not nd: return
        if key == nd.k: return nd.v
        if key < nd.k: return s._floor(nd.L, key)
        t = s._floor(nd.R, key)
        if t is not None: return t
        return nd.v
 
    def ceil(s, key):
        k = s.k(key)
        if s.rt:
            x = s._ceil(s.rt, k);
            if x is not None: return x
            else: return None

    def _ceil(s, nd, key):
        if not nd: return
        if key == nd.k: return nd.v
        if key > nd.k: return s._ceil(nd.R, key)
        t = s._ceil(nd.L, key)
        if t is not None: return t
        return nd.v