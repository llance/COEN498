# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protoSerializer.proto

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
  name='protoSerializer.proto',
  package='protoData.test',
  serialized_pb=_b('\n\x15protoSerializer.proto\x12\x0eprotoData.test\"0\n\x0cprotoMessage\x12\x10\n\x08question\x18\x01 \x02(\t\x12\x0e\n\x06\x61nswer\x18\x02 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PROTOMESSAGE = _descriptor.Descriptor(
  name='protoMessage',
  full_name='protoData.test.protoMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='question', full_name='protoData.test.protoMessage.question', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='answer', full_name='protoData.test.protoMessage.answer', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['protoMessage'] = _PROTOMESSAGE

protoMessage = _reflection.GeneratedProtocolMessageType('protoMessage', (_message.Message,), dict(
  DESCRIPTOR = _PROTOMESSAGE,
  __module__ = 'protoSerializer_pb2'
  # @@protoc_insertion_point(class_scope:protoData.test.protoMessage)
  ))
_sym_db.RegisterMessage(protoMessage)


# @@protoc_insertion_point(module_scope)
