class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList ();
        for (int i = 0; i <= nums.length; i++)
            backtrack(ans, nums, new ArrayList<Integer> (), 0, i);
        return ans;
    }

    public void backtrack(List<List<Integer>> ans, int[] nums, ArrayList<Integer> temp, int start, int k) {
        if (temp.size() == k)
            ans.add(new ArrayList(temp));
        for (int i = start; i < nums.length; i++) {
            temp.add(nums[i]);
            backtrack(ans, nums, temp, i+1, k);
            temp.remove(temp.size()-1);
        }
    }
}