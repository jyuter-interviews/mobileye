import grpc
import grpc_testing
import unittest
import mnist_pb2
import mnist_server

class TestMnistServer(unittest.TestCase):
    def setUp(self):
        servicers = {mnist_pb2.DESCRIPTOR.services_by_name['Greeter']: MnistServicer()}

