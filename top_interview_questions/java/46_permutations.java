class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List ans = new ArrayList<ArrayList<Integer>> ();
        boolean[] visited = new boolean[nums.length];
        backtrack(ans, nums, new LinkedList(), visited);
        return ans;
    }

    public void backtrack(List<List<Integer>> ans, int[] nums, LinkedList<Integer> temp,  boolean[] visited) {
        if (temp.size() == nums.length) {
            ans.add(new ArrayList(temp));
        }
        for (int i = 0; i < nums.length; i++) {
            if (!visited[i]) {
                temp.addLast(nums[i]);
                visited[i] = true;
                backtrack(ans, nums, temp, visited);
                temp.removeLast();
                visited[i] = false;
            }
        }
    }
}