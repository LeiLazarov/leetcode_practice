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
 * @return {number[]}
 */
var inorderTraversal = function(root) {
    let ans = [];
    inorder(ans, root);
    return ans;
};

var inorder = function(ans, root) {
        if (!root) return;
        inorder(ans, root.left);
        ans.push(root.val);
        inorder(ans, root.right);
};

var iteratingInorderTraversal = function(root) {
    let ans = [];
    let stack = [];

    while (root || stack.length) {
        while(root) {
            stack.push(root);
            root = root.left;
        }
        root = stack.pop();
        ans.push(root.val);
        root = root.right;
    }

    return ans;
};