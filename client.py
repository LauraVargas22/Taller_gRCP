import grpc
import greeter_pb2
import greeter_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greeter_pb2_grpc.GreeterStub(channel)

        request = greeter_pb2.HelloRequest(name='Estudiante', age=20)

        response = stub.SayHello(request)
        print('Respuesta unaria:', response.message)

        response = stub.SayGoodbye(request)
        print('Despedida unaria:', response.message)

        print('Respuestas en streaming:')
        for response in stub.SayHelloRepeatedly(request):
            print(' ->', response.message)


if __name__ == '__main__':
    run()