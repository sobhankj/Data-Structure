#inital goups
groupA = []
groupB = []

#input number of v and e
number_v , number_e = map(int , input().split(' '))

#inital for each v a list that show its group is selected or not and name of the group 1 for groupA and 2 for groupB
dict_student = {(key + 1): [False , 0] for key in range(number_v)}

#create function to reduse repeat code
def updating_groupX(student , group , name_group) :
    group.append(student)
    dict_student[student][0] = True
    dict_student[student][1] = name_group
    
#solve the problem
for i in range(number_e) :
    first , second = map(int , input().split(' '))
    if dict_student[first][0] == False and dict_student[second][0] == False :
        updating_groupX(first , groupA , 1)
        updating_groupX(second , groupB , 2)
        
    elif dict_student[first][0] == False and dict_student[second][0] == True :
        if dict_student[second][1] == 1 :
            updating_groupX(first , groupB , 2)
        else :
            updating_groupX(first , groupA , 1)
            
    elif dict_student[first][0] == True and dict_student[second][0] == False :
        if dict_student[first][1] == 1 :
            updating_groupX(second , groupB , 2)
        else :
            updating_groupX(second , groupA , 1)
            
    else : #both dict student frirst and second is true
        pass
    
#print the result
print(len(groupA))
for student in groupA :
    print(student , end = ' ')