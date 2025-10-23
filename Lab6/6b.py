for i in range(65, 91):           
    filename = chr(i) + ".txt"    
    f = open(filename, "w")       
    f.write("file name: " + filename)
    f.close()                    
    print(filename, "created")
