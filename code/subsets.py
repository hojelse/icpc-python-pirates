# Bitmap-based iterative
num_elements = ??
for bitmap in range(1 << num_element):
  # element i is in the subset if i & bitmap != 0

# Recursive subset searching (backtracking-li)
def search(k, n, subset):
  if k == n:
    # process subset
  else:
    subset.push(k)
    search(k + 1, n, subset) # take element k in the set
    subset.pop() # backtrack
    search(k + 1, n, subset) # dont take element k in the set