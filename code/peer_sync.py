#!/bin/python3
import requests
import subprocess as sp
import time
import json


def disconnectPeers(left=2):
    peers = json.loads(
        sp.getoutput(
            "docker exec miner miner peer gossip_peers"
        )
    )
    if len(peers) <= left:
        return
    for peer in peers[left - 1 :]:
        print(
            f"Try disconnect peer {peer}",
            sp.getoutput(
                f"docker exec miner miner peer disconnect {peer}"
            ),
        )

data=[
        {"p2pAddress":
            [
                "/ip4/31.223.195.49/tcp/44158",
                "/ip4/102.177.177.176/tcp/44158",
                "/ip4/207.154.220.49/tcp/44158",
                "/ip4/167.99.142.141/tcp/44158",

                ""
            ]
        }
    ]


while True:
    try:
        resp = requests.get(
            "https://p2p.heliuminerdeploy.xyz/api/miners/getMaxHeight?top=20"
        )
        data = resp.json()

        disconnectPeers(2)
        for miner in data["data"]:
            for peer in miner["p2pAddress"]:
                if "ip4" in peer:
                    print(
                        f"Try connect to {peer}",
                        sp.getoutput(
                            f"docker exec miner miner peer sync {peer}"
                        ),
                    )
    except:
        print("Failed to perform peer sync, retry next time")
    # perform peer sync every 30s
    break