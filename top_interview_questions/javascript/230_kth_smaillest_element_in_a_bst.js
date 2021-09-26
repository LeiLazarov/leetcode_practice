/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(root, k) {
    let ans = 0;
    const stack = [];
    while ((root || stack.length) && k) {
        while (root) {
            stack.push(root);
            root = root.left;
        }
        ans = stack[stack.length-1].val;
        k -= 1
        root = stack.pop().right;
    }
    return ans;
};