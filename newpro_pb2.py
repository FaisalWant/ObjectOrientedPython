# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: newpro.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='newpro.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0cnewpro.proto\"\x17\n\x06Number\x12\r\n\x05value\x18\x01 \x01(\t2/\n\x0b\x64isplayInfo\x12 \n\nGetFeature\x12\x07.Number\x1a\x07.Number\"\x00\x62\x06proto3')
)




_NUMBER = _descriptor.Descriptor(
  name='Number',
  full_name='Number',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Number.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=39,
)

DESCRIPTOR.message_types_by_name['Number'] = _NUMBER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Number = _reflection.GeneratedProtocolMessageType('Number', (_message.Message,), dict(
  DESCRIPTOR = _NUMBER,
  __module__ = 'newpro_pb2'
  # @@protoc_insertion_point(class_scope:Number)
  ))
_sym_db.RegisterMessage(Number)



_DISPLAYINFO = _descriptor.ServiceDescriptor(
  name='displayInfo',
  full_name='displayInfo',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=41,
  serialized_end=88,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFeature',
    full_name='displayInfo.GetFeature',
    index=0,
    containing_service=None,
    input_type=_NUMBER,
    output_type=_NUMBER,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DISPLAYINFO)

DESCRIPTOR.services_by_name['displayInfo'] = _DISPLAYINFO

# @@protoc_insertion_point(module_scope)
