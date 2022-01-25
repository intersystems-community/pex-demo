import iris.pex

class MyResponse(iris.pex.Message):

    def __init__(self, res=None):
        super().__init__()
        self.responseString = res