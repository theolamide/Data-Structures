# Understanding
#   * can we count
#       solution: build count var
#   * ONE pass, not FIRST pass
#       sol: setup for the one pass
# turns out ^^^ was incorrect :grin:

#                                   c
#   [h/1] [2] [3] [4] [5] [6] [7] [t/8]
#                   m
# m = c // 2 + 1
# when (count reaches tail || next == null)
#   return m


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __len__(self):
        # come back here later
        return self.length

    def findMiddle(self, value):
        count = 0
        middle = 0
        while self.next != None:
            # track current node
            count += 1
            middle = (count // 2) + 1

        return middle


Collapse
