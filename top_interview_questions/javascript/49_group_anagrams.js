`
@author: Fizz Cao 
@file: 49_group_anagrams.py
@time: 1/10/2021 11:54 pm
`
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let m = new Map();

    for (let str of strs) {
        let count = new Array(26).fill(0);
        for (let c of str)
            count[c.charCodeAt()-97]++;
        let keyStr = count.join('#')
        m[keyStr] ? m[keyStr].push(str) : m[keyStr] = [str];
    }

    return Object.values(m);

//     let m = new Map();

//     for (let str of strs) {
//         keyStr = str.split("").sort().join("");
//         if (!m.has(keyStr))
//             m.set(keyStr, [])
//         m.set(keyStr, [...m.get(keyStr), str]);
//     }

//     return Array.from(m.values());
};