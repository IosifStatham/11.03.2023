def union_and_create_new (command): 
    rez = 0
    rez1 = 0
    line_file_1 =''
    line_file_2 =''
    line_file_3 =''
    
    with open ('data/1.txt', 'rt', encoding= 'utf-8') as file:
        for line in file:
            rez += 1
    
    with open ('data/1.txt', 'rt', encoding= 'utf-8') as file:
        line = file.readlines()
        line_file = ''.join(line)
        line_file_1 = line_file
    
    with open ('data/2.txt', 'rt', encoding= 'utf-8') as file:
        for line in file:
            rez1 += 1  
            
    with open ('data/2.txt', 'rt', encoding= 'utf-8') as file:
        line = file.readlines()
        line_file = ' '.join(line)
        line_file_2 = line_file
        
    print(rez)    
    print(line_file_1) 
    print(rez1)    
    print(line_file_2)
        
    with open ('data/3.txt', 'w',encoding= 'utf-8') as file:
        if rez > rez1:
          file.write(" 2.txt \n")
          file.write(str(rez1))
          file.write("\n")
          file.write(line_file_2)  
          file.write("\n1.txt \n")
          file.write(str(rez))
          file.write("\n")
          file.write(line_file_1)
          

        else:
          file.write(" 1.txt\n")
          file.write(str(rez))
          file.write("\n")
          file.write(line_file_1)  
          file.write("\n2.txt \n")
          file.write(str(rez1))
          file.write("\n")
          file.write(line_file_2)
          
    
    with open ('data/3.txt', 'rt', encoding= 'utf-8') as file:
        line = file.readlines()
        line_file = ' '.join(line)
        line_file_3 = line_file
        return (line_file_3)
     
     
print(union_and_create_new (1))