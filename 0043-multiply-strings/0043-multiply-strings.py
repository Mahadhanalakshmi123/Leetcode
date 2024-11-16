class Solution(object):
    def multiply(self, num1, num2):
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                product = int(num1[i]) * int(num2[j])
                temp_sum = product + result[i + j + 1]
                result[i + j + 1] = temp_sum % 10
                result[i + j] += temp_sum // 10
        
        while result[0] == 0 and len(result) > 1:
            result.pop(0)
        
        return ''.join(map(str, result))
