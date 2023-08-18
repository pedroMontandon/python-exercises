def study_schedule(permanence_period, target_time=None):
    students = 0
    for st in permanence_period:
        try:
            if (st[0] <= target_time and st[1] >= target_time):
                students += 1
        except (TypeError, ValueError):
            return None
    return students
