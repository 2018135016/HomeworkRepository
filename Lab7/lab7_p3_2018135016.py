
class not2DError(Exception):
# Error for 1D list
    def __str__(self):
        return '[ERROR]: list is not 2D.'

class unevenListError(Exception):
# Error for uneven list
    def __str__(self):
        return '[ERROR]: inner lists are not same in length.'

class improperMatrixError(Exception):
# Error for incompatible matmul pair
    def __str__(self):
        return '[ERROR]: [a][b]*[c][d] not b==c.'


def mul1d(arr1,arr2):
    # arr1 * arr2
    # [1,2,3] * [4,5,6]
    # return  1*4 + 2*5 + 3*6
    sum = 0
    for i in range(len(arr1)):
        sum+=arr1[i]*arr2[i]
    return sum

class list_D2(list):
    def __init__(self,arr):
        
        ### YOUR CODE HERE ###
        dimension=0
        check=arr
        while type(check)==type([]): # type을 통해 차원 확인
            dimension+=1
            if len(check)==0:break
            check=check[0]
        if dimension!=2: # 차원이 2가 아니면 에러
            raise  not2DError()
        for i in range(len(arr)-1): # 길이가 서로 다르면 에러
            if len(arr[i])!=len(arr[i+1]):
                raise unevenListError()
        
    
        ######

        self.extend(arr)

    def __str__(self):

        ### YOUR CODE HERE ###
        
        return "list_2D: {0}*{1}".format(len(self),len(self[0]))

        ######

    def transpose(self):

        ### YOUR CODE HERE ###
        arr=[[self[j][i] for j in range(len(self))] for i in range(len(self[0]))]
        return list_D2(arr)
        
        ######


    def __matmul__(self, others):
        
        ### YOUR CODE HERE ###
        if len(self[0])!=len(others): # 곱이 불가하면 에러
            raise improperMatrixError()
        arr=[[0]*len(self) for i in range(len(others[0]))] # 결과를 저장할 arr 생성

        for i in range(len(self)): 
            for j in range(len(others[0])):
                for k in range(len(self[0])): # 행렬곱 수행
                    arr[i][j]+=self[i][k]*others[k][j]
        

        return list_D2(arr)

        ######

    def avg(self):

        ### YOUR CODE HERE ###
        
        s=sum([self[i][j] for j in range(len(self[0])) for i in range(len(self))])

        return s/(len(self)*len(self[0]))

        ######