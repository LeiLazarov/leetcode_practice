`
@author: Fizz Cao 
@file: 242_valid_anagram.py
@time: 7/10/2021 10:29 pm
`
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    s = s.split("").sort().join("");
    t = t.split("").sort().join("");
    return s === t;
};