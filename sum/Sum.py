#coding=utf-8
from collections import Counter
class TwoSum(object):
    # Given an array of integers,
    # return indices of the two numbers such that they add up to a specific target.
    def two_sum(self, nums, target):
        dict1 = {}
        for i in range(len(nums)):
            if(target - nums[i]) in dict1:
                return [dict1[target-nums[i]], i]
            dict1[nums[i]] = i
        return [-1, -1]


class ThreeSum(object):
    # Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
    # Find all unique triplets in the array which gives the sum of zero.
    def three_sum(self,nums):
        """
              :type nums: List[int]
              :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        result = []
        for i in range(length-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            lf = i+1
            rf =length-1
            sum =0-nums[i]
            while lf <rf:
                if nums[lf] + nums[rf] == sum:
                    result.append([nums[i], nums[lf], nums[rf]])
                    while lf < rf and nums[lf] == nums[lf + 1]:
                        lf += 1
                    while lf < rf and nums[rf] == nums[rf - 1]:
                        rf -= 1
                    lf += 1
                    rf -= 1
                elif nums[lf] + nums[rf] < sum:
                    lf += 1
                else:
                    rf -= 1
        return result


class FourSum(object):
    # Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
    # Find all unique quadruplets in the array which gives the sum of target.
    def four_sum(self,nums, target):
        nums.sort()
        result = []
        length = len(nums)
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                sum = target - nums[i] - nums[j]
                left = j + 1
                right = length - 1
                while left < right:
                    if nums[left] + nums[right] == sum:
                        tmp = [nums[i], nums[j], nums[left], nums[right]]
                        result.append(tmp)
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif (nums[left] + nums[right]) < sum:
                        left += 1
                    else:
                        right -= 1
        return result

class FourSum1(object):
    # Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l)
    # there are such that A[i] + B[j] + C[k] + D[l] is zero.
    def four_sum_count(self,A,B,C,D):
        AB = Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)
if __name__ == '__main__':
    ts = TwoSum()
    nums1 = [2, 7, 11, 15]
    result1 = ts.two_sum(nums1, 9)
    for result in result1:
        print(str(result) + "\t")

    nums2=[1, 0, -1, 0, -2, 2]
    ts1 = FourSum()
    result2 = ts1.four_sum(nums2,0)
    for result in result2:
        for tmp in result:
            print(str(tmp) + "\t")
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    fs=FourSum1()
    result2 = fs.four_sum_count(A,B,C,D)
    print(str(result2))