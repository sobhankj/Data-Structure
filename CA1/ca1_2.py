def seperator_time(time_begin_end):
    list_time = time_begin_end.split(" ")
    return list_time

def calculate_time(time , AM_PM):
    h_min = time.split(":")
    total_min = int(h_min[0]) * 60 + int(h_min[1])
    if AM_PM == "PM" and int(h_min[0]) != 12:
        total_min = int(total_min) + 720
    elif AM_PM == "AM" and int(h_min[0]) == 12:
        total_min = int(total_min) - 720
    return total_min

def time_begin_and_end_person(list_time):
    t1 = calculate_time(list_time[0] , list_time[1])
    t2 = calculate_time(list_time[2] , list_time[3])
    l_t1_t2 = [t1 , t2]
    return l_t1_t2

def compare_times(t_main , l_t_compare):
    if int(l_t_compare[0]) <= int(t_main) <= int(l_t_compare[1]):
        return 1
    else:
        return 0
    
def print_result(list):
    for k in list:
        print(*k , sep="")
    
def main1():
    list_result = []
    # x = input()
    how_many_time_for_class_to_check = int(input())
    for i in range(how_many_time_for_class_to_check):
        time_res = []
        t_class = input()
        list_time = seperator_time(t_class)
        total_min_class_main = calculate_time(list_time[0] , list_time[1])
        how_many_person_to_check = int(input())
        for j in range(how_many_person_to_check):
            l_t_each_person = input()
            list_time_person_free = seperator_time(l_t_each_person)
            l_t1_t2 = time_begin_and_end_person(list_time_person_free)
            time_res.append(int(compare_times(total_min_class_main , l_t1_t2)))
        list_result.append(time_res)
    
    print_result(list_result)
            
main1()