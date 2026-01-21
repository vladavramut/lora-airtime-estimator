#!/usr/bin/env python3
"""
LoRa Airtime and Capacity Estimator

This script calculates:
- Time-on-air for a LoRa packet
- Theoretical max packets per hour per channel
- Approximate network capacity under duty-cycle limits

It is intended for first-principles analysis of LPWAN and mesh constraints,
not marketing or idealized simulation.

Author: Vlad Avramut
Website: https://vladavramut.com
"""

import math

def lora_airtime(payload_bytes, sf, bandwidth=125000, coding_rate=5, preamble_symbols=8):
    symbol_duration = (2 ** sf) / bandwidth

    payload_symbol_nb = 8 + max(
        math.ceil(
            (8 * payload_bytes - 4 * sf + 28 + 16 - 20) /
            (4 * (sf - 2))
        ) * coding_rate,
        0
    )

    total_symbols = preamble_symbols + 4.25 + payload_symbol_nb
    airtime = total_symbols * symbol_duration

    return airtime


def packets_per_hour(airtime_seconds, duty_cycle=0.01):
    max_airtime_per_hour = 3600 * duty_cycle
    return max_airtime_per_hour / airtime_seconds


def estimate_mesh_capacity(nodes, payload_bytes, sf, bandwidth=125000, duty_cycle=0.01):
    airtime = lora_airtime(payload_bytes, sf, bandwidth)
    pph = packets_per_hour(airtime, duty_cycle)

    per_node_pph = pph / nodes
    per_node_interval = 3600 / per_node_pph if per_node_pph > 0 else float("inf")

    return {
        "airtime_seconds": round(airtime, 3),
        "max_packets_per_hour_total": round(pph, 2),
        "max_packets_per_hour_per_node": round(per_node_pph, 3),
        "avg_seconds_between_packets_per_node": round(per_node_interval, 1)
    }


if __name__ == "__main__":
    print("LoRa Airtime & Mesh Capacity Estimator\n")

    payload = int(input("Payload size (bytes): "))
    sf = int(input("Spreading Factor (7–12): "))
    nodes = int(input("Number of nodes in mesh: "))
    duty = float(input("Duty cycle (e.g. 0.01 = 1%): "))

    result = estimate_mesh_capacity(nodes, payload, sf, duty_cycle=duty)

    print("\nResults:")
    for k, v in result.items():
        print(f"{k}: {v}")
