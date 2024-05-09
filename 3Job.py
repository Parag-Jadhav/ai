def job_sequencing(jobs):
  jobs.sort(key=lambda job: job["profit"], reverse=True)

  latest_deadline = max(jobs, key=lambda job: job["deadline"])["deadline"] 
  schedule = [None] * latest_deadline
  total_profit = 0
  
  for job in jobs:
    # Assign task to its deadline slot (assuming it's free)
    schedule[job["deadline"] - 1] = job["id"]  # ID at deadline - 1
    total_profit += job["profit"]
  return schedule, total_profit

num_jobs = int(input("Enter the number of jobs: "))
jobs = []
for job_id in range(1, num_jobs + 1):
  job_details = {}  # Dictionary to store job info
  job_details["id"] = input(f"Enter job ID for job {job_id}: ")
  job_details["deadline"] = int(input(f"Enter deadline for job {job_id}: "))
  job_details["profit"] = int(input(f"Enter profit for job {job_id}: "))
  jobs.append(job_details)

sequence, total_profit = job_sequencing(jobs)
print("Job Sequence:", sequence)
print("Total Profit:", total_profit)
