class Solution {
    public int majorityElement(int[] nums) {
        int candi = nums[0];
        int count = 1;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == candi)
                count += 1;
            else
                count -= 1;
            if (count == 0) {
                candi = nums[i];
                count = 1;
            }
        }

        return candi;
    }
}