from itertools import permutations
import string

number_of_books = int(input())
number_of_senario = int(input())

correct_senario = []
wrong_senario = []
correct_list = []
for i in range(number_of_senario) :
    wrong , correct = input().split(' ')
    correct_list.append(correct)
    correct_temp = [character for character in correct]
    wrong_temp = [character for character in wrong]
    correct_senario.append(correct_temp)
    wrong_senario.append(wrong_temp)
    
    
def generate_alphabet(n):
    alphabet_list = list(string.ascii_lowercase)[:n]
    return alphabet_list

first_n_character_alphabet = generate_alphabet(number_of_books)
all_senario = permutations(first_n_character_alphabet)
dict_all_senario = {i : -1 for i in all_senario}

def create_diffrent_senario(senario , n) :
    temp = []
    for i in range(n + 1):
        for j in range(i + 2, n + 1):
            new = list(senario)
            new[i:j] = reversed(new[i:j])
            temp.append(new)
            
    return temp
            

def BFS(number_of_book , dict_all_senario) :
    temp = []
    root = tuple(generate_alphabet(number_of_book))
    temp.append(root)
    dict_all_senario[root] = 0
    while len(temp) != 0 :
        senario = tuple(temp[0])
        temp = temp[1:]
        new_senario = create_diffrent_senario(senario , number_of_book)
        for sen in new_senario :
            if dict_all_senario[tuple(sen)] == -1 :
                dict_all_senario[tuple(sen)] = dict_all_senario[senario] + 1
                temp.append(sen)

BFS(number_of_books , dict_all_senario)

for i in range(len(wrong_senario)) :
    for j in range(len(wrong_senario[i])) :
        index = correct_list[i].index(wrong_senario[i][j])
        wrong_senario[i][j] = first_n_character_alphabet[index]

for i in wrong_senario :
    print(dict_all_senario[tuple(i)])    