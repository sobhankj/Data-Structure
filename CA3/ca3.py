import heapq

number_of_teacher , number_of_day = [int(i) for i in input().split(' ')]
teachers = []
for i in range(int(number_of_teacher)) :
    teachers.append([int(i) for i in input().split(' ')])
    
teachers.sort(key=lambda x: x[0])
max_heap = []
c_teacher = 0
c = 0

for i in range(1 , number_of_day + 1) :
    for j in range(c_teacher , len(teachers)) :
        if teachers[j][0] <= i :
            heapq.heappush(max_heap, [-1 * teachers[j][2] , teachers[j][1]])
            c += 1
        else :
            break
    
    c_teacher = c
        
    if len(max_heap) == 0 :
        continue
    
    max_heap[0][1] -= 1
    
    if max_heap[0][1] <= 0 :
        heapq.heappop(max_heap)
        
min_angry = 0
for i in max_heap :
    min_angry += i[0] * i[1] * -1

print(min_angry)