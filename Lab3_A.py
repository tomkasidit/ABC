print("Lab 3(A)")
print("student ID 62055001")
print("student ID 62055003")
def knapSack(W , wt , val , n):
    if n == 0 or W == 0 : 
        return 0
    if (wt[n-1] > W): 
        return (knapSack(W , wt , val , n-1)) 
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1), knapSack(W , wt , val , n-1))        

print("-----------------------------")

val = [2, 5, 10, 5] 
wt = [20, 30, 10, 50] 
W = 10
n = len(val) 
print (knapSack(W , wt , val , n))                    
print (knapSack(W , wt , val , n-1))