#db_server.p
import grpc
import function_grpc
from concurrent import futures

import time

import newpro_pb2
import newpro_pb2_grpc

class DatbaseServicer(newpro_pb2_grpc.displayInfoServicer):
	def GetFeature(self, request,context):
		# response=newpro_pb2.Feature()
		
		response=function_grpc.getCarats(request.input)
		return newpro_pb2.Feature(output=response)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

newpro_pb2_grpc.add_displayInfoServicer_to_server(DatbaseServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()


try:
	while True:
	  time.sleep(86400)
except KeyboardInterrupt:
	  server.stop(0)