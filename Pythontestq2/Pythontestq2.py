#question 2
def compute_cross_product(array1, array2):
    if len(array1) !=3 and len(array2)!=3:
        result="value error"
    x=array1[1]*array2[2]-array1[2]*array2[1]
    y=array1[2]*array2[0]-array1[0]*array2[0]
    z=array1[1]*array2[1]-array1[1]*array2[0]
    return(x,y,z)



