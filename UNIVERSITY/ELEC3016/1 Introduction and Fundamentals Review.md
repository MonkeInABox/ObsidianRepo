Unit Coordinator = Herbert Iu
# Circuitry Theory
### Kirchoff's Current Law
$$\Sigma_{node} i_{k}= 0$$
### Kirchoff's Voltage Law
$$\Sigma_{loop} v_{k}= 0$$
### Miscellaneous
$$v=iR, i=C\frac{dv}{dt}, v = L\frac{di}{dt}$$
# Time Varying Signals
$$v(t)=v_{max}sin(\omega t + \theta _{v})$$
$$i(t)=vi{max}sin(\omega t + \theta _{i})$$
### Frequency Domain Phasors
$$v(t)=Vcos(\omega t + \theta_{v}) | \mathbf{V}=Ve^{j\theta_{v}}$$
$$V_{RMS}=V/\sqrt2$$
$$\mathbf{V}e^{j\omega t}=Ve^{j\theta_{v}}e^{j\omega t}$$
$$v(t)=Re[\mathbf{V}e^{j\omega t}]=Vcos(\omega t + \theta _{v})$$
$$\mathbf{V}=\frac{-j\mathbf{I}}{\omega c}=-j\mathbf{I}\omega L$$
# AC Power
$$v(t)=V_{m}cos(\omega t+\theta _{v})$$
$$i(t)=I_{m}cos(\omega t+\theta _{i})$$
$$p(t)=v(t)i(t)$$
$$\text{Active Power}=p_{R}(t)=V_{rms}I_{rms}cos\theta (1+cos(2\omega t))$$
$$\text{Reactive Power}=p_{L}(t)=V_{rms}I_{rms}sin\theta sin(2\omega t)$$
- Reactive power (Q) is 90 degrees out of phase, imaginary and used for inductors and capacitors, measured in $VAR$ , active power (P) is the true power $W$ with the apparent power (S) being the combination $VA$ and is active + reactive
$$\mathbf{S}=\mathbf{VI}^{*}=VIe^{j(\theta_{v}-\theta_{i})}=VIcos(\theta_{v}-\theta_{i})+jVIsin(\theta_{v}-\theta_{i})=P+jQ$$
$$P=|\mathbf{S}|cos\theta , Q=|\mathbf{S}|sin\theta$$
- This is the power triangle
- The power factor is the ratio between true and apparent power
	- pf = 1 when resistive load, <1 when leading (angle of current greater, capacitive, neg reactive power), <1 when lagging (inductive, pos reactive power)
	- 0 when purely inductive or capacitive
## 3 Phase AC System
![[Pasted image 20250721143639.png]]
- ACB is same thing, just in a different order
- Notably, $V_{A}+ V_{B}+ V_{C} = 0$ if they are at $120\degree$ of each other
## 3 Phase Wye (Star) Connection
![[Pasted image 20250721143810.png]]
$$\mathbf{I}_{N}= \mathbf I _{A}+ \mathbf I _B + \mathbf I _{C}| I_{ }=\frac{V_{}}{Z_{}}$$
- With balanced loads, this is 0
- The voltage across each element of a wye connected device is the phase voltage
- The current is the phase current
- Voltage across lines is line-to-line or just line voltage, likewise with current
$$V_{line}=\sqrt3 V_{phase}1\angle 30 \degree, I_{line}=I_{phase}$$
## 3 Phase Delta Connection
![[Pasted image 20250721144222.png]]
## Instantaneous Power for Three Phase
$$p(t)=v(t) \times i(t)\therefore p_{3\phi}(t) = 3V_{\phi}I_{\phi}cos\theta=\sqrt3 V_{L}I_{L}cos\theta$$
- Which is constant with no pulsations (not time dependent)!
