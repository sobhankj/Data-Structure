list_ = []
def joda_kardan(how_much , donbale) :
    number = donbale[:how_much]
    donbale = donbale[how_much:]
    return number , donbale

def dorost_kardan_adad(first , second) :
    first , second = second , str(int(first) + int(second))
    return first , second

def check(first , second , three) :
    if int(first) + int(second) == int(three) :
        return True
    else :
        False

def calculate(first , second , donbale):
    if first[0] == '0' or second[0] == '0' :
        return False
    if len(donbale) == 0 :
        return True
    else :
        three , donbale = joda_kardan(len(str(int(first) + int(second))) , donbale)
        if check(first , second , three) :
            first , second = dorost_kardan_adad(first , second)
            list_.append(three)
            if calculate(first , second , donbale) :
                return True
        else :
            return False
        return False

string = input()
temp_string = string
i = 1
flag = False
while i < len(string) and flag == False and string[0] != '0':
    j = 1
    while j < len(string) and flag == False:
        first_int , temp_string = joda_kardan(i , temp_string)
        second_int , temp_string = joda_kardan(j , temp_string)
        list_.append(first_int)
        list_.append(second_int)
        if calculate(first_int , second_int , temp_string) and len(list_) > 2:
            print("YES")
            flag = True
        else :
            j += 1
            temp_string = string
            list_.clear()
     
    i += 1
    temp_string = string
    list_.clear()

if flag == False :
    print("NO")