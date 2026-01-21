# LoRa Airtime & Mesh Capacity Estimator

This repository contains a small analytical tool for estimating:

- LoRa packet time-on-air  
- Theoretical packet throughput  
- Rough mesh network capacity under duty-cycle constraints  

This is not a simulator.
It is a first-principles estimator intended to show why LPWAN and mesh
architectures hit hard physical limits at scale.

## What This Tool Models

- Spreading factor impact on airtime  
- Payload size scaling  
- Duty-cycle constraints (EU ISM bands)  
- Single-channel capacity ceilings  
- Per-node throughput collapse as node count grows  

## What This Tool Does NOT Model

- Collisions  
- Acknowledgments  
- Retransmissions  
- Downlinks  
- Channel hopping  
- Regulatory edge cases  
- Interference or fading  

Results are optimistic upper bounds.

## Usage

```bash
python3 lora_airtime_calculator.py
