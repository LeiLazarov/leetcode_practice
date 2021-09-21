class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] ans = new int[2];
        Map<Integer, Integer> toolMap = new HashMap ();
        for (int i = 0; i < nums.length; i++) {
            if (toolMap.containsKey(target - nums[i])) {
                ans[0] = toolMap.get(target - nums[i]);
                ans[1] = i;
                break;
            }
            toolMap.put(nums[i], i);
        }
        return ans;
    }
}