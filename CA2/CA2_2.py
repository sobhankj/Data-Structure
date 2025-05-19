pos_number = {}
temp_stack = []
perv_grater_pos = {}
stack_ans = []
output = [0]
n = int(input())
array_number = input().split(' ')
    
for i in range(len(array_number)) :
    pos_number[int(array_number[i])] = i
    
for i in range(len(array_number) , 0 , -1) :
    while len(temp_stack) != 0 and temp_stack[-1] >= pos_number[i]:
        temp_stack.pop()
    if len(temp_stack) == 0 :
        perv_grater_pos[i] = -1
        temp_stack.append(pos_number[i])
    else :
        perv_grater_pos[i] = temp_stack[-1]
        temp_stack.append(pos_number[i])

for i in range(1 , n + 1) :
    if perv_grater_pos[i] == -1 :
        stack_ans.clear()
        output.append(len(stack_ans))
        continue
    elif len(stack_ans) == 0 :
        stack_ans.append(pos_number[i])
        output.append(len(stack_ans))
        continue
    else :
        while len(stack_ans) != 0 and stack_ans[-1] > perv_grater_pos[i] :
            stack_ans.pop()
        if len(stack_ans) == 0 :
            stack_ans.append(pos_number[i])
            output.append(len(stack_ans))
            continue
        elif stack_ans[-1] < perv_grater_pos[i] :
            stack_ans.append(perv_grater_pos[i])
            output.append(len(stack_ans))
        elif stack_ans[-1] == perv_grater_pos[i]:
            output.append(len(stack_ans))
            pass

for i in output :
    print(i)
            
            
# n = int(input())
# array_number = input().split(' ')
# correct_guess = -0.5
# for i in range(n + 1) :
#     correct_guess += 1
#     answer = 0
#     max = n + 1
#     min = -1
#     check = []
#     for j in range(len(array_number)) :
#         if int(array_number[j]) > correct_guess and max > int(array_number[j]):
#             max = int(array_number[j])
#             check.append(1)
#         elif int(array_number[j]) < correct_guess and min < int(array_number[j]) : 
#             min = int(array_number[j])
#             check.append(0)
#             if check[len(check) - 2] == 1:
#                 answer += 1          
#     print(answer)