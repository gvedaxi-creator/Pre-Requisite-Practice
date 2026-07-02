class WaitlistMerger:
    def __init__(self):
        self.list1 = [11, 13, 25, 27, 29]
        self.list2 = [12, 14, 26, 28, 30]
    def merge(self):
        merged_list = []
        i = j = 0

        while i < len(self.list1) and j < len(self.list2):
            if self.list1[i] < self.list2[j]:
                merged_list.append(self.list1[i])
                i += 1
            else:
                merged_list.append(self.list2[j])
                j += 1

        while i < len(self.list1):
            merged_list.append(self.list1[i])
            i += 1

        while j < len(self.list2):
            merged_list.append(self.list2[j])
            j += 1

        return merged_list

m = WaitlistMerger()
print("Merged Waitlist:", m.merge())
