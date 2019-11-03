class Solution {
    public int[][] reconstructQueue(int[][] people) {
        int[][] sortedPeople = people;
        Arrays.sort(sortedPeople, new Comparator<int[]>() {
            @Override
            public int compare(int[] a, int[] b) {
                return a[0] != b[0] ? b[0] - a[0] : a[1] - b[1];
            }
        });
        List<int[]> res = new LinkedList<>();
        for (int[] person : sortedPeople) {
            res.add(person[1], person);
        }
        return res.toArray(new int[people.length][]);
    }
}