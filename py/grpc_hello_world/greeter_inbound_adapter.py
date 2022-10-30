import iris.pex

from concurrent import futures
import grpc

import grpc_hello_world.helloworld_pb2 as helloworld_pb2
import grpc_hello_world.helloworld_pb2_grpc as helloworld_pb2_grpc

from grpc_hello_world.utils import log
from grpc_hello_world.hello_request import HelloRequest


class GreeterInboundAdapter(iris.pex.InboundAdapter):
    """
    The greeter server gRPC hello world example adapted as an IRIS Inbound Adapter
    """

    gRPCPort = int(0)
    """Port of the gRPC server"""

    def OnInit(self):
        """
        The OnInit() method is called when the component is started. Use the OnInit() method to initialize any structures needed by the component.
        """
        log(self, "OnInit() is called")

        self.gRPCPort = int(
            self.gRPCPort)  # ensure that we are using a int data type
        log(self, "gRPCPort: %d" % self.gRPCPort)

        self.grpc_server = self.start_server()

        return

    def OnTearDown(self):
        """
        The OnTearDown() method is called before the business component is terminated. Use the OnTeardown() method to free any structures.
        """
        log(self, "OnTeardown() is called")

        self.grpc_server.stop(None)
        log(self, "Server stopped")

        return

    def start_server(self):
        """
        The Python implementation of the GRPC helloworld.Greeter server.
        """

        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        greeter = Greeter()

        # reference itself to the gRPC server implementation
        greeter.adapter = self

        helloworld_pb2_grpc.add_GreeterServicer_to_server(greeter, server)
        server.add_insecure_port('[::]:' + str(self.gRPCPort))

        server.start()
        log(self, "Server started, listening on %s" % self.gRPCPort)

        return server


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    """
    The Python implementation of the GRPC helloworld.Greeter server.
    """

    # PEX adapter reference
    adapter: iris.pex.InboundAdapter

    def SayHello(self, grpc_hello_request, context):
        log(
            self.adapter, "SayHello called with %s = %s" %
            (grpc_hello_request.__class__, grpc_hello_request.name))
        request = HelloRequest(name=grpc_hello_request.name)
        self.adapter.BusinessHost.ProcessInput(request)  # type: ignore

        return helloworld_pb2.HelloReply(message='Hello, %s!' %
                                         request.name)  # type: ignore
