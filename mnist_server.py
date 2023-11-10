from concurrent import futures
import random
import time
import grpc
import mnist_pb2
import mnist_pb2_grpc
from mnist import MNIST


class MnistServicer(mnist_pb2_grpc.MnistServiceServicer):
    mndata = MNIST('samples')
    images, labels = mndata.load_training()

    def GetTrainingSamples(self, request, context):
        mndata = MNIST('samples')
        images, labels = mndata.load_training()
        print(f"Returning {request.sample_size} images as stream")
        for x in range(0, request.sample_size):
            index = random.randrange(0, len(images))  # choose an index ;-)
            sample = mnist_pb2.Sample()
            sample.image = bytes(images[index])
            sample.label = labels[index]
            yield sample
            time.sleep(1)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mnist_pb2_grpc.add_MnistServiceServicer_to_server(MnistServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ =='__main__':
    serve()
