import sys
import os

# Asegúrate de que la carpeta 'proto' esté en sys.path
proto_path = os.path.join(os.path.dirname(__file__), '../services/proto')
if proto_path not in sys.path:
    sys.path.append(proto_path)

import grpc
import file_service_pb2
import file_service_pb2_grpc

def list_files(directory):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = file_service_pb2_grpc.FileServiceStub(channel)
        response = stub.ListFiles(file_service_pb2.FileRequest(directory=directory))
        print("Files in directory:", response.files)

def upload_file(file_path):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = file_service_pb2_grpc.FileServiceStub(channel)
        def file_chunks():
            with open(file_path, 'rb') as f:
                while chunk := f.read(1024):
                    yield file_service_pb2.FileChunk(content=chunk)
        response = stub.UploadFile(file_chunks())
        print(response.status)

if __name__ == "__main__":
    # Ajusta las rutas según la estructura de tu proyecto
    list_files("C:/Users/holme/OneDrive/Escritorio/Universidad/Noveno Semestre/Topicos Telematica/reto1/ortegago3-st0263/src/shared/files")
    upload_file("C:/Users/holme/OneDrive/Escritorio/Universidad/Noveno Semestre/Topicos Telematica/reto1/ortegago3-st0263/src/shared/files/testfile.txt")
