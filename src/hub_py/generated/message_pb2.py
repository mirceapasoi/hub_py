# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmessage.proto\"\xa4\x01\n\x07Message\x12\x1a\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x0c.MessageData\x12\x0c\n\x04hash\x18\x02 \x01(\x0c\x12 \n\x0bhash_scheme\x18\x03 \x01(\x0e\x32\x0b.HashScheme\x12\x11\n\tsignature\x18\x04 \x01(\x0c\x12*\n\x10signature_scheme\x18\x05 \x01(\x0e\x32\x10.SignatureScheme\x12\x0e\n\x06signer\x18\x06 \x01(\x0c\"\x80\x04\n\x0bMessageData\x12\x1a\n\x04type\x18\x01 \x01(\x0e\x32\x0c.MessageType\x12\x0b\n\x03\x66id\x18\x02 \x01(\x04\x12\x11\n\ttimestamp\x18\x03 \x01(\r\x12\"\n\x07network\x18\x04 \x01(\x0e\x32\x11.FarcasterNetwork\x12%\n\rcast_add_body\x18\x05 \x01(\x0b\x32\x0c.CastAddBodyH\x00\x12+\n\x10\x63\x61st_remove_body\x18\x06 \x01(\x0b\x32\x0f.CastRemoveBodyH\x00\x12&\n\rreaction_body\x18\x07 \x01(\x0b\x32\r.ReactionBodyH\x00\x12K\n!verification_add_eth_address_body\x18\t \x01(\x0b\x32\x1e.VerificationAddEthAddressBodyH\x00\x12;\n\x18verification_remove_body\x18\n \x01(\x0b\x32\x17.VerificationRemoveBodyH\x00\x12)\n\x0fsigner_add_body\x18\x0b \x01(\x0b\x32\x0e.SignerAddBodyH\x00\x12\'\n\x0euser_data_body\x18\x0c \x01(\x0b\x32\r.UserDataBodyH\x00\x12/\n\x12signer_remove_body\x18\r \x01(\x0b\x32\x11.SignerRemoveBodyH\x00\x42\x06\n\x04\x62ody\";\n\rSignerAddBody\x12\x0e\n\x06signer\x18\x01 \x01(\x0c\x12\x11\n\x04name\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_name\"\"\n\x10SignerRemoveBody\x12\x0e\n\x06signer\x18\x01 \x01(\x0c\":\n\x0cUserDataBody\x12\x1b\n\x04type\x18\x01 \x01(\x0e\x32\r.UserDataType\x12\r\n\x05value\x18\x02 \x01(\t\";\n\x05\x45mbed\x12\r\n\x03url\x18\x01 \x01(\tH\x00\x12\x1a\n\x07\x63\x61st_id\x18\x02 \x01(\x0b\x32\x07.CastIdH\x00\x42\x07\n\x05\x65mbed\"\xbf\x01\n\x0b\x43\x61stAddBody\x12\x19\n\x11\x65mbeds_deprecated\x18\x01 \x03(\t\x12\x10\n\x08mentions\x18\x02 \x03(\x04\x12!\n\x0eparent_cast_id\x18\x03 \x01(\x0b\x32\x07.CastIdH\x00\x12\x14\n\nparent_url\x18\x07 \x01(\tH\x00\x12\x0c\n\x04text\x18\x04 \x01(\t\x12\x1a\n\x12mentions_positions\x18\x05 \x03(\r\x12\x16\n\x06\x65mbeds\x18\x06 \x03(\x0b\x32\x06.EmbedB\x08\n\x06parent\"%\n\x0e\x43\x61stRemoveBody\x12\x13\n\x0btarget_hash\x18\x01 \x01(\x0c\"#\n\x06\x43\x61stId\x12\x0b\n\x03\x66id\x18\x01 \x01(\x04\x12\x0c\n\x04hash\x18\x02 \x01(\x0c\"n\n\x0cReactionBody\x12\x1b\n\x04type\x18\x01 \x01(\x0e\x32\r.ReactionType\x12!\n\x0etarget_cast_id\x18\x02 \x01(\x0b\x32\x07.CastIdH\x00\x12\x14\n\ntarget_url\x18\x03 \x01(\tH\x00\x42\x08\n\x06target\"[\n\x1dVerificationAddEthAddressBody\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x15\n\reth_signature\x18\x02 \x01(\x0c\x12\x12\n\nblock_hash\x18\x03 \x01(\x0c\")\n\x16VerificationRemoveBody\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c*:\n\nHashScheme\x12\x14\n\x10HASH_SCHEME_NONE\x10\x00\x12\x16\n\x12HASH_SCHEME_BLAKE3\x10\x01*g\n\x0fSignatureScheme\x12\x19\n\x15SIGNATURE_SCHEME_NONE\x10\x00\x12\x1c\n\x18SIGNATURE_SCHEME_ED25519\x10\x01\x12\x1b\n\x17SIGNATURE_SCHEME_EIP712\x10\x02*\xd0\x02\n\x0bMessageType\x12\x15\n\x11MESSAGE_TYPE_NONE\x10\x00\x12\x19\n\x15MESSAGE_TYPE_CAST_ADD\x10\x01\x12\x1c\n\x18MESSAGE_TYPE_CAST_REMOVE\x10\x02\x12\x1d\n\x19MESSAGE_TYPE_REACTION_ADD\x10\x03\x12 \n\x1cMESSAGE_TYPE_REACTION_REMOVE\x10\x04\x12-\n)MESSAGE_TYPE_VERIFICATION_ADD_ETH_ADDRESS\x10\x07\x12$\n MESSAGE_TYPE_VERIFICATION_REMOVE\x10\x08\x12\x1b\n\x17MESSAGE_TYPE_SIGNER_ADD\x10\t\x12\x1e\n\x1aMESSAGE_TYPE_SIGNER_REMOVE\x10\n\x12\x1e\n\x1aMESSAGE_TYPE_USER_DATA_ADD\x10\x0b*\x8a\x01\n\x10\x46\x61rcasterNetwork\x12\x1a\n\x16\x46\x41RCASTER_NETWORK_NONE\x10\x00\x12\x1d\n\x19\x46\x41RCASTER_NETWORK_MAINNET\x10\x01\x12\x1d\n\x19\x46\x41RCASTER_NETWORK_TESTNET\x10\x02\x12\x1c\n\x18\x46\x41RCASTER_NETWORK_DEVNET\x10\x03*\xa5\x01\n\x0cUserDataType\x12\x17\n\x13USER_DATA_TYPE_NONE\x10\x00\x12\x16\n\x12USER_DATA_TYPE_PFP\x10\x01\x12\x1a\n\x16USER_DATA_TYPE_DISPLAY\x10\x02\x12\x16\n\x12USER_DATA_TYPE_BIO\x10\x03\x12\x16\n\x12USER_DATA_TYPE_URL\x10\x05\x12\x18\n\x14USER_DATA_TYPE_FNAME\x10\x06*X\n\x0cReactionType\x12\x16\n\x12REACTION_TYPE_NONE\x10\x00\x12\x16\n\x12REACTION_TYPE_LIKE\x10\x01\x12\x18\n\x14REACTION_TYPE_RECAST\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'message_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HASHSCHEME._serialized_start=1435
  _HASHSCHEME._serialized_end=1493
  _SIGNATURESCHEME._serialized_start=1495
  _SIGNATURESCHEME._serialized_end=1598
  _MESSAGETYPE._serialized_start=1601
  _MESSAGETYPE._serialized_end=1937
  _FARCASTERNETWORK._serialized_start=1940
  _FARCASTERNETWORK._serialized_end=2078
  _USERDATATYPE._serialized_start=2081
  _USERDATATYPE._serialized_end=2246
  _REACTIONTYPE._serialized_start=2248
  _REACTIONTYPE._serialized_end=2336
  _MESSAGE._serialized_start=18
  _MESSAGE._serialized_end=182
  _MESSAGEDATA._serialized_start=185
  _MESSAGEDATA._serialized_end=697
  _SIGNERADDBODY._serialized_start=699
  _SIGNERADDBODY._serialized_end=758
  _SIGNERREMOVEBODY._serialized_start=760
  _SIGNERREMOVEBODY._serialized_end=794
  _USERDATABODY._serialized_start=796
  _USERDATABODY._serialized_end=854
  _EMBED._serialized_start=856
  _EMBED._serialized_end=915
  _CASTADDBODY._serialized_start=918
  _CASTADDBODY._serialized_end=1109
  _CASTREMOVEBODY._serialized_start=1111
  _CASTREMOVEBODY._serialized_end=1148
  _CASTID._serialized_start=1150
  _CASTID._serialized_end=1185
  _REACTIONBODY._serialized_start=1187
  _REACTIONBODY._serialized_end=1297
  _VERIFICATIONADDETHADDRESSBODY._serialized_start=1299
  _VERIFICATIONADDETHADDRESSBODY._serialized_end=1390
  _VERIFICATIONREMOVEBODY._serialized_start=1392
  _VERIFICATIONREMOVEBODY._serialized_end=1433
# @@protoc_insertion_point(module_scope)
