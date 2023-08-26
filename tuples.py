filenames = ['1.myfile.txt','2.myfile.txt','3.myfile.txt']

for filename in filenames:
    filename = filename.replace('.','#',1)
    ##replace method will give a new string and not edit the actual one, same like str.title()
    ## We can also use the function filename.rename()
print(filenames)

tuples_vals = (1,2,3)

##tuples_vals[2] = 4;## gives error here as th tuples are not mutable
print(tuples_vals)