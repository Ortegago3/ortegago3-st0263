# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/proto/file_service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1csrc/proto/file_service.proto\" \n\x0b\x46ileRequest\x12\x11\n\tdirectory\x18\x01 \x01(\t\"!\n\x10\x46ileListResponse\x12\r\n\x05\x66iles\x18\x01 \x03(\t\"\x1c\n\tFileChunk\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\"\x1e\n\x0cUploadStatus\x12\x0e\n\x06status\x18\x01 \x01(\t2j\n\x0b\x46ileService\x12.\n\tListFiles\x12\x0c.FileRequest\x1a\x11.FileListResponse\"\x00\x12+\n\nUploadFile\x12\n.FileChunk\x1a\r.UploadStatus\"\x00(\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'src.proto.file_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_FILEREQUEST']._serialized_start=32
  _globals['_FILEREQUEST']._serialized_end=64
  _globals['_FILELISTRESPONSE']._serialized_start=66
  _globals['_FILELISTRESPONSE']._serialized_end=99
  _globals['_FILECHUNK']._serialized_start=101
  _globals['_FILECHUNK']._serialized_end=129
  _globals['_UPLOADSTATUS']._serialized_start=131
  _globals['_UPLOADSTATUS']._serialized_end=161
  _globals['_FILESERVICE']._serialized_start=163
  _globals['_FILESERVICE']._serialized_end=269
# @@protoc_insertion_point(module_scope)
