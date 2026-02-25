# AC Machines
### Rotating Magnetic Field
- If the magnetic field of a stator rotates, the rotor will constantly follow/chase the rotating magnetic field (three coils 120deg apart)
- Induced Voltage in Stator
	- Assume 3 phases produce components of field, the flux is proportional to current
# Construction of Synchronous Machines
- Two main parts, the rotor and stator
	- Doubly-fed machines
## DC Voltage Rotor: Two Types
1. Salient
	- Low-speed, concentrated winding, many poles
2. Non-Salient
	- High speed, distributed winding, 2 or 4 poles
- DC is supplied through brushes and slip ring
## Stator
- Laminated steel
- Armature winding (induced voltage)
- Rotate at constant speed, the same as the speed of rotating field in the airgap (synchronous)
## Paralleling Synchronous Machines
- The rms line voltages of the two generators must be equal
- The generators must have the same phase sequence and phase angles
# Synchronism
- The magnetic field of the stator is locked with the magnetic field of the rotor
- In motor flux, stator field is ahead of rotor field, opposite for generator flux
$$N_{s}=\frac{60f}{P}[rev/min], p = \frac{no.poles}{2}$$
## Open Circuit Characteristic
- The induced voltage when terminal is open circuit
$$E_{A} = K\phi\omega$$$$K = \frac{N_{C}}{\sqrt2}, \text{when omega is electrical rads}$$$$K = \frac{N_{C}P}{\sqrt2}, \text{when omega is mechanical rads}$$
## Equivalent Circuit (Non-Salient)
- The induced voltage normally does not appear at the terminal of the generator
- Armature reaction: the distortion of airgap field due to current in stator
- The leakage inductance of armature coils
- The resistance of armature coils
- The effect of salient pole rotor shape
- These cause current to lag the induced voltage
	- Creates a new magnetic field $B_{S}$ which creates an induced voltage across the magnetizing reactance
$$V_{\phi}=E_{A, max}+E_{S}, B_{net}=B_{R}+B_{S}$$
- For the voltage at the terminal
- The armature reaction effects $X$ and leakage inductance $X_{S}$ in the machine are both represented by reactance
- Synchronous Reactance: $$V_{\phi} = E_{A}-jX_{S}I_{A}-R_{A}I_{A}$$
	- $E_{A}$ is excitation voltage, $X_{S}$ is synch. reactance, $R_{A}$ is resistance of winding in phase $A$ 
## OCC & SCC
- Open circuit test
	- No current, no voltage drop
	- Gradually increase the field current at nominal speed
- Short circuit test
	- Terminal open shot circuit
	- Gradually increase at nominal speed
$$Z_{S}=\sqrt{R_{S}^{2}+X_{S}^{2}} = \frac{E_{A}}{I_{A}}$$
# Phasor Diagram
- Synchronous generator ($\delta > 0$):
![[Pasted image 20250922095357.png]]
![[Pasted image 20250922095654.png]]
- Synchronous Motor ($\delta < 0$)
![[Pasted image 20250922095918.png]]
# Excitation Control
- Done by changing excitation current (= field current)
- If the mechanical load is constant, the electrical power would be constant
- Unity power factor: the current is minimum at UPF, $E=E_{0}, \delta = \delta_{0}$
- PF Correction
	- Only synchro. motors can operate at leading PF
	- Induction motors operate at a lagging PF
	- Overexcited synchro machines to compensate the total lagging PF of the grid
	- 