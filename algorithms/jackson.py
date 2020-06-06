
# 1) List the jobs and their times at each work center.
# 2) Select the job with the shortest activity time.
# If that activity time is for the first work center, then schedule the job first. If that activity time is for the second work center then schedule the job last. Break ties arbitrarily.
# 3) Eliminate the shortest job from further consideration.
# 4) Repeat steps 2 and 3, working towards the center of the job schedule until all jobs have been scheduled.
def jackson():
    print('Jacksons Algorithm')
