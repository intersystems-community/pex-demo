import iris.pex

class MyRequest(iris.pex.Message):

    def __init__(self, req=None):
        super().__init__()
        self.requestString = req