class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        if (k == nums.length)
            return nums;

        // 1. build hash map : character and how often it appears
        HashMap<Integer, Integer> count = new HashMap ();
        for (int num: nums)
            count.put(num, count.getOrDefault(num, 0) + 1);

        int[] unique = new int[count.size()];
        int i = 0;
        for (int num: count.keySet()) {
            unique[i] = num;
            i++;
        }

        // 2. keep k top frequent elements in the heap
        Queue<Integer> heap = new PriorityQueue ((n1, n2) -> count.get(n1) - count.get(n2));
        for (int num: unique) {
            heap.add(num);
            if (heap.size() > k)
                heap.poll();
        }

        // 3. build an output array
        int[] top = new int [k];
        for (int j = k - 1; j >= 0; j--)
            top[j] = heap.poll();
        return top;
    }
}