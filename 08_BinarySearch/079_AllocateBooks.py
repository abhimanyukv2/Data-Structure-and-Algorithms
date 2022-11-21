'''Given an array arr of integer numbers. Where arr[i] represent the
number of pages in the i-th book. There are m number of student
and the task is to allocate all the book to their students.
Allocate books in such a way that:
1. Each student gets at least one book.
2. Each book should be allocate to a student.
3. Book allocation should be in a contiguous manner.
You have to allocate the book to m students such that the maximum
number of pages assigned to a student is miniumm.'''

def allocateBooks(arr, numberOfBooks, numberOfStudents):
    totalNumberOfPages = sum(arr)
    start = 0  
    end = totalNumberOfPages
    ans = -1
    while start <= end:
        mid = start + (end - start)//2
        
        if isPossible(arr, numberOfBooks, numberOfStudents, mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans

def isPossible(arr, numberOfBooks, numberOfStudents, mid):
    studentCount = 1
    pageSum = 0

    for i in range(numberOfBooks):
        if pageSum + arr[i] <= mid:
            pageSum += arr[i]
        else:
            studentCount += 1
            if studentCount > numberOfStudents or arr[i] > mid:
                return False

            pageSum = arr[i]
    return True

if __name__ == "__main__":
    testCase = int(input())
    for _ in range(testCase):
        numberOfBooks = int(input())
        numberOfStudents = int(input())
        arr = list(map(int,input().split()))

        ans = allocateBooks(arr, numberOfBooks, numberOfStudents)
        print(ans)