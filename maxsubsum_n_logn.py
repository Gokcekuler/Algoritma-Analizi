import time
start= time.time()
def  max_of_two(a, b):
    if (a > b):
        return a
    else:
        return b
def max_of_three(a, b, c):
    return max_of_two(a, max_of_two(b, c))

def my_f_3(a=[4, -3, 5, -2, -1, 2, 6, -2,4, -3, 5, -2, -1, 2, 6, -2]):
    n = len(a)
    if (n == 1 ) :
            return a[0]
    left_i = 0
    left_j = n // 2
    right_i = n // 2
    right_j = n
    left_sum =my_f_3(a[left_i:left_j])
    right_sum =my_f_3(a[right_i:right_j])

    temp_left_sum = 0
    t = 0
    for i in range(left_j-1,left_i-1,-1):
        t = t + a[i] 
        if(t > temp_left_sum): 
            temp_left_sum = t
    temp_right_sum=0
    t=0
    for i in range(right_i,right_j):
        t = t + a[i]
        if(t > temp_right_sum):
            temp_right_sum = t
    center_sum = temp_left_sum + temp_right_sum
    return (max_of_three(left_sum, right_sum, center_sum))
print(my_f_3(a=[4, -3, 5, -2, -1, 2, 6, -2]))
finish=time.time()
sub=finish-start
print(sub)







     
