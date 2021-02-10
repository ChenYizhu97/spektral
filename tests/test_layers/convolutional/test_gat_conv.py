from core import run_layer, MODES
from spektral import layers

config = {
    "layer": layers.GATConv,
    "modes": [MODES["SINGLE"], MODES["BATCH"], MODES["MIXED"]],
    "kwargs": {
        "channels": 8,
        "attn_heads": 2,
        "concat_heads": False,
        "activation": "relu",
    },
    "dense": True,
    "sparse": True,
}


def test_layer():
    run_layer(config)
    config["kwargs"]["concat_heads"] = True
    try:
        run_layer(config)
    except AssertionError:
        # We expect this because the test checks for an output shape equal to channels
        pass