# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GRPC.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nGRPC.proto\x12\nnumFlights\"+\n\x14numberFlightsRequest\x12\x13\n\x0b\x61irlineCode\x18\x01 \x01(\t\".\n\x15numberFlightsResponse\x12\x15\n\rnumberFlights\x18\x01 \x01(\x05\x32j\n\rnumberFlights\x12Y\n\x10getNumberFlights\x12 .numFlights.numberFlightsRequest\x1a!.numFlights.numberFlightsResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GRPC_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NUMBERFLIGHTSREQUEST._serialized_start=26
  _NUMBERFLIGHTSREQUEST._serialized_end=69
  _NUMBERFLIGHTSRESPONSE._serialized_start=71
  _NUMBERFLIGHTSRESPONSE._serialized_end=117
  _NUMBERFLIGHTS._serialized_start=119
  _NUMBERFLIGHTS._serialized_end=225
# @@protoc_insertion_point(module_scope)