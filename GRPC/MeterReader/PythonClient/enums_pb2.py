# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: enums.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='enums.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\027MeterReaderWeb.Services'),
  serialized_pb=_b('\n\x0b\x65nums.proto*6\n\rReadingStatus\x12\x0b\n\x07INVALID\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02\x42\x1a\xaa\x02\x17MeterReaderWeb.Servicesb\x06proto3')
)

_READINGSTATUS = _descriptor.EnumDescriptor(
  name='ReadingStatus',
  full_name='ReadingStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=15,
  serialized_end=69,
)
_sym_db.RegisterEnumDescriptor(_READINGSTATUS)

ReadingStatus = enum_type_wrapper.EnumTypeWrapper(_READINGSTATUS)
INVALID = 0
SUCCESS = 1
FAILURE = 2


DESCRIPTOR.enum_types_by_name['ReadingStatus'] = _READINGSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)