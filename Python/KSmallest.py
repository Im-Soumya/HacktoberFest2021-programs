'''You have been given two sorted lists of size M and N. It is desired to find the Kth
smallest element out of M+N elements of both lists. Propose and implement an efficient
algorithm to accomplish the task. Further, propose and implement an efficient algorithm
to accomplish the task considering that elements in both lists are unsorted.'''

# Sorted Array
def KSmallestSorted(A, B, m, n, k_req):
    i, j, k = 0, 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            k += 1
            if k == k_req:
                return A[i]
            i += 1
        else:
            k += 1
            if k == k_req:
                return B[j] 
            j += 1

    while i < len(A):
        k += 1
        if k == k_req:
                return A[i]
        i += 1

    while j < len(B):
        k += 1
        if k == k_req:
            
            return B[j]
        j += 1
if __name__=='__main__':
    A = [2, 3, 6, 7, 9]
    B = [1, 4, 8, 10]
    k = 5;
    kthsmallest=KSmallestSorted(A, B, 5, 4, k)
    print(f"Kth(K={k}) smallest element in both arrays is {kthsmallest}",) 

# Unsorted Array

def kthSmallestunsorted(arr1,arr2,K):
    merge_arr=arr1+arr2
    N = len(merge_arr)
    return select(merge_arr, 0, N - 1, K)
    
def select(arr, l, r, K):

    if (K > 0 and K <= r - l + 1):

        pos = partition(arr, l, r)

        if (pos - l == K - 1):
            return arr[pos]
        if (pos - l > K - 1): 
            return select(arr, l, pos - 1, K)
        else:
            return select(arr, pos + 1, r,K - pos + l - 1)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
 
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1
if __name__ == "__main__":

    arr1 = [12, 3, 5, 7, 4, 19, 26]
    arr2=[47,9,2,34,8,10]
    K = 8
    kthsmallest=kthSmallestunsorted(arr1,arr2,K)
    print(f"Kth(K={K}) smallest element in both arrays is {kthsmallest}",) 

