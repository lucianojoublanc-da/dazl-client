# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/digitalasset/ledger/api/v1/command_submission_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import trace_context_pb2 as com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2
from . import commands_pb2 as com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_commands__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/digitalasset/ledger/api/v1/command_submission_service.proto',
  package='com.digitalasset.ledger.api.v1',
  syntax='proto3',
  serialized_options=_b('\n\036com.digitalasset.ledger.api.v1B\"CommandSubmissionServiceOuterClass\252\002\036Com.DigitalAsset.Ledger.Api.V1'),
  serialized_pb=_b('\n?com/digitalasset/ledger/api/v1/command_submission_service.proto\x12\x1e\x63om.digitalasset.ledger.api.v1\x1a\x32\x63om/digitalasset/ledger/api/v1/trace_context.proto\x1a-com/digitalasset/ledger/api/v1/commands.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x91\x01\n\rSubmitRequest\x12:\n\x08\x63ommands\x18\x01 \x01(\x0b\x32(.com.digitalasset.ledger.api.v1.Commands\x12\x44\n\rtrace_context\x18\xe8\x07 \x01(\x0b\x32,.com.digitalasset.ledger.api.v1.TraceContext2k\n\x18\x43ommandSubmissionService\x12O\n\x06Submit\x12-.com.digitalasset.ledger.api.v1.SubmitRequest\x1a\x16.google.protobuf.EmptyBe\n\x1e\x63om.digitalasset.ledger.api.v1B\"CommandSubmissionServiceOuterClass\xaa\x02\x1e\x43om.DigitalAsset.Ledger.Api.V1b\x06proto3')
  ,
  dependencies=[com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2.DESCRIPTOR,com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_commands__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_SUBMITREQUEST = _descriptor.Descriptor(
  name='SubmitRequest',
  full_name='com.digitalasset.ledger.api.v1.SubmitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='commands', full_name='com.digitalasset.ledger.api.v1.SubmitRequest.commands', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trace_context', full_name='com.digitalasset.ledger.api.v1.SubmitRequest.trace_context', index=1,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=228,
  serialized_end=373,
)

_SUBMITREQUEST.fields_by_name['commands'].message_type = com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_commands__pb2._COMMANDS
_SUBMITREQUEST.fields_by_name['trace_context'].message_type = com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2._TRACECONTEXT
DESCRIPTOR.message_types_by_name['SubmitRequest'] = _SUBMITREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubmitRequest = _reflection.GeneratedProtocolMessageType('SubmitRequest', (_message.Message,), dict(
  DESCRIPTOR = _SUBMITREQUEST,
  __module__ = 'com.digitalasset.ledger.api.v1.command_submission_service_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.SubmitRequest)
  ))
_sym_db.RegisterMessage(SubmitRequest)


DESCRIPTOR._options = None

_COMMANDSUBMISSIONSERVICE = _descriptor.ServiceDescriptor(
  name='CommandSubmissionService',
  full_name='com.digitalasset.ledger.api.v1.CommandSubmissionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=375,
  serialized_end=482,
  methods=[
  _descriptor.MethodDescriptor(
    name='Submit',
    full_name='com.digitalasset.ledger.api.v1.CommandSubmissionService.Submit',
    index=0,
    containing_service=None,
    input_type=_SUBMITREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_COMMANDSUBMISSIONSERVICE)

DESCRIPTOR.services_by_name['CommandSubmissionService'] = _COMMANDSUBMISSIONSERVICE

# @@protoc_insertion_point(module_scope)
