import iris.pex

from grpc_hello_world.utils import log

class GreeterBusinessService(iris.pex.BusinessService):
    """
    The greeter server gRPC hello world example adapted as an IRIS Business Service
    """
    
    def OnInit(self):
        log(self, "OnInit() is called")
        return

    def OnTeardown(self):
        log(self, "OnTeardown() is called")
        return

    def OnProcessInput(self, messageInput):
        log(self, "OnProcessInput() is called")
        log(self, "messageInput: %s" % messageInput)
        return