SCRIPT_DIR="$(dirname "$(realpath "${BASH_SOURCE[0]}")")"
# https://stackoverflow.com/questions/600079/how-do-i-clone-a-subdirectory-only-of-a-git-repository/52269934#52269934
svn export --force https://github.com/farcasterxyz/hub-monorepo/trunk/protobufs/schemas $SCRIPT_DIR/schemas
python3 -m grpc_tools.protoc \
    -I$SCRIPT_DIR/schemas \
    --python_out=$SCRIPT_DIR/generated --pyi_out=$SCRIPT_DIR/generated --grpc_python_out=$SCRIPT_DIR/generated \
    $SCRIPT_DIR/schemas/*.proto