/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    let ans = [];
    backtrack(ans, n, "", 0, 0);
    return ans;

};

var backtrack = function(ans, n, temp, left, right) {
    if (left === n && right === n)
        ans.push(temp);
    if (left < n)
        backtrack(ans, n, temp+"(", left+1, right);
    if (right < left)
        backtrack(ans, n, temp+")", left, right+1);
}