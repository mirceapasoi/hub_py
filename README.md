# hub_py

An incomplete port of [@farcaster/hub-nodejs](https://github.com/farcasterxyz/hub-monorepo/tree/main/packages/hub-nodejs) gRPC client and [@farcaster/core](https://github.com/farcasterxyz/hub-monorepo/tree/main/packages/core) protobuf definitions and utility functions for Python

## Protocol buffers

To generate the latest protocol buffer Python code run this:

```
% ./src/hub_py/generate_proto.sh
A    src/hub_py/schemas
A    src/hub_py/schemas/gossip.proto
A    src/hub_py/schemas/hub_event.proto
A    src/hub_py/schemas/hub_state.proto
A    src/hub_py/schemas/id_registry_event.proto
A    src/hub_py/schemas/job.proto
A    src/hub_py/schemas/message.proto
A    src/hub_py/schemas/name_registry_event.proto
A    src/hub_py/schemas/request_response.proto
A    src/hub_py/schemas/rpc.proto
A    src/hub_py/schemas/sync_trie.proto
Exported revision 602.
```

## Examples

-   [Generate a chronological feed](./examples/chron_feed.py) using `asyncio`
-   [Building casts correctly](./examples/make_cast.py) including a patch to account for difference in serialization with `ts-proto` ([issue](https://github.com/farcasterxyz/hub-monorepo/issues/757))
-   [Write data for a user](./examples/write_data.py) including loading a Farcaster account from a mnemonic

For ease of use, the example scripts load data from a `.env` file:

```
FARCASTER_HUB=testnet1.farcaster.xyz:2283
FARCASTER_USE_SSL=true
FARCASTER_NETWORK=FARCASTER_NETWORK_TESTNET
# Used by write_data.py
FARCASTER_ID=<your-farcaster-id>
FARCASTER_MNEMONIC=<your-farcaster-mnemonic>
# If not specified, a random signer key will be generated
FARCASTER_SIGNER_KEY=<ed25519-private-key-for-signer>
```
