`
@author: Fizz Cao 
@file: 215_kth_largest_element_in_an_array.py
@time: 3/10/2021 11:49 pm
`
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    return nums.sort((a, b) => a - b)[nums.length-k];
};