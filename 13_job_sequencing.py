def job_sequencing(jobs):
    jobs.sort(key=lambda x: -x[2])
    n = max(j[1] for j in jobs)
    slots = [None]*n
    total_profit = 0
    for job in jobs:
        for i in range(min(n, job[1])-1, -1, -1):
            if not slots[i]:
                slots[i] = job[0]
                total_profit += job[2]
                break
    selected_jobs = [s for s in slots if s]
    return selected_jobs, total_profit

# (id, deadline, profit)
jobs = [('a',2,100),('b',1,19),('c',2,27),('d',1,25),('e',3,15)]
selected_jobs, total_profit = job_sequencing(jobs)
print(selected_jobs)
print(f"Total Profit: {total_profit}")
