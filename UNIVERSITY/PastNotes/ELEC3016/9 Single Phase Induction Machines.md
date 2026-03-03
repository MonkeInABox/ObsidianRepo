# Single Phase Motors
- Small motors
- Three types:
	- Single phase induction
		- Majority
		- Classified based on starting methods (resistance, capacitor, shaded-pole)
	- Single phase synchronous
		- Runs at constant speed
		- Reluctance type and hysteresis type
	- Single phase series
		- Either DC or single phase supply
		- High starting torque
		- High speed
- If a 3 phase induction machine is disconnected, the result is a single phase
![[Pasted image 20251020110536.png]]
- Double revolving field theory: A pulsating field can be obtained from an interaction of two rotating fields
- Rotor stand still: Pulsating field induces current by transformer action in the rotor, this current creates a rotor pulsating flux. Stator and rotor field are on the same axis so no torque is created
### Single Phase Induction Motors
- If the rotor is made to revolve externally, the two torque components are no longer balanced, a torque is created
![[Pasted image 20251020110820.png]]
- The rotor current has two components, a positive sequence component $I_{rp}$, associated with the forward rotating field and a negative-sequence component $I_{rn}$ associated with the backwards rotating field
- Relative to the forward component, the fractional slip $s$ is given by: $$s_{f}=\frac{N_{s}-N_{r}}{N_{s}} = s$$
- Relative to the backward component, the fractional slip $s$ is given by: $$s_{b}=\frac{-N_{s}-N_{r}}{-N_{s}}=1+\frac{n_{r}}{N_{s}}=1+(1-s)=2-s$$
![[Pasted image 20251020111349.png]]
- If motor is running the same direction as the forward field:
	- Frequency of current induced by forward field = $sf$
	- Frequency of current induced by backward field = $(2-s)f$
	- Therefore $E_{f}>E_{b}, \Phi_{f}>\Phi_{b}$ 
### Starting of a single-phase motor
- Single phase motors have two windings
- The second winding is the auxiliary winding
	- It is wound in series with a capacitor and the phases of the two windings are displaced in space by $90\degree$ (for a 2 pole machine), corresponding to a $90\degree$ time phase displacement between the currents
	- This winding can be disconnected after starting