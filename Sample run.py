metres = int(input("Enter starting meters:"))
finalmetre = int(input("Enter ending metres:"))
stepvalue = int(input("Enter step value:"))
print ()
 
print ("    Metres     Yards      Feet      Inches")
print ("-------------------------------------------")
for i in range(metres, finalmetre, stepvalue):
     
    print ("{:>10.3f} {:>10.3f} {:>10.3f} {:>10.3f}".format(i, i*1.094, i*3.28, i*39.37))

     
