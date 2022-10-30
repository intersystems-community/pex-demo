# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

############################
# put the nod parent directory (module) in the python path
import os
import sys
from pathlib import Path
dir_path = os.path.dirname(os.path.realpath(__file__))
classpath = str(Path(dir_path).parent)
sys.path.append(classpath)
#############################

import logging

import grpc

import grpc_hello_world.helloworld_pb2 as helloworld_pb2
import grpc_hello_world.helloworld_pb2_grpc as helloworld_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        if len(sys.argv) > 1:
            myName = sys.argv[1]
        else:
            myName = 'you'
        response = stub.SayHello(helloworld_pb2.HelloRequest(name=myName))  # type: ignore
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
