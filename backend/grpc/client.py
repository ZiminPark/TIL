import logging

import grpc
from proto import hello_pb2, hello_pb2_grpc

logging.basicConfig(level=logging.DEBUG)


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hello_pb2.HelloRequest(name="Alice"))
    logging.debug(response.message)


if __name__ == "__main__":
    run()
