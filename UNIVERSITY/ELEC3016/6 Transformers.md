- Transformers are magnetically coupled coils by a common magnetic field
- Transfer energy from one coil to the other
	- Only for AC currents and voltages
- Coils are usually placed on a common magnetic core
	- High frequency cores are made of magnetically soft ferrites
	- Steel transformers made from thin laminations, insulated from one another to minimise eddy currents
## The Principle
- Consider with two windings, a primary winding of $N_1$, $N_2$ for the secondary $$e_{1}= \frac{d\lambda_1}{dt}=N_1\frac{d\phi}{dt}, e_{2}=\frac{d\lambda_2}{dt}=N_2\frac{d\phi}{dt} $$ $$v_{1}= R_{1}i_{1}= R_{1}i_{1}+N_{1}\frac{d\phi}{dt}, v_{2}= R_{2}i_{2}= R_{2}i_{2}+N_{2}\frac{d\phi}{dt}$$ $$\frac{v_{1}}{v_{2}} \approx \frac{N_{1}}{N_{2}}=a = \frac{1}{n}$$ $$v_{1}>v_{2}== \text{step down transformer}$$ $$\frac{i_{1}}{i_{2}}\approx\frac{N_{2}}{N_{1}}=\frac{1}{a} \therefore v_{1}i_{1}=v_{2}i_{2}$$
- Ideal transformer: the winding resistances are negligible, all fluxes are confined to the core and link both windings; no leakage present, permeability of the core is infinite
- Increase in $v_{1}$ could run the transformation to saturation area, in this case the loss $R_{1}i_{1}$ is **NOT** negligible

# Types of Power Transformers
### Auto Wound Transformer
![[Pasted image 20250911093044.png]]
$$V_{s}= V_{2} + V_{1}, I_{L}= I_{1}+ I_{2}$$
- If $N_{1}=N_{2}$:$$2V_{2} = V_{s} = 2V_{L}$$
### 3 Phase Transformer
![[Pasted image 20250911093305.png]]
![[Pasted image 20250911093311.png]]
- Can treat it as three sets of single transformers
$$\Phi_{a}=\Phi_{m}cos\omega t, \Phi_{b}=\Phi_{m}cos(\omega t-120), \Phi_{c}=\Phi_{m}cos(\omega t-240)$$
- Sum all together to equal 0
### Current Transformers
![[Pasted image 20250911093650.png]]
$$I_{M}\approx \frac{N_{1}}{N_{2}}I_{L}$$
- With the switch open in the smaller circuit ($I_{M}=0$), impossible due to core saturation, with no secondary MMF to balance the primary MMF, resulting in dangerously high voltage pulses
	- Switch should be in parallel for safe operation
# Transformer Per-Unit Values
- Solving circuits containing transformers can be tedious, therefore we need per-unit system$$QuantityPerUnit = \frac{actualValue}{baseValueofQuantity}$$
$$P_{base}=V_{base}I_{base}, R_{base}=\frac{V_{base}}{I_{base}}$$
- Base values are determined for each section (transformers do not change the apparent power from section to section)
- The impedance of transformers are normally given in per unit based ratings of transformers