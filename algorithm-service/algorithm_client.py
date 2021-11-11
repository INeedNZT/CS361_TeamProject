"""
Example code of python how to use alogrithm microservice
"""

import logging

import grpc
import algorithm_pb2
import algorithm_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = algorithm_pb2_grpc.AlgorithmStub(channel)
        response = stub.Add(algorithm_pb2.Two(number1=1,number2=2))
    print("The sum is: ", response.number1)


if __name__ == '__main__':
    logging.basicConfig()
    run()