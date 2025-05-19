dictionary_code = {}
list_code = []
stack = []
n = int(input())
flag = False

for i in range(n) :
    check = int(input())
    if check > n or check < 0 :
        flag = True
    else :
        list_code.append(check)

for i in range(len(list_code)):
    if dictionary_code.get(list_code[i]) == None :
        dictionary_code[list_code[i]] = [i , None]
    else :
        continue
    
for i in range(len(list_code)-1 , -1 , -1) :
    if dictionary_code[list_code[i]][1] == None :
        dictionary_code[list_code[i]][1] = i
    else :
        continue
   
awnser = 0
count = 0
for i in range(len(list_code)) :
    
    if list_code[i] == 0 :
        if len(stack) == 0 :
            count = 0
            continue
        else :
            awnser = -1
            break      
    if i == dictionary_code[list_code[i]][0] and i != dictionary_code[list_code[i]][1] :
        stack.append(list_code[i])
        count += 1
        if count >= awnser :
            awnser = count
    elif i != dictionary_code[list_code[i]][0] and i == dictionary_code[list_code[i]][1] :
        if stack[len(stack)-1] == list_code[i] :
            stack.pop()
            count -= 1
        else :
            awnser = -1
            break
    elif i == dictionary_code[list_code[i]][0] and i == dictionary_code[list_code[i]][1] :
        count += 1
        if count >= awnser :
            awnser = count
        count -= 1
    elif i != dictionary_code[list_code[i]][0] and i != dictionary_code[list_code[i]][1] :
        pass
        
if flag == True :
    print(-1)        
else :
    print(awnser)
    
    
# class Stack :
#     def __init__(self, size = 10) -> None:
#         self.stack = [None] * size
#         self.ptrindex = 0
#         self.capacity = size
    
#     def isEmpty(self) :
#         if self.ptrindex == 0 :
#             return True
#         else :
#             return False
    
#     def push(self, value) :
#         if self.ptrindex == self.capacity :
#             return None
#         self.stack[self.ptrindex] = value
#         self.ptrindex += 1
    
#     def pop(self) :
#         if self.ptrindex == 0 :
#             return None
#         pop_value = self.stack[self.ptrindex - 1]
#         self.stack[self.ptrindex - 1] = None
#         self.ptrindex -= 1
#         return pop_value
    
#     def peek(self) :
#         return self.stack[self.ptrindex - 1]
    
#     def getInOneLine(self) :
#         l = []
#         for o in range(self.ptrindex) :
#             l.append(self.stack[o])
#         return " ".join(str(l))
    
# stack = Stack()
# dictionary_code = {}
# n = int(input())
# flag = True
# flag_c = False
# count = 0
# for i in range(n) :
#     if flag == False:
#         continue
#     code_color = int(input())
#     if code_color == 0 :
#         while stack.isEmpty() == False :
#             stack.pop()
#         print(stack.getInOneLine() , count)
#         continue
#     if stack.isEmpty() and flag_c == False:
#         stack.push(code_color)
#         if code_color != 0 :
#             flag_c = True
#             count += 1
#         dictionary_code[code_color] = True
#     else :
#         if dictionary_code.get(code_color) == None :
#             stack.push(code_color)
#             dictionary_code[code_color] = True
#         else :
#             if stack.peek() == code_color :
#                 print(stack.getInOneLine() , count)
#                 continue
#             else :
#                 if dictionary_code[code_color] == False :
#                     if stack.isEmpty():
#                         flag = False
#                         count = -1
#                         break
#                     while stack.isEmpty() == False :
#                         stack.pop()
#                     stack.push(code_color)
#                     print(stack.getInOneLine() , count , "##############")
#                     continue
#                 while stack.peek() != code_color :
#                     if stack.isEmpty():
#                         flag = False
#                         count = -1
#                         break
#                     stack.pop()
#                 else :
#                     dictionary_code[code_color] = False
#                     count += 1
    
#     print(stack.getInOneLine() , count)
                
# print(count)