from concurrent import futures
import logging

import grpc
import imagesend_pb2
import imagesend_pb2_grpc

class ImageSend(imagesend_pb2_grpc.ImageSendServicer):
    def Imagerequest(self, request, context):
        if request.image_name1 == "New York":
            with open("NY1.jpg", 'rb') as f1:
                image1 = f1.read()
            with open("NY2.jpg", 'rb') as f2:
                image2 = f2.read()
            return imagesend_pb2.images(images1 = image1, images2 = image2)
        elif request.image_name1 == "Los Angeles":
            image1 = open("LA1.jpg", 'rb')
            image2 = open("LA2.jpg", 'rb')
            return imagesend_pb2.images(images1 = image1, images2 = image2)
        elif request.image_name1 == "San Francisco":
            image1 = open("SF1.jpg", 'rb')
            image2 = open("SF2.jpg", 'rb')
            return imagesend_pb2.images(images1 = image1, images2 = image2)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    imagesend_pb2_grpc.add_ImageSendServicer_to_server(ImageSend(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()