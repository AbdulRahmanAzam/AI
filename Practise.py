# ======================================== JOB SCHEDULING USING CSP ===================================
from ortools.sat.python import cp_model
def job_scheduling_problem():
    model = cp_model.CpModel()

    job_durations = [5, 3, 8, 6, 2]
    num_jobs = len(job_durations)

    horizon = sum(job_durations)

    start_vars = []
    end_vars = []
    interval_vars = []

    for i in range(num_jobs):
        start = model.NewIntVar(0, horizon, f'start_time_{i}')
        end = model.NewIntVar(0, horizon, f'end_time_{i}')
        interval = model.NewIntervalVar(start, job_durations[i], end, f'interval_{i}')

        start_vars.append(start)
        end_vars.append(end)
        interval_vars.append(interval)
    
    model.AddNoOverlap(interval_vars)

    makespan = model.NewIntVar(0, horizon, 'makespan')
    model.AddMaxEquality(makespan, end_vars)
    model.Minimize(makespan)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f'Optimal schedule found: {solver.Value(makespan)}')
        for i in range(num_jobs):
            print(f'Job {i+1} starts at {solver.Value(start_vars[i])} and ends at {solver.Value(end_vars[i])}')
    else:
        print('No optimal or feasible solution found')

job_scheduling_problem()
