from concurrent import futures
import logging

import grpc
import algorithm_pb2
import algorithm_pb2_grpc

class Algorithm(algorithm_pb2_grpc.AlgorithmServicer):
    def Add(self, request, context):
        sum = request.number1 + request.number2
        return algorithm_pb2.One(number1=sum)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    algorithm_pb2_grpc.add_AlgorithmServicer_to_server(Algorithm(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()