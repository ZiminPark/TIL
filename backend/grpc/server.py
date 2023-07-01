from concurrent import futures

import grpc
import structlog
from proto import hello_pb2, hello_pb2_grpc


class HelloService(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        logger.debug(f"Request Accepted: {request}")
        msg = f"Hello, {request.name}!"
        return hello_pb2.HelloResponse(message=msg)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(HelloService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    logger.info("Starting gPRC server on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    structlog.configure(
        processors=[
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer(),
        ]
    )
    logger = structlog.get_logger()
    serve()
