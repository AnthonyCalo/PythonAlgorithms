'''
You are given a string num, representing a large integer, and an integer k.

We call some integer wonderful if it is a permutation of the digits in num and is greater in value than num. There can be many wonderful integers. However, we only care about the smallest-valued ones.

    For example, when num = "5489355142":
        The 1st smallest wonderful integer is "5489355214".
        The 2nd smallest wonderful integer is "5489355241".
        The 3rd smallest wonderful integer is "5489355412".
        The 4th smallest wonderful integer is "5489355421".

Return the minimum number of adjacent digit swaps that needs to be applied to num to reach the kth smallest wonderful integer.

The tests are generated in such a way that kth smallest wonderful integer exists.

'''
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def next_perm(num):
            num = list(num)
            n = len(num) -1
            while(n> 0 and ord(num[n - 1]) >= ord(num[n])):
                n-=1
            if(n<=0):
                return False
            j = len(num) - 1
            while (ord(num[j]) <= ord(num[n - 1])):
                j -= 1
            num[j], num[n-1] = num[n -1], num[j]
            j = len(num) - 1
            while n < j:
                num[j], num[n] = num[n], num[j]
                j-=1
                n+=1
            return (num)
            
        orig = list(num)
        res = list(num)

        for i in range(k):
            orig= next_perm(orig)

        sc = 0
        for i in range(len(res)):
            if(res[i] != orig[i]):
                start = i+1
                while (res[i] != orig[start]):
                    start += 1
                while i != start:
                    orig[start], orig[start -1] = orig[start -1 ], orig[start]
                    start -= 1
                    sc +=1
        return sc