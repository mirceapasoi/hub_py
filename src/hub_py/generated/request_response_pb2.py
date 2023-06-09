# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: request_response.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import message_pb2 as message__pb2
import hub_event_pb2 as hub__event__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16request_response.proto\x1a\rmessage.proto\x1a\x0fhub_event.proto\"\x07\n\x05\x45mpty\"X\n\x10SubscribeRequest\x12\"\n\x0b\x65vent_types\x18\x01 \x03(\x0e\x32\r.HubEventType\x12\x14\n\x07\x66rom_id\x18\x02 \x01(\x04H\x00\x88\x01\x01\x42\n\n\x08_from_id\"\x1a\n\x0c\x45ventRequest\x12\n\n\x02id\x18\x01 \x01(\x04\"\"\n\x0eHubInfoRequest\x12\x10\n\x08\x64\x62_stats\x18\x01 \x01(\x08\"w\n\x0fHubInfoResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x12\n\nis_syncing\x18\x02 \x01(\x08\x12\x10\n\x08nickname\x18\x03 \x01(\t\x12\x11\n\troot_hash\x18\x04 \x01(\t\x12\x1a\n\x08\x64\x62_stats\x18\x05 \x01(\x0b\x32\x08.DbStats\"Q\n\x07\x44\x62Stats\x12\x14\n\x0cnum_messages\x18\x01 \x01(\x04\x12\x16\n\x0enum_fid_events\x18\x02 \x01(\x04\x12\x18\n\x10num_fname_events\x18\x03 \x01(\x04\"3\n\x11SyncStatusRequest\x12\x13\n\x06peerId\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_peerId\"J\n\x12SyncStatusResponse\x12\x12\n\nis_syncing\x18\x01 \x01(\x08\x12 \n\x0bsync_status\x18\x02 \x03(\x0b\x32\x0b.SyncStatus\"\xb9\x01\n\nSyncStatus\x12\x0e\n\x06peerId\x18\x01 \x01(\t\x12\x0e\n\x06inSync\x18\x02 \x01(\t\x12\x12\n\nshouldSync\x18\x03 \x01(\x08\x12\x18\n\x10\x64ivergencePrefix\x18\x04 \x01(\t\x12\x1c\n\x14\x64ivergenceSecondsAgo\x18\x05 \x01(\x05\x12\x15\n\rtheirMessages\x18\x06 \x01(\x04\x12\x13\n\x0bourMessages\x18\x07 \x01(\x04\x12\x13\n\x0blastBadSync\x18\x08 \x01(\x03\"{\n\x18TrieNodeMetadataResponse\x12\x0e\n\x06prefix\x18\x01 \x01(\x0c\x12\x14\n\x0cnum_messages\x18\x02 \x01(\x04\x12\x0c\n\x04hash\x18\x03 \x01(\t\x12+\n\x08\x63hildren\x18\x04 \x03(\x0b\x32\x19.TrieNodeMetadataResponse\"l\n\x18TrieNodeSnapshotResponse\x12\x0e\n\x06prefix\x18\x01 \x01(\x0c\x12\x17\n\x0f\x65xcluded_hashes\x18\x02 \x03(\t\x12\x14\n\x0cnum_messages\x18\x03 \x01(\x04\x12\x11\n\troot_hash\x18\x04 \x01(\t\" \n\x0eTrieNodePrefix\x12\x0e\n\x06prefix\x18\x01 \x01(\x0c\"\x1b\n\x07SyncIds\x12\x10\n\x08sync_ids\x18\x01 \x03(\x0c\"\x89\x01\n\nFidRequest\x12\x0b\n\x03\x66id\x18\x01 \x01(\x04\x12\x16\n\tpage_size\x18\x02 \x01(\rH\x00\x88\x01\x01\x12\x17\n\npage_token\x18\x03 \x01(\x0cH\x01\x88\x01\x01\x12\x14\n\x07reverse\x18\x04 \x01(\x08H\x02\x88\x01\x01\x42\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\n\n\x08_reverse\"}\n\x0b\x46idsRequest\x12\x16\n\tpage_size\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x17\n\npage_token\x18\x02 \x01(\x0cH\x01\x88\x01\x01\x12\x14\n\x07reverse\x18\x03 \x01(\x08H\x02\x88\x01\x01\x42\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\n\n\x08_reverse\"N\n\x0c\x46idsResponse\x12\x0c\n\x04\x66ids\x18\x01 \x03(\x04\x12\x1c\n\x0fnext_page_token\x18\x02 \x01(\x0cH\x00\x88\x01\x01\x42\x12\n\x10_next_page_token\"`\n\x10MessagesResponse\x12\x1a\n\x08messages\x18\x01 \x03(\x0b\x32\x08.Message\x12\x1c\n\x0fnext_page_token\x18\x02 \x01(\x0cH\x00\x88\x01\x01\x42\x12\n\x10_next_page_token\"\xc9\x01\n\x14\x43\x61stsByParentRequest\x12!\n\x0eparent_cast_id\x18\x01 \x01(\x0b\x32\x07.CastIdH\x00\x12\x14\n\nparent_url\x18\x05 \x01(\tH\x00\x12\x16\n\tpage_size\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x17\n\npage_token\x18\x03 \x01(\x0cH\x02\x88\x01\x01\x12\x14\n\x07reverse\x18\x04 \x01(\x08H\x03\x88\x01\x01\x42\x08\n\x06parentB\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\n\n\x08_reverse\"\x87\x01\n\x0fReactionRequest\x12\x0b\n\x03\x66id\x18\x01 \x01(\x04\x12$\n\rreaction_type\x18\x02 \x01(\x0e\x32\r.ReactionType\x12!\n\x0etarget_cast_id\x18\x03 \x01(\x0b\x32\x07.CastIdH\x00\x12\x14\n\ntarget_url\x18\x04 \x01(\tH\x00\x42\x08\n\x06target\"\xd1\x01\n\x15ReactionsByFidRequest\x12\x0b\n\x03\x66id\x18\x01 \x01(\x04\x12)\n\rreaction_type\x18\x02 \x01(\x0e\x32\r.ReactionTypeH\x00\x88\x01\x01\x12\x16\n\tpage_size\x18\x03 \x01(\rH\x01\x88\x01\x01\x12\x17\n\npage_token\x18\x04 \x01(\x0cH\x02\x88\x01\x01\x12\x14\n\x07reverse\x18\x05 \x01(\x08H\x03\x88\x01\x01\x42\x10\n\x0e_reaction_typeB\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\n\n\x08_reverse\"\x8a\x02\n\x18ReactionsByTargetRequest\x12!\n\x0etarget_cast_id\x18\x01 \x01(\x0b\x32\x07.CastIdH\x00\x12\x14\n\ntarget_url\x18\x06 \x01(\tH\x00\x12)\n\rreaction_type\x18\x02 \x01(\x0e\x32\r.ReactionTypeH\x01\x88\x01\x01\x12\x16\n\tpage_size\x18\x03 \x01(\rH\x02\x88\x01\x01\x12\x17\n\npage_token\x18\x04 \x01(\x0cH\x03\x88\x01\x01\x12\x14\n\x07reverse\x18\x05 \x01(\x08H\x04\x88\x01\x01\x42\x08\n\x06targetB\x10\n\x0e_reaction_typeB\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\n\n\x08_reverse\"E\n\x0fUserDataRequest\x12\x0b\n\x03\x66id\x18\x01 \x01(\x04\x12%\n\x0euser_data_type\x18\x02 \x01(\x0e\x32\r.UserDataType\"(\n\x18NameRegistryEventRequest\x12\x0c\n\x04name\x18\x01 \x01(\x0c\"3\n\x13VerificationRequest\x12\x0b\n\x03\x66id\x18\x01 \x01(\x04\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0c\",\n\rSignerRequest\x12\x0b\n\x03\x66id\x18\x01 \x01(\x04\x12\x0e\n\x06signer\x18\x02 \x01(\x0c\"M\n\x0bLinkRequest\x12\x0b\n\x03\x66id\x18\x01 \x01(\x04\x12\x11\n\tlink_type\x18\x02 \x01(\t\x12\x14\n\ntarget_fid\x18\x03 \x01(\x04H\x00\x42\x08\n\x06target\"\xb6\x01\n\x11LinksByFidRequest\x12\x0b\n\x03\x66id\x18\x01 \x01(\x04\x12\x16\n\tlink_type\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tpage_size\x18\x03 \x01(\rH\x01\x88\x01\x01\x12\x17\n\npage_token\x18\x04 \x01(\x0cH\x02\x88\x01\x01\x12\x14\n\x07reverse\x18\x05 \x01(\x08H\x03\x88\x01\x01\x42\x0c\n\n_link_typeB\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\n\n\x08_reverse\"\xcc\x01\n\x14LinksByTargetRequest\x12\x14\n\ntarget_fid\x18\x01 \x01(\x04H\x00\x12\x16\n\tlink_type\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x16\n\tpage_size\x18\x03 \x01(\rH\x02\x88\x01\x01\x12\x17\n\npage_token\x18\x04 \x01(\x0cH\x03\x88\x01\x01\x12\x14\n\x07reverse\x18\x05 \x01(\x08H\x04\x88\x01\x01\x42\x08\n\x06targetB\x0c\n\n_link_typeB\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\n\n\x08_reverse\"%\n\x16IdRegistryEventRequest\x12\x0b\n\x03\x66id\x18\x01 \x01(\x04\"2\n\x1fIdRegistryEventByAddressRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'request_response_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=58
  _EMPTY._serialized_end=65
  _SUBSCRIBEREQUEST._serialized_start=67
  _SUBSCRIBEREQUEST._serialized_end=155
  _EVENTREQUEST._serialized_start=157
  _EVENTREQUEST._serialized_end=183
  _HUBINFOREQUEST._serialized_start=185
  _HUBINFOREQUEST._serialized_end=219
  _HUBINFORESPONSE._serialized_start=221
  _HUBINFORESPONSE._serialized_end=340
  _DBSTATS._serialized_start=342
  _DBSTATS._serialized_end=423
  _SYNCSTATUSREQUEST._serialized_start=425
  _SYNCSTATUSREQUEST._serialized_end=476
  _SYNCSTATUSRESPONSE._serialized_start=478
  _SYNCSTATUSRESPONSE._serialized_end=552
  _SYNCSTATUS._serialized_start=555
  _SYNCSTATUS._serialized_end=740
  _TRIENODEMETADATARESPONSE._serialized_start=742
  _TRIENODEMETADATARESPONSE._serialized_end=865
  _TRIENODESNAPSHOTRESPONSE._serialized_start=867
  _TRIENODESNAPSHOTRESPONSE._serialized_end=975
  _TRIENODEPREFIX._serialized_start=977
  _TRIENODEPREFIX._serialized_end=1009
  _SYNCIDS._serialized_start=1011
  _SYNCIDS._serialized_end=1038
  _FIDREQUEST._serialized_start=1041
  _FIDREQUEST._serialized_end=1178
  _FIDSREQUEST._serialized_start=1180
  _FIDSREQUEST._serialized_end=1305
  _FIDSRESPONSE._serialized_start=1307
  _FIDSRESPONSE._serialized_end=1385
  _MESSAGESRESPONSE._serialized_start=1387
  _MESSAGESRESPONSE._serialized_end=1483
  _CASTSBYPARENTREQUEST._serialized_start=1486
  _CASTSBYPARENTREQUEST._serialized_end=1687
  _REACTIONREQUEST._serialized_start=1690
  _REACTIONREQUEST._serialized_end=1825
  _REACTIONSBYFIDREQUEST._serialized_start=1828
  _REACTIONSBYFIDREQUEST._serialized_end=2037
  _REACTIONSBYTARGETREQUEST._serialized_start=2040
  _REACTIONSBYTARGETREQUEST._serialized_end=2306
  _USERDATAREQUEST._serialized_start=2308
  _USERDATAREQUEST._serialized_end=2377
  _NAMEREGISTRYEVENTREQUEST._serialized_start=2379
  _NAMEREGISTRYEVENTREQUEST._serialized_end=2419
  _VERIFICATIONREQUEST._serialized_start=2421
  _VERIFICATIONREQUEST._serialized_end=2472
  _SIGNERREQUEST._serialized_start=2474
  _SIGNERREQUEST._serialized_end=2518
  _LINKREQUEST._serialized_start=2520
  _LINKREQUEST._serialized_end=2597
  _LINKSBYFIDREQUEST._serialized_start=2600
  _LINKSBYFIDREQUEST._serialized_end=2782
  _LINKSBYTARGETREQUEST._serialized_start=2785
  _LINKSBYTARGETREQUEST._serialized_end=2989
  _IDREGISTRYEVENTREQUEST._serialized_start=2991
  _IDREGISTRYEVENTREQUEST._serialized_end=3028
  _IDREGISTRYEVENTBYADDRESSREQUEST._serialized_start=3030
  _IDREGISTRYEVENTBYADDRESSREQUEST._serialized_end=3080
# @@protoc_insertion_point(module_scope)
