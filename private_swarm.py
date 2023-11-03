from pprint import pprint
import hivemind
from health import fetch_health_state

INITIAL_PEERS = [
    "/ip4/86.48.21.229/tcp/31337/p2p/12D3KooWPyRUNtfz4f9RiPwhT99GVLvfVAALMXZ27AV1DubSc6oR",
    "/ip4/81.0.246.28/tcp/31337/p2p/12D3KooWA6QWj4eP5D9xfsuAfarhDJX1nGhHasmFYJEVkjhSydyV",
]
dht = hivemind.DHT(initial_peers=INITIAL_PEERS, client_mode=True, start=True)
pprint(fetch_health_state(dht))
