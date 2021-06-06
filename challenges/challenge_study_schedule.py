def study_schedule(start_time, end_time, target_time):
    """ Faça o código aqui. """
    if not target_time or not start_time:
        return 0

    number_of_students_by_time = 0
    for index, start_study_time in enumerate(start_time):
        if start_study_time <= target_time <= end_time[index]:
            number_of_students_by_time += 1

    return number_of_students_by_time
