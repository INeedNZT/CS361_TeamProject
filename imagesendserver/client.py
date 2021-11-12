import logging

import grpc
import imagesend_pb2
import imagesend_pb2_grpc


def run():
    image_Name = input(">")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = imagesend_pb2_grpc.ImageSendStub(channel)
        response = stub.Imagerequest(imagesend_pb2.image_name(image_name1=image_Name))
    rec_image1 = open("./image/"+image_Name+"1.jpg", 'wb')
    rec_image1.write(response.images1)
    rec_image2 = open("./image/"+image_Name+"2.jpg", 'wb')
    rec_image2.write(response.images2)


if __name__ == '__main__':
    logging.basicConfig()
    run()
