class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] ans = new int[nums.length];
        for (int i = 0; i < nums.length; i++)
            ans[i] = 1;

        for (int l = 1; l < nums.length; l++)
            ans[l] = ans[l-1] * nums[l-1];

        int R = 1;
        for (int r = nums.length - 2; r >= 0; r--) {
            R *= nums[r+1];
            ans[r] *= R;
        }

        return ans;
    }
}