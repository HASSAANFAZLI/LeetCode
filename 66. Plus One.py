class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        string = ""

        for i in range(len(digits)):
            string += str(digits[i])

        string = int(string)

        string +=1

        result = [int(digit) for digit in str(string)]

        return result
