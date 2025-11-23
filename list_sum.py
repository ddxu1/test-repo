class ListSum:
    def __init__(self, lst):
        self.lst = []
        self.lst_sum = sum(self.lst)

    
    def set_list(self, lst):
        self.lst = lst

    def get_sum(self):
        return sum(self.lst)
