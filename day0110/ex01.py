class whisky:
    def __init__(self, do, type, mili):
        self.do = do
        self.type = type
        self.mili = mili

    @property
    def do(self):
        return self.do
    
    @set
    def do(self, do):
        self.do = do