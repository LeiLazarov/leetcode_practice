/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    const ans = new Array();
    const visited = new Array(nums.length).fill(0);
    backtrack(ans, nums, [], visited);
    return ans;

};

function backtrack(ans, nums, temp, visited) {
    if (temp.length === nums.length) {
        ans.push([...temp]);
        return;
    }
    for (let i = 0; i < nums.length; i++) {
        if (!visited[i]) {
            temp.push(nums[i]);
            visited[i] = 1;
            backtrack(ans, nums, temp, visited);
            temp.pop();
            visited[i] = 0;
        }
    }
}