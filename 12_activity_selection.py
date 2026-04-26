def activity_selection(start, end):
    activities = sorted(zip(start, end), key=lambda x: x[1])
    res, last = [activities[0]], activities[0][1]
    for s, e in activities[1:]:
        if s >= last: res.append((s,e)); last = e
    return res

s = [1,3,0,5,8,5]; e = [2,4,6,7,9,9]
print(activity_selection(s, e))
