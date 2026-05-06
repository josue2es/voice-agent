"""Configuration for the server.

Centralizing settings here means you change behavior in one file
instead of hunting through the codebase. Later we'll load these from
environment variables, but for Step 1 plain constants are fine.
"""

# Whisper model to use. Options: tiny, base, small, medium, large-v3
# 'small' is our chosen balance of speed and multilingual accuracy.
WHISPER_MODEL = "small"

# Where to run the model. 'cpu' for our modest hardware.
# 'cuda' if you ever add a GPU.
WHISPER_DEVICE = "cpu"

# Compute precision. 'int8' is the fastest CPU option with minimal
# accuracy loss. 'float32' is the most accurate but ~2x slower.
WHISPER_COMPUTE_TYPE = "int8"

# Server bind address. '0.0.0.0' means "listen on all network
# interfaces" so your phone on the same Wi-Fi can reach it.
# Use '127.0.0.1' to lock it to localhost only (more secure but
# blocks the phone).
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8000
