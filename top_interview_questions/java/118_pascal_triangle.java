class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans = new ArrayList<> ();

        for (int i = 0; i < numRows; i++) {
            List<Integer> tool = new ArrayList<> ();
            for (int j = 0; j < i+1; j++)
                tool.add(1);
            for (int k = 1; k < i ; k++)
                tool.set(k, ans.get(i-1).get(k) + ans.get(i-1).get(k-1));
            ans.add(tool);
        }

        return ans;
    }
}