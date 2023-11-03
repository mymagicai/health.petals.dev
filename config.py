#from petals.constants import PUBLIC_INITIAL_PEERS

from data_structures import ModelInfo

INITIAL_PEERS = [
    "/ip4/86.48.21.229/tcp/31337/p2p/12D3KooWPyRUNtfz4f9RiPwhT99GVLvfVAALMXZ27AV1DubSc6oR",
    "/ip4/81.0.246.28/tcp/31337/p2p/12D3KooWA6QWj4eP5D9xfsuAfarhDJX1nGhHasmFYJEVkjhSydyV",
]

MODELS = [
    ModelInfo(
        dht_prefix="Llama-2-70b-chat-hf",
        repository="https://huggingface.co/meta-llama/Llama-2-70b-chat-hf",
        num_blocks=80,
    ),
]

UPDATE_PERIOD = 60
