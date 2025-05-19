import copy

#initial parameter
NEIGHBORS = 'neighbors'
COLOR = 'color'
TIME = 'time'
PARENT = 'parent'
DISTANCE = 'distance'
BLACK = 3
GRAY = 2
WHITE = 1


#input number of v
number_v = int(input())


#intial for each v a dict that include neighbors , color , time and parent this inital for DFS alg.
dict_tree = {(key + 1) : {NEIGHBORS :[] , COLOR : WHITE , TIME : [] , PARENT : None , DISTANCE : 0} for key in range(number_v)}


#set neighbors for each v from input
for i in range(number_v - 1) :
    first , second = map(int , input().split(' '))
    dict_tree[first][NEIGHBORS].append(second)
    dict_tree[second][NEIGHBORS].append(first)
    
    
#DFS ALGORITHEM
time_dfs = 0
tempG_neighbors = []
def DFS(tree , root) :
    global time_dfs
    global tempG_neighbors
    tempG_neighbors.append(root)
    time_dfs = time_dfs + 1
    tree[root][TIME].append(time_dfs)
    tree[root][COLOR] = GRAY
    for neighbor in tree[root][NEIGHBORS] :
        if tree[neighbor][COLOR] == WHITE :
            temp_neighbors = copy.copy(tempG_neighbors)
            tree[neighbor][PARENT] = temp_neighbors
            tree[neighbor][DISTANCE] = tree[root][DISTANCE] + 1
            DFS(tree , neighbor)
    tempG_neighbors.pop()
    tree[root][COLOR] = BLACK
    time_dfs = time_dfs + 1
    tree[root][TIME].append(time_dfs)
    
DFS(dict_tree , 1)

#input possition of the beaches
list_pos_sea = input().split(' ')

def Cfind_first_parent(tree , first , second) :
    first , second = int(first) , int(second)
    if len(tree[first][PARENT]) < len(tree[second][PARENT]) :
        for i in range(len(tree[first][PARENT]) - 1 , -1 , -1) :
            if tree[first][PARENT][i] in tree[second][PARENT] :
                return tree[first][PARENT][i]
    else :
        for i in range(len(tree[second][PARENT]) - 1 , -1 , -1) :
            if tree[second][PARENT][i] in tree[first][PARENT] :
                return tree[second][PARENT][i]
      
parents = []
def find_first_parent(tree , list_pos) :
    global parents
    for i in range(len(list_pos) - 1) :
        parent = Cfind_first_parent(tree , list_pos[i] , list_pos[i + 1])
        parents.append(parent)
    
find_first_parent(dict_tree , list_pos_sea)

def find_way1(list , end) :
    index_end = list.index(end)
    templist = list[len(list) - 1 : index_end : -1]
    return templist

def find_way2(list , start) :
    index_start = list.index(start)
    templist = list[index_start :]
    return templist

def sovle_the_problem(tree , list_beaches , list_parent) :
    ways = []
    prev_par = 1
    counter = 0
    list_parent.append(1)
    temp_beach = 1
    for i in range(len(list_beaches)) :
        # ways.extend(tree[int(list_beaches[i])][PARENT])
        temp_ways = find_way2(tree[int(list_beaches[i])][PARENT] , prev_par)
        ways.extend(temp_ways)
        # print("@@@" , ways)
        ways.append(int(list_beaches[i]))
        # print('!!!' , ways)
        temp_ways = find_way1(tree[int(list_beaches[i])][PARENT] , list_parent[i])
        ways.extend(temp_ways)
        # print("&&&" , ways)
        temp_counter = tree[int(list_beaches[i])][DISTANCE] - tree[temp_beach][DISTANCE]
        counter += temp_counter
        temp_beach = list_parent[i]
        temp_counter = tree[int(list_beaches[i])][DISTANCE] - tree[temp_beach][DISTANCE]
        counter += temp_counter
        prev_par = list_parent[i]
        
    return counter , ways

cnt , solve_ways = sovle_the_problem(dict_tree , list_pos_sea , parents)

if cnt <= 2 * number_v - 2 :
    for i in solve_ways :
        print(i , end=' ')
else :
    print(-1)

# print('\n' , parents , sep='')
# for i in range(len(dict_tree)) :
#     print(i+1 , dict_tree[i+ 1])

# print('$$$' , cnt)
# print(solve_ways)