# gguf_reader.py
import struct

class GGUFReader:
    """
    Minimal GGUF reader.
    Currently loads:
    - header
    - metadata key/value pairs

    Tensor loading will be added later.
    """

    def __init__(self, path: str):
        self.path = path
        self.metadata = {}
        self._load()

    def _load(self):
        with open(self.path, "rb") as f:
            magic = f.read(4)
            if magic != b"GGUF":
                raise ValueError("Not a valid GGUF file")

            version, = struct.unpack("<I", f.read(4))

            # number of metadata KV pairs
            kv_count, = struct.unpack("<Q", f.read(8))

            for _ in range(kv_count):
                key_len, = struct.unpack("<I", f.read(4))
                key = f.read(key_len).decode("utf-8")

                val_type, = struct.unpack("<I", f.read(4))

                # Only support string metadata for now
                if val_type == 0:  # string
                    val_len, = struct.unpack("<I", f.read(4))
                    val = f.read(val_len).decode("utf-8")
                else:
                    val = None  # unsupported type for now

                self.metadata[key] = val