/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var map = new Map();

    for (var i = 0; i < nums.length; i++) {
        if (map.has(target - nums[i]))
            return [map.get(target - nums[i]), i];
        if (!map.has(nums[i]))
            map.set(nums[i], i);
    }
};