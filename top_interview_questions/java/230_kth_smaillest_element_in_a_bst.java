/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        int ans = 0;
        LinkedList<TreeNode> stack = new LinkedList ();

        while ((root != null || stack.size() > 0) && k > 0) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            ans = stack.peek().val;
            k -= 1;
            root = stack.pop().right;
        }
        return ans;
    }
}