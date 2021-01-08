s = 'cacbbba'
s_list = [char for char in s]
print(s_list)
s_count=[]
check=''

for i in range(len(s_list)):
    for j in range(3,len(s_list)):
        if i == 0:
            check = s_list[i:j]
            print(check)
            if check == check[::-1]:
                print('adding')
                s_count.append(len(check))
        else:
            s_list.append(s_list[0])
            s_list.pop(0)
            print(s_list)
            check = s_list[i:j]
            print(check)
            if check == check[::-1]:
            	print('adding')
                s_count.append(len(check))
    print(s_count)
    s_count.clear()
               
                
                
            
            
        
    

    