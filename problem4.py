
def find_largest_number():
    data = [50, 2, 1, 9]    
    temp = ''
    temp2 = 0

    temp_list = []
    temp_list2 = []

    for i in data:        
        temp_list = list(data)
        temp_list.remove(i)
        for j in temp_list:            
            temp_list2 = list(temp_list)
            temp_list2.remove(j)
           
            a = temp_list2[0]
            b = temp_list2[1]
            temp = str(i) + str(j) +str(a) + str(b)
            if int(temp) > temp2:
                temp2 = int(temp)
            temp = str(i) + str(j) +str(b) + str(a)
            if int(temp) > temp2:
                temp2 = int(temp)
    
    print(temp2) 

def find_largest(data):  
    number = 0  
    temp2 = ''  
    
    temp_list = list(data)
    for m in range(len(data)): 
        if m > 0:
            tt = data[0]
            data[0] = data[m]
            data[m] = tt
        for n in range(len(data)):            
            temp_list = list(data)                      
            if temp_list[m] != temp_list[n]:
                temp_main = temp_list[m]
                temp_list[m] = temp_list[n]
                temp_list[n]= temp_main
                print(temp_list)
            elif temp_list[m] == temp_list[n]:
                print(temp_list)

    return
    for i in range(len(data) - 1):  
        if i > 0:
            temp_number = data[i]
            data[i] = data[i + 1]
            data[i + 1] = temp_number

        temp_list = list(data)
        temp_list2 = list(temp_list)
        for j in range(len(temp_list2)):            
            temp = temp_list2[0]
            temp_list2.remove(temp)
            temp_list2.append(temp)
            temp2 = ''.join(str(x) for x in temp_list2)
            print(temp2)
            if int(temp2) > number:
                number = int(temp2)

    print(number) 

def swap(data, x, y):
    temp = data[x]
    data[x] = data[y]
    data[y] = temp    
    

def back_tracking(data, x, y):
    if x == y:
        print(data)
    for i in range(x):
        swap(data, x, i)
        back_tracking(data, i, y + 1)
        swap(data, x, i)

    


if __name__ == "__main__":
    '''for a in range(4):
        for b in range(4):
            print(str(a) + str(b))'''
    
    #find_largest_number()
    data = [50, 2, 1, 9]   
    #find_largest(data) 
    back_tracking(data, 4, 0)
