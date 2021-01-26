class cell:

    # 1 denotes possiblity, 0 denotes impossiblity

    def __init__(self, num, x, y):
        self.x = x
        self.y = y
        self.i = 0 # this is the index of the current number

        if num == 0:
            self.possible_nums = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        else:
            self.possible_nums = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            self.possible_nums[num-1] = 1
         

    # returns the index not the actual number
    def next_num(self):
        for j in range(self.i+1, 9):
            if self.possible_nums[j] != 0:
                self.i = j
                return j
        return -1 # this is only if there are no possible nums
    
    # removes number given actual number
    def remove_num(self, num):
        self.possible_nums[num-1] = 0

    # num should be given as index, not as the actual number
    def set_num(self, num):
        self.i = num
    

