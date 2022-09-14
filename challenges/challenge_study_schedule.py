def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    schedule = 0
    for prohibited, exit in permanence_period:
        if type(prohibited) != int or type(exit) != int:
            return None
        elif prohibited <= target_time <= exit:
            schedule += 1

    return schedule
