class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        table = {}
        for val in arr:
            table[val] = table.get(val, 0) + 1
        if len(set(table.values())) != len(table):
            return False
        return True