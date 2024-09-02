from concurrent import futures
import grpc
import file_service_pb2
import file_service_pb2_grpc
import os

class FileServiceServicer(file_service_pb2_grpc.FileServiceServicer):
    def ListFiles(self, request, context):
        files = os.listdir(request.directory)
        return file_service_pb2.FileListResponse(files=files)

    def UploadFile(self, request_iterator, context):
        with open('uploaded_file', 'wb') as f:
            for file_chunk in request_iterator:
                f.write(file_chunk.content)
        return file_service_pb2.UploadStatus(status="File uploaded successfully")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    file_service_pb2_grpc.add_FileServiceServicer_to_server(FileServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC Server running on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()