import re

import iris.pex

from grpc_hello_world.utils import log
from grpc_hello_world.hello_reply import HelloReply
from grpc_hello_world.hello_request import HelloRequest


class GreeterBusinessOperation(iris.pex.BusinessOperation):

    def OnInit(self):
        log(self, "OnInit() is called")
        return

    def OnTeardown(self):
        log(self, "OnTeardown() is called")
        return

    def OnMessage(self, request):
        log(self, "OnMessage() was called")
        oref = request.getOREF()
        log(self, "oref: %s" % oref)
        if re.search("dc.MyRequest", oref):
            log(self, "dc.MyRequest detected, calling processMyRequest()...")
            return self.processMyRequest(request)
        elif re.search("dc.HelloRequest", oref):
            log(self,
                "dc.HelloRequest detected, calling processHelloRequest()...")
            return self.processHelloRequest(request)
        return

    def processMyRequest(self, irisMyRequest):
        name = irisMyRequest.get("requestString")
        log(self, "processHelloRequest() was called with message: %s" % (name))
        return self.callSayHello(name)

    def processHelloRequest(self, irisHelloRequest):
        name = irisHelloRequest.get("name")
        log(self, "processHelloRequest() was called with message: %s" % (name))
        return self.callSayHello(name)

    def callSayHello(self, name):
        helloRequest = HelloRequest(name=name)
        helloResponse = self.Adapter.invoke("sayHello", helloRequest)  # type: ignore
        response = HelloReply(helloResponse.message)
        return response