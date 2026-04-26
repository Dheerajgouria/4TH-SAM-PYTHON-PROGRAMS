def knapsack(W, items):
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    val = 0
    for w, v in items:
        if W >= w: val += v; W -= w
        else: val += v * W/w; break
    return val

items = [(10,60),(20,100),(30,120)]
print(knapsack(50, items))
