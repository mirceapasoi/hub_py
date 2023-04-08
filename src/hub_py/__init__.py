import os

# Necessary to implement the patched serializer
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
