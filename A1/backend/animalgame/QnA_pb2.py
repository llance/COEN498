# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: QnA.proto

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
  name='QnA.proto',
  package='MyPkg.Animals',
  serialized_pb=_b('\n\tQnA.proto\x12\rMyPkg.Animals\"7\n\x07\x43\x61rrier\x12\x10\n\x08question\x18\x01 \x02(\t\x12\n\n\x02id\x18\x02 \x02(\t\x12\x0e\n\x06\x61nswer\x18\x03 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CARRIER = _descriptor.Descriptor(
  name='Carrier',
  full_name='MyPkg.Animals.Carrier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='question', full_name='MyPkg.Animals.Carrier.question', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='MyPkg.Animals.Carrier.id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='answer', full_name='MyPkg.Animals.Carrier.answer', index=2,
      number=3, type=9, cpp_type=9, label=2,
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
  serialized_start=28,
  serialized_end=83,
)

DESCRIPTOR.message_types_by_name['Carrier'] = _CARRIER

Carrier = _reflection.GeneratedProtocolMessageType('Carrier', (_message.Message,), dict(
  DESCRIPTOR = _CARRIER,
  __module__ = 'QnA_pb2'
  # @@protoc_insertion_point(class_scope:MyPkg.Animals.Carrier)
  ))
_sym_db.RegisterMessage(Carrier)


# @@protoc_insertion_point(module_scope)
