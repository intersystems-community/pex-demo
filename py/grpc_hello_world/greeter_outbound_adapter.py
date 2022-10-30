import iris.pex

import grpc

from grpc_hello_world.utils import log
import grpc_hello_world.helloworld_pb2 as helloworld_pb2
import grpc_hello_world.helloworld_pb2_grpc as helloworld_pb2_grpc

class GreeterOutboundAdapter(iris.pex.OutboundAdapter):
    """
    The Python implementation of the GRPC helloworld.Greeter as an Outbound Adapter.
    """

    """Address of the gRPC server"""
    gRPCHost = str("")

    """"Port of the gRPC server"""
    gRPCPort = str("")
    
    def OnInit(self):
        log(self, "OnInit() is called")
        return

    def OnTearDown(self):
        log(self, "OnTeardown() is called")
        return

    def sayHello(self, helloRequest):
        log(self, "sayHello(): name = %s" % (helloRequest.name))
        log(self, "sayHello(): server:port = %s:%s" % (self.gRPCHost, self.gRPCPort))
        log(self, "sayHello(): Will try to greet world ...")
        with grpc.insecure_channel("%s:%s" % (self.gRPCHost, self.gRPCPort)) as channel:
            stub = helloworld_pb2_grpc.GreeterStub(channel)
            response = self.process(stub, helloRequest)
        log(self, "sayHello(): Greeter client received: %s" % (response.message))
        return response

    def process(self, stub, helloRequest):
        response = stub.SayHello(helloworld_pb2.HelloRequest(name=helloRequest.name))
        return response