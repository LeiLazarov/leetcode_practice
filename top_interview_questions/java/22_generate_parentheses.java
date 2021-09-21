class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ans = new ArrayList ();
        backtrack(ans, n, "", 0, 0);
        return ans;
    }

    public void backtrack(List<String> ans, int n, String temp, int left, int right) {
        if (left == n && right == n)
            ans.add(temp);
        if (left < n)
            backtrack(ans, n, temp + "(", left+1, right);
        if (right < left)
            backtrack(ans, n, temp + ")", left, right+1);
    }

//     public List<String> generateParenthesis(int n) {
//         List<String> ans = new ArrayList ();
//         backtrack(ans, n, new StringBuilder(), 0, 0);
//         return ans;
//     }

//     public void backtrack(List<String> ans, int n, StringBuilder temp, int left, int right) {
//         if (temp.length() == 2*n) {
//             ans.add(temp.toString());
//         }
//         if (left < n) {
//             temp.append("(");
//             backtrack(ans, n, temp, left+1, right);
//             temp.deleteCharAt(temp.length()-1);
//         }
//         if (right < left) {
//             temp.append(")");
//             backtrack(ans, n, temp, left, right+1);
//             temp.deleteCharAt(temp.length()-1);
//         }
//     }
}