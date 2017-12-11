
import grpc
# import the generated classes
import newpro_pb2
import newpro_pb2_grpc
# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')
# create a stub (client)
stub = newpro_pb2_grpc.displayInfoStub(channel)
# create a valid request message
number = newpro_pb2.Point(input='carat')
# make the call
response = stub.GetFeature(number)
# et voilà
print(response.output)
