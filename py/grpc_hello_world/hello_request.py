import iris.pex

class HelloRequest(iris.pex.Message,):

    def __init__(self, name=None):
        super().__init__()
        self.name = name