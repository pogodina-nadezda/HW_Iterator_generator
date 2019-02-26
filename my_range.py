class MyRange:
    def __init__(self, start, stop, step = 1):
        self.start = start
        self.stop = stop
        self.step = step
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.start < self.stop:
            for_print = self.start
            self.start += self.step
            return for_print
        else:
            raise StopIteration()
           
            
            
def MyRangeGenerator(start, stop, step = 1):
    while start < stop:
            for_print = start
            start += step
            yield for_print
