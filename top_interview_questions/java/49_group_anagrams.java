class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap ();

        for (String str: strs) {
            char[] count = new char [26];
            for (char c: str.toCharArray())
                count[c - 'a'] += 1;
            String keyStr = String.valueOf(count);
            if (!map.containsKey(keyStr))
                map.put(keyStr, new ArrayList<>());
            map.get(keyStr).add(str);
        }

        return new ArrayList<> (map.values());

//         Map<String, List<String>> map = new HashMap ();

//         for (String str: strs) {
//             char[] ca = str.toCharArray();
//             Arrays.sort(ca);
//             String keyStr = String.valueOf(ca);
//             if (!map.containsKey(keyStr))
//                 map.put(keyStr, new ArrayList<>());
//             map.get(keyStr).add(str);
//         }

//         return new ArrayList<> (map.values());
    }
}