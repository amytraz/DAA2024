# Input for the number of jobs
n = int(input("Enter the number of jobs: "))

# Input for the jobs and their profits and deadlines
jobs = []
profits = []
deadlines = []

for i in range(n):
    jobs.append(i + 1)
    profits.append(int(input("Enter the profit for job " + str(i + 1) + ": ")))
    deadlines.append(int(input("Enter the deadline for job " + str(i + 1) + ": ")))

# Sorting the jobs according to the profits using Python's built-in sorted function
job_info = list(zip(profits, deadlines, jobs))
job_info = sorted(job_info, key=lambda x: x[0], reverse=True)

# Creating a blank list of size max
max_deadline = max(deadlines)
schedule = [" "] * max_deadline

tprofit = 0

# Scheduling the jobs
for profit, deadline, job in job_info:
    for j in range(deadline - 1, -1, -1):
        if schedule[j] == " ":
            schedule[j] = job
            tprofit += profit  
            break

# Displaying the schedule
print("The schedule is: ", *schedule)

print("The profit is: ", tprofit)
