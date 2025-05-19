maping_letters_as_0to9 = {'a' : 0 , 'b' : 1 , 'c' : 2 , 'd' : 3 , 'e' : 4 , 'f' : 5 , 'g' : 6 , 'h' : 7 , 'i' : 8 , 'j' : 9}
all_states = {(bin(i)[2:]).zfill(10) : 0 for i in range(1024)}

str = input()
now_state = '0000000000'
awnser = 0

def flip_or_unfilp(state , index_to_flip) :
    if state[index_to_flip] == '1' :
        return state[:index_to_flip] + '0' + state[index_to_flip + 1 :]
    elif state[index_to_flip] == '0' :
        return state[:index_to_flip] + '1' + state[index_to_flip + 1 :]

def check_valid(state) :
    global awnser 
    if state.count('1') <= 1 :
        awnser += all_states[state]
        # print(awnser , all_states[state])
        

def calculate_interesting_letter(state) :
    global awnser
    if state.count('1') <= 1 :
        awnser += 1
        # print(awnser)
    for letter_i in range(10) :
        temp = state
        temp = flip_or_unfilp(state , letter_i)
        # print(temp)
        # check_valid(temp)
        awnser += all_states[temp]



for letter in str :
    index_letter = maping_letters_as_0to9[letter]
    now_state = flip_or_unfilp(now_state , index_letter)
    # print('now_state' , now_state)
    calculate_interesting_letter(now_state)
    awnser += all_states[now_state]
    all_states[now_state] += 1
    
print(awnser)