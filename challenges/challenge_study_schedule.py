def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    count_target_time = 0
    for students in permanence_period:
        if type(students[0]) != int or type(students[1]) != int:
            return None
        # Solução lembrada pelo Gabriel Suassuna (entre valores);
        if students[0] <= target_time <= students[1]:
            count_target_time += 1
    return count_target_time
