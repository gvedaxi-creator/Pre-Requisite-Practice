class PriceFilter:
    def __init__(self):
        self.price = [25000, 30000, 47000, 50000, 60000, 75000]

    def search(self, target):
        left = 0
        right = len(self.price) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if self.price[mid] >= target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        if ans == -1:
            print("No Product Found")
        else:
            print("First Product >= Target:", self.price[ans])


p = PriceFilter()

p.search(50000)
p.search(55000)
p.search(80000)