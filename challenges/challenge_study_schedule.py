def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count = 0

    for permanence in permanence_period:
        entered = permanence[0]
        left = permanence[1]

        if type(entered) != int or type(left) != int:
            return None

        if entered <= target_time and left >= target_time:
            count += 1

    return count
