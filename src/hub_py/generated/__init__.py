import os
import sys

# Required to import gRPC generated code
generated_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(generated_dir)
