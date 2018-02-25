def read_data(name):
    f = open("HackTheValley2.txt", "r")
    a=[]
    i = 0
    for line in f:
        word = line.split('\n')
        a.append(word[0])
        i += 1
    f.close()


    mass = [[]for k in range (5)]    
    for i in range (5):
       for j in range (i*4, i*4+4):
           mass[i].append(a[j])
           
    while j in range(1, 3):
        int(a[j])


    if name == mass[i][0]:
        print("Credit Card Number:" + mass[i][1])
        print("Expiration Date:" + mass[i][2])
        print("Security Code:" + mass[i][3])
    else:
        i += 1
    

 








            
    
    
