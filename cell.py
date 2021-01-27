class Cell:

    # 1 denotes possiblity, 0 denotes impossiblity

    def __init__(self, num, x, y):
        self.x = x
        self.y = y
        # the index will be max(num-1, 0)
        self.num = num
        self.is_fixed = False

        if num == 0:
            self.possible_nums = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        else:
            self.possible_nums = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            self.possible_nums[num-1] = 1
            self.is_fixed = True
         

    # returns the next number, does not set anything
    def next_num(self):
        for num_i in range(self.num+1, 10):
            if self.possible_nums[num_i-1] != 0:
                return num_i
        return -1 # this is only if there are no possible nums
    
    # removes number given num
    def remove_num(self, num):
        self.possible_nums[num-1] = 0

    # sets the number to num
    def set_num(self, num):
        self.num = num

    def get_num(self):
        return self.num

    def reset_i(self):
        self.possible_nums = [1, 1, 1, 1, 1, 1, 1, 1, 1]

