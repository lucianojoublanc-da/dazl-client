# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: da/daml_lf_0.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='da/daml_lf_0.proto',
  package='daml_lf_0',
  syntax='proto3',
  serialized_options=_b('\n\030com.digitalasset.daml_lf\252\002 Com.DigitalAsset.Daml_lf.DamlLf0'),
  serialized_pb=_b('\n\x12\x64\x61/daml_lf_0.proto\x12\tdaml_lf_0\"\t\n\x07PackageB=\n\x18\x63om.digitalasset.daml_lf\xaa\x02 Com.DigitalAsset.Daml_lf.DamlLf0b\x06proto3')
)




_PACKAGE = _descriptor.Descriptor(
  name='Package',
  full_name='daml_lf_0.Package',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=42,
)

DESCRIPTOR.message_types_by_name['Package'] = _PACKAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Package = _reflection.GeneratedProtocolMessageType('Package', (_message.Message,), dict(
  DESCRIPTOR = _PACKAGE,
  __module__ = 'da.daml_lf_0_pb2'
  # @@protoc_insertion_point(class_scope:daml_lf_0.Package)
  ))
_sym_db.RegisterMessage(Package)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
