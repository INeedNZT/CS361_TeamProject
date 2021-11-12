# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import regform_pb2 as regform__pb2


class MyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MyMethod1 = channel.unary_unary(
                '/handson.MyService/MyMethod1',
                request_serializer=regform__pb2.MyRequest.SerializeToString,
                response_deserializer=regform__pb2.MyResponse.FromString,
                )
        self.MyMethod2 = channel.unary_unary(
                '/handson.MyService/MyMethod2',
                request_serializer=regform__pb2.MyRequest.SerializeToString,
                response_deserializer=regform__pb2.MyResponse.FromString,
                )
        self.MyMethod3 = channel.stream_stream(
                '/handson.MyService/MyMethod3',
                request_serializer=regform__pb2.MyRequest.SerializeToString,
                response_deserializer=regform__pb2.MyResponse.FromString,
                )


class MyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def MyMethod1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MyMethod2(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MyMethod3(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MyMethod1': grpc.unary_unary_rpc_method_handler(
                    servicer.MyMethod1,
                    request_deserializer=regform__pb2.MyRequest.FromString,
                    response_serializer=regform__pb2.MyResponse.SerializeToString,
            ),
            'MyMethod2': grpc.unary_unary_rpc_method_handler(
                    servicer.MyMethod2,
                    request_deserializer=regform__pb2.MyRequest.FromString,
                    response_serializer=regform__pb2.MyResponse.SerializeToString,
            ),
            'MyMethod3': grpc.stream_stream_rpc_method_handler(
                    servicer.MyMethod3,
                    request_deserializer=regform__pb2.MyRequest.FromString,
                    response_serializer=regform__pb2.MyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'handson.MyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MyService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def MyMethod1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/handson.MyService/MyMethod1',
            regform__pb2.MyRequest.SerializeToString,
            regform__pb2.MyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MyMethod2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/handson.MyService/MyMethod2',
            regform__pb2.MyRequest.SerializeToString,
            regform__pb2.MyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MyMethod3(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/handson.MyService/MyMethod3',
            regform__pb2.MyRequest.SerializeToString,
            regform__pb2.MyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
