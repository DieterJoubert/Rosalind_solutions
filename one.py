def ruleAsc(n):
    a = [0 for i in range(n + 1)]
    k = 1
    a[1] = n
    while k != 0:
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1
        while x <= y:
            a[k] = x
            y -= x
            k += 1
        a[k] = x + y
        print a[:k + 1]


def partCount(x):
  def p(sum,largest):
    if largest==0: return 0
    if sum==0: return 1
    if sum<0: return 0
    return p(sum-largest, largest) + p(sum, largest-1)
  return p(x,x)