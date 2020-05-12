'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def solution(array, commands):
    answer = []
    for i,j,k in commands:
        temp = array[i-1:j]
        temp.sort()
        print(temp)
        answer.append(temp[k-1])
    return answer
    
result = solution([5,1,2,3,5,6,87,11,235,24], [[1,3,2], [2,5,3]]) 

print("-result-")
print(result)
