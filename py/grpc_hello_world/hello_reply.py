import iris.pex

class HelloReply(iris.pex.Message,):

    def __init__(self, message=None):
        super().__init__()
        self.message = message