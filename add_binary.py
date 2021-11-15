class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def getBinVal(binary_number):
            converted=0
            for i in range(len(binary_number)):
                current=len(binary_number)-i-1
                binary_integer=int(binary_number[current])
                converted+=2**i*binary_integer
            return(converted)
        normal_sum=getBinVal(a)+getBinVal(b)
        return (bin(normal_sum)[2:])