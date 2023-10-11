def get_outcomes(pass_input_value, defer_input_value, fail_input_value):
    if (pass_input_value == 120 and defer_input_value == 0 and fail_input_value == 0):
        return "Progress"
    elif (pass_input_value == 100 and 0 <= defer_input_value <= 20 and fail_input_value <= 20 and fail_input_value >= 0):
        return "Progress (module trailer)"
    elif (40 <= pass_input_value <= 80 and 0 <= defer_input_value <= 80 and 0 <= fail_input_value <= 60):
        return "Do not progress - module retriever"
    elif (pass_input_value == 40 and defer_input_value == 0 and fail_input_value == 80):
        return "Exclude"
    elif (pass_input_value == 20 and 40 <= defer_input_value <= 100 and 0 <= fail_input_value <= 60):
        return "Do not progress - module retriever"
    elif (pass_input_value == 20 and 0 <= defer_input_value <= 20 and 80 <= fail_input_value <= 100):
        return "Exclude"
    elif (pass_input_value == 0 and 60 <= defer_input_value <= 120 and 0 <= fail_input_value <= 60):
        return "Do not progress - module retriever"
    else:
        return "Exclude"



def entering_queries():
    lst = ["pass", "defer", "fail"]
    lst_values = []
    outcome = "Integer required"
    
    for query in lst:
        value = input(f"Enter {query}: ")
        if (not value.isnumeric()):
            break
        elif (int(value) not in range(0, 140, 20)):
            outcome = "Out of range"
            break
        else:
            lst_values.append(int(value))

    return lst_values, outcome



def get_single_student_outcome():
    lst_values, outcome = entering_queries()
    
    if (len(lst_values) == 3):
        if sum(lst_values) == 120:
            pass_input_value, defer_input_value, fail_input_value = lst_values
            outcome = get_outcomes(pass_input_value, defer_input_value, fail_input_value) 
        else:
            outcome = "Total incorrect"
    
    return outcome

# print(get_single_student_outcome())



def histogram(lst_of_outcomes):
    counter = 0
    print("---------------------------------------------------------------")
    print("Histogram")  
    number_of_progresses = lst_of_outcomes.count("Progress")
    number_of_trailings = lst_of_outcomes.count("Progress (module trailer)")
    number_of_retrievers = lst_of_outcomes.count("Do not progress - module retriever")
    number_of_excludes = lst_of_outcomes.count("Exclude")
    lst_count = [number_of_progresses, number_of_trailings, number_of_retrievers, number_of_excludes]
    for i in range(len(lst_count)):
        if (lst_count[i] > 0):
            counter += lst_count[i]
    print("Progress ", number_of_progresses, ":", "*" * number_of_progresses)
    print("Trailer ", number_of_trailings, ":", "*" * number_of_trailings)
    print("Retriever ", number_of_retrievers, ":", "*" * number_of_retrievers)
    print("Excluded ", number_of_excludes, ":", "*" * number_of_excludes)
    print("\n")
    print(counter, "outcomes in total")
    print("---------------------------------------------------------------")


def get_multiple_students_outcomes():
    lst_of_outcomes = []
    y_or_q = 'y'
    while y_or_q == 'y':
        outcome = get_single_student_outcome()
        lst_of_outcomes.append(outcome)
        print(outcome)
        print("Would you like to enter another set of data?\n")
        print("Enter 'y' for yes or 'q' to quit and view results: ")
        while True:
            y_or_q = input()
            if (y_or_q == 'q' or y_or_q == 'y'):
                break
            else:
                print("Wrong query. Try again")
                continue
    else:
        histogram(lst_of_outcomes)

get_multiple_students_outcomes()
