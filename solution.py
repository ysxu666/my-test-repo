class Solution:
    def maxFrequencyScore(self, nums, k):
        # 对数组进行排序
        nums.sort()
        
        # 初始化答案和窗口左边界
        ans = 0
        left = 0
        
        # 计算窗口内元素的总和
        window_sum = 0
        
        # 遍历数组，right 为窗口右边界
        for right in range(len(nums)):
            window_sum += nums[right]
            
            # 当窗口大小大于 k 时，移动左边界
            while right - left + 1 > k:
                window_sum -= nums[left]
                left += 1
            
            # 当窗口大小等于 k 时，计算答案
            if right - left + 1 == k:
                # 计算窗口内元素的平均值，并更新答案
                ans = max(ans, window_sum // k)
        
        return ans

# 示例使用
solution = Solution()
nums = [1, 2, 3, 4]
k = 2
print(solution.maxFrequencyScore(nums, k))  # 输出应为 4