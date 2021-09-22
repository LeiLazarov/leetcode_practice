/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    ans = [];
    for (let i = 0; i <= nums.length; i++)
        backtrack(ans, nums, [], 0, i);
    return ans
};

var backtrack = function(ans, nums, temp, start, k) {
    if (temp.length === k)
        ans.push(temp.slice());
    for (let i = start; i < nums.length; i++) {
        temp.push(nums[i]);
        backtrack(ans, nums, temp, i+1, k);
        temp.pop();
    }
}