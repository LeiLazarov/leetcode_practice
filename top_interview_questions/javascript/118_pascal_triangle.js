`
@author: Fizz Cao 
@file: 118_pascal_triangle.py
@time: 12/10/2021 11:46 pm
`
/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    let ans = [];

    for (let i = 0; i < numRows; i++) {
        let tool = [];
        for (let j = 0; j < i+1; j++)
            tool.push(1);
        for (let k = 1; k < i ; k++)
            tool[k] = ans[i-1][k] + ans[i-1][k-1];
        ans.push(tool);
    }

    return ans;
};