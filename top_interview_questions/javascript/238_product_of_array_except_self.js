`
@author: Fizz Cao 
@file: 238_product_of_array_except_self.py
@time: 30/09/2021 11:26 pm
`
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let ans = [1];

    for (let l = 1; l < nums.length; l++)
        ans.push(ans[l-1] * nums[l-1]);

    let R = 1;
    for (let r = nums.length - 2; r >= 0; r--) {
        R *= nums[r+1];
        ans[r] *= R;
    }

    return ans;
};