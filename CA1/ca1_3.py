T_majmoee = set()
str = input()
max_sub = 0;
temp_max = 0;
for i in range(len(str)):
    j = i
    while j < len(str):
        T_majmoee.add(str[j])
        temp_max = temp_max + 1
        if temp_max > len(T_majmoee):
            if max_sub < len(T_majmoee):
                max_sub = len(T_majmoee)
            temp_max = 0
            T_majmoee.clear()
            break
        j = j + 1

print(max_sub)