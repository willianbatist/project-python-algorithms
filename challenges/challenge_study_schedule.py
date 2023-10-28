def study_schedule(permanence_period, target_time):
    
    try:
        for hour in permanence_period:
            if hour[0] <= target_time <= hour[1]:
                students += 1
    except TypeError:
        return None
    return students
