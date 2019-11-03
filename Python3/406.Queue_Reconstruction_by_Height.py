class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sorted_heights = sorted(people)
        res = [None for _ in range(len(people))]
        for person in sorted_heights:
            ahead_pos = person[1]
            count = 0
            for i in range(len(res)):
                if (count == ahead_pos and res[i] == None):
                    res[i] = person
                    break
                if (res[i] == None or res[i][0] >= person[0]):
                    count += 1
        return res

# simpler solution but same time complexity


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sorted_people = sorted(people, key=lambda x: (-x[0], x[1]))
        res = []
        for person in sorted_people:
            res.insert(person[1], person)
        return res
