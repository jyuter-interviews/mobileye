import mnist_pb2
import mnist_pb2_grpc
import time
import grpc
from mnist import MNIST


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        try:
            stub = mnist_pb2_grpc.MnistServiceStub(channel)
            sample_size = int(input("Please enter the number of images you would like to retrieve: "))
            image_request = mnist_pb2.DataRequest(sample_size = sample_size)
            responses = stub.GetTrainingSamples(image_request)
            for response in responses:
                print(MNIST.display(response.image))
                print(response.label)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise

if __name__ == "__main__":
    run()
