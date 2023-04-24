def study_schedule(permanence, target_time):
    students = 0
    try:
        for hour in permanence:
            if hour[0] <= target_time <= hour[1]:
                students += 1
    except TypeError:
        return None
    return students
