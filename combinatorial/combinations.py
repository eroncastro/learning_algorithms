class Combination:
    def __init__(self, alist):
        self.alist = alist
    
    def combinations(self, subset=None, index=0):
        if subset is None:
            subset = []
        
        if index >= len(self.alist):
            return [subset]
        
        left = self.combinations(subset, index + 1)
        right = self.combinations(subset + [self.alist[index]], index + 1)
        return left + right
