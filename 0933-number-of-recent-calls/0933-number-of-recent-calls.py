class RecentCounter:

    def __init__(self):
        self.lst = []

    def ping(self, t: int) -> int:
        self.lst.append(t)
        while self.lst[0] < (t-3000) or self.lst[0] > t:
            self.lst.pop(0)
        return len(self.lst)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)