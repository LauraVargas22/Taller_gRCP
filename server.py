import time
from concurrent import futures
import grpc
import greeter_pb2
import greeter_pb2_grpc
class GreeterServicer(greeter_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return greeter_pb2.HelloReply(
            message=f'Hola, {request.name}! Tienes {request.age} años.'
        )

    def SayGoodbye(self, request, context):
        return greeter_pb2.HelloReply(
            message=f'¡Hasta luego, {request.name}!'
        )

    def SayHelloRepeatedly(self, request, context):
        for i in range(5):
            yield greeter_pb2.HelloReply(
                message=f'Hola #{i + 1}, {request.name}!'
            )
            time.sleep(1)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(
        GreeterServicer(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Servidor gRPC escuchando en el puerto 50051...')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
