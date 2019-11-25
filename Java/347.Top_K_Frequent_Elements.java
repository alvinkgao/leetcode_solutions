import java.util.HashMap;
import java.util.PriorityQueue;

class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> freq_map = new HashMap<>();
        for (int num: nums) {
            if (freq_map.containsKey(num)) {
                freq_map.put(num, freq_map.get(num) + 1);
            } else {
                freq_map.put(num, 1);
            }
        }

        PriorityQueue<Integer> heap = new PriorityQueue<>((a,b) -> freq_map.get(a) - freq_map.get(b));
        int counter = 0;
        for (int num : freq_map.keySet()) {
            if (counter < k) {
                heap.add(num);
                counter++;
            } else {
                int smallest_in_heap = heap.peek();
                if (freq_map.get(num) > freq_map.get(smallest_in_heap)) {
                    heap.poll();
                    heap.add(num);
                }
            }
        }
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < heap.size();) {
            ans.add(heap.poll());
        }

        return ans;
    }
}