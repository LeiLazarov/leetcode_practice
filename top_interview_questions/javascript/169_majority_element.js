`
@author: Fizz Cao 
@file: 169_majority_element.py
@time: 2/10/2021 8:32 pm
`
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let candi = nums[0];
    let count = 1;

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === candi)
            count += 1;
        else
            count -= 1;
        if (count == 0) {
            candi = nums[i];
            count = 1;
        }
    }

    return candi;
};