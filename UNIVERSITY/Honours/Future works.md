3d point cloud map generate data
LLM generate data
Using a Kalman/Gated fusion to dynamically decide which model to trust more

# Notes
Unweighted MAE
# To Find
- Different lighting conditions
- **Drift from centre lane (get gps coords - stamped)**
	- Jerk
	- People to walk around
- ~~**Accuracy improvement with adversarial training**~~
- **Script to go through turning data**
- **Analysis of averaging the models**
	- Time cost
- **Simple data manipulation**
- Model size/vram usage
- Get more data points? maybe?
- Publishing Hz
- Number of data
- SLIDE NUMBERS
- Get a adversarial masked point cloud image
- Logging for deadmans
- Record incidents and what happened
- Development of robust SSM LiDAR end to end model for dynamic environments
- ~~Check for csv of outputs from adv masking training~~



The shuttle bus driving model uses **L1 loss** (mean absolute error), applied separately to each output head and then summed:

```python
criterion = nn.L1Loss()
...
loss1 = criterion(output1, label1)   # speed prediction vs. ground truth
loss2 = criterion(output2, label2)   # steering angle prediction vs. ground truth
loss = loss1 + loss2
```


- **Unweighted sum**: speed error and steering error get added together with no relative weighting, even though they're on very different physical scales (speed maxes around ~5.4, steering angle around ~0.3, based on the accuracy-threshold constants elsewhere in the script). In practice that means the loss is almost entirely dominated by whichever of the two has the larger raw magnitude — likely speed — so the optimizer is implicitly prioritizing getting speed right over steering, whether or not that's actually what you want.
- **L1, not L2/MSE**: L1 penalizes errors linearly rather than quadratically, so it's less sensitive to occasional large outlier errors (a sharp momentary mispredict from a wild frame) than MSE would be — a reasonable choice for this kind of noisy real-world sensor data, though it also means the model gets less pressure to correct large errors compared to an L2 loss.
- There's a commented-out `# criterion = nn.MSELoss()` right above it in the code, so MSE was considered/tried at some point but L1 is what's actually active.

If you want, I could add a `--loss_weight_speed`/`--loss_weight_steering` pair of sweepable args so the relative weighting between the two heads becomes something you can actually tune (right now it's implicitly whatever the raw unit scales happen to produce) — that's a fairly natural next axis to test given the sweep infrastructure already in place.

Good question — and worth flagging up front: Jetson Orin doesn't have separate "VRAM" the way a desktop GPU does. It uses **unified memory** shared between CPU and GPU (one LPDDR pool), and `nvidia-smi` doesn't work properly on Jetson at all — that's a discrete-GPU tool. Here's what actually works, at two different levels:

### System-level (whole-device memory/GPU usage, run on the host — not inside the container)

tegrastats (simplest, already installed)tegrastats — NVIDIA's own Jetson monitoring tool, built in, no install needed. Prints a live line every second or so: overall RAM used, GR3D (GPU) utilization %, EMC (memory controller) usage, per-core CPU load, temps, power draw. Good for "is the GPU actually busy and how much total memory is in use right now", but doesn't break usage down by process.