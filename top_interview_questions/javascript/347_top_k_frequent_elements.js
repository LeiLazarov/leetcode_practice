`
@author: Fizz Cao 
@file: 347_top_k_frequent_elements.py
@time: 30/09/2021 11:27 pm
`
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    if (k == nums.length)
        return nums;

    // 1. build hash map : character and how often it appears
    let count = {};
    nums.forEach(num => count[num] ? count[num] += 1 : count[num] = 1);

    // 2. keep k top frequent elements in the heap
    let heap = new PriorityQueue ();
    for (let key in count) {
        heap.enqueue(key, count[key]);
    }

    // 3. build an output array
    let ans = []
    for (let i = 0; i < k; i++)
        ans.push(heap.dequeue());

    return ans;
};


class PriorityQueue {
    constructor(){
        this._values = [];
    }

    enqueue(val, priority){
        this._values.push(new Node(val, priority));
        this._traverseUp();
    }

    dequeue(){
        const max = this._values[0];
        const end = this._values.pop();
        if(this._values.length > 0){
            this._values[0] = end;
            this._traverseDown();
        }
        return max.val;

    }

    _traverseUp(){
        let idx = this._values.length - 1;
        const el = this._values[idx];
        while(idx > 0){
            let pIdx = Math.floor((idx - 1) / 2);
            let parent = this._values[pIdx];
            if(el.priority <= parent.priority) break;
            this._values[pIdx] = el;
            this._values[idx] = parent;
            idx = pIdx;
        }
    }

    _traverseDown(){
        let leftChildIdx = null;
        let rightChildIdx = null;
        let leftChild = null;
        let rightChild = null;
        let swapIdx = null;

        let idx = 0;
        const el = this._values[idx];
        while(true){
            swapIdx = null;
            leftChildIdx = 2 * idx + 1;
            rightChildIdx = 2 * idx + 2;

            if(leftChildIdx < this._values.length){
                leftChild = this._values[leftChildIdx];
                if(leftChild.priority > el.priority){
                    swapIdx = leftChildIdx;
                }
            }

            if(rightChildIdx < this._values.length){
                rightChild = this._values[rightChildIdx];
                if(
                    (swapIdx === null && rightChild.priority > el.priority) ||
                    (swapIdx !==null && rightChild.priority > leftChild.priority)
                ) {
                    swapIdx = rightChildIdx;
                }
            }

            if(swapIdx === null) break;
            this._values[idx] = this._values[swapIdx];
            this._values[swapIdx] = el;
            idx = swapIdx
        }
    }
}


class Node {
    constructor(val, priority){
        this.val = val;
        this.priority = priority;
    }
}

