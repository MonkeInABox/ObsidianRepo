# Effects on Conductors
- Conductor in a magnetic field
	- Magnetic field strength is Magnetic Flux Density $\mathbf{B}$
	- Two possible effects
		- If the conductor moving with speed $v$ in the direction perpendicular to the field and current: $e = Blv$ where $l$ is length of conductor, $e$ is EMF
		- Conductor carries current $i$ in a direction perpendicular to the field $f=Bli$ where $f$ is the force
	- The Lorentz Force Law describes the forces on a moving charge $q$
$$\mathbf F=q(\mathbf E + v + \mathbf B)$$
- Force can be divided into 2 components:
	- Electric with the forces on moving charge $q$: $\mathbf F _{e}=q\mathbf E$
	- Magnetic forces on a moving charge: $\mathbf F_{m}=q(v \times \mathbf B)$
	- $\mathbf F_{e}=-\mathbf F_{m}\space \space \therefore E = -v \times B$
![[Pasted image 20250728140212.png]]
# Magnetic Forces on Iron
- U shaped steel cores with two coils creates magnetic field which exert forces on an iron bar (armature), air gap between to allow for moving parts
- This magnetic field is shown by flux plot
- The force on a unit of area due to uniform magnetic field:
	$$\frac{f_{m}}{A}=0.5 \frac{B^{2}}{\mu_{0}}$$
	- The structure has two poles so two lots
	- $\mu$ is the primary permeability
	- Total force on armature is $2f_{m}$
## Magnetic Flux and Gauss
- Total flux$=\Phi = \int_{s}B.dA$ 
- Measured in $Wb$ , weber
- If B is uniform and same angle to area: $\Phi = BA$
- Gauss/Flux Law: For any closed region in the magnetic field, the total flux entering the region is equal to the flux leaving
- Permanent Magnet: Instead of using a coil, permanent magnet, materials to create magnetic flux
- Imagine a gauss surface, flux density in steel = flux density in airgap
	- From magnet to pole: 
		- $\Phi = B_{magnet}A_{magnet}=B_{steel}A_{pole}$
	- Flux through airgap would be:
		- $B_{gap}=B_{s}=\frac{A_{m}}{A_{p}}B_m$
	- If the pole area is made smaller than the magnet area, the flux density in the air gap will be greater than the flux in the magnet
		- $f_{t}=\frac{B_{g}^{2}A_{p}}{\mu_{0}}$ 
# Magnetic Field of a Current-Carrying Conductor
- The magnetic flux density at point P due to current in an infinitesimal length of wire is given by the Bio-Savart formula:
$$\mathbf {dB}=\frac{\mu_{0}I}{4\pi R^{2}}\mathbf{dl}sin\theta \longrightarrow B=\frac{\mu_{0}I}{2\pi r}$$
- $B$ is calculated by integrating over the length
- $R, \theta$ are varying over the length
- With finite length, distance r from wire: (angles are the angles from the conductor to the point)
$$\mathbf B=\frac{\mu_{0}I}{4\pi r}(cos\alpha_{2}- cos\alpha_1)$$
- Current loop conductor:
$$B=\frac{\mu_{0}I}{2r}$$
# Ampere's Law
- Magnetic Intensity $H$ is A/m and is $H=\frac{B}{\mu_{0}}$
- The permeability of material $\mu_{r}$ is multiplied by the permeability of the free space $\mu_{r}$ to give $\mu$ 
![[Pasted image 20250728142025.png]]
# Magnetic Field Intensity
- Magnetic intensity of a toroidal core
	- $H=\frac{Ni}{2\pi r}$
# Magnetic Flux Linkage
- The magnetic flux in a cross sectional area:
$$\Phi = BA$$
- The sum of fluxes of each coil is known as flux linkage:
$$\lambda = N\Phi =NAB$$
- If due to shape of coils, the flux of each coil is different:
$$\lambda = \sum\limits \Phi $$
### Inductance
-  The flux linkage is proportional to the current with a linear relationship, where $L$ is in $Henrys (H)$:
$$\lambda = Li$$
- Where $Li$ is the inductance, for the toroidal core we can write:
$$ \Phi =BA\frac{\mu_{0}NiA}{2\pi r_{AV}}$$
### Energy Stored 
- The magnetic energy stored in a inductor is:
$$W=0.5\lambda i = 0.5 Li^{2}$$
# Magnetic Material
- Relative Permeability: If core is wound on a core of magnetic material the flux density and flux will increase and consequently the inductance will increase:
$$L'=\mu_{r}L|\mu_{r}=\frac{B}{\mu_{0}H}$$
- $\mu_r$ is the magnetic field created due to the magnetisation of the material
- Higher core permeability = less flux leakage
### Magnetisation Curve
- If H starts to increase from zero (Point O): B increases (linearly with slope $\mu$) until saturation point $a$
- If H start to decrease from point $a$: B decreases but does not follow previous curve. If H increased to zero B will not be zero (point $b$), due to residual flux, the material is still magnetised
![[Pasted image 20250728145557.png]]
# Magnetic Circuit Analysis
- With air gap:
	- The length of the flux path in core is $l_s$ and the length of the airgap is $l_{g}$.
	- Due to flux law, the flux in the steel core and airgap should be equal:
$$\Phi_{s}\approx \Phi_{g}\therefore B_{S}A_{S}\approx B_{g}A_{g}$$
- Since the two cross sections are equal, so are the $B$s
- Accounts for fringing effect:
$$H_{g}=\frac{B}{\mu_{0}}$$
- If $\mu_{r}\rightarrow  \nfnt$ then $H_{s}\rightarrow 0$
$$i=\frac{H_{s}l_{s}+H_{g}l_{g}}{N}\approx \frac{H_{g}l_{g}}{N}$$
- Since $Ni$ is the driving force in magnetic circuit, it is the magneto motive force (mmf)
$$\mathcal F=Ni\text{ in At}$$
### Reluctance 
- Assuming linear relationship of B-H
$$\mathcal F=\frac{B_{c}l_{c}}{\mu} + \frac{B_{g}l_{g}}{\mu_{0}}=\Phi(\frac{l_{c}}{\mu A_c}+\frac{l_g}{\mu_{0}Ag})$$
- The terms in parenthesis are all the properties and dimension of steel and airgap, this is the reluctance
$$\mathcal F=\Phi(\mathcal R_{c}+ \mathcal R_{g})$$
- $V \rightarrow \mathcal F, I \rightarrow \Phi, R \rightarrow \mathcal R$ (they are similar concepts)
# Magnetic Induction
- Generation of voltage due to conductor carrying magnetic field
	- Motional induction: conductor move in field
	- Transformer induction: field varies around conductor
$$\lambda = N\Phi = NBA - Li$$
- If L is constant: (due to Faraday's)
$$e=L \frac{di}{dt}$$
- If i is constant:
$$e = i \frac{dL}{dt}$$
- Change in L:
$$L=\frac{\mu_{0}N^{2}A}{l}$$
### Mutual Inductance
- If the flux created by current in one coil passes through another coil, they are magnetically coupled. The flux in the second loop is linearly proportional to the current in the first loop:
$$\lambda_{12}=M_{12}i_{2} \text{ and likewise } \lambda_{21}=M_{21}i_{1}$$
- $M$ is the mutual inductance and is equal for both.
- When connected to a voltage generator (battery, etc.)
$$v_{1}= R_{1}i_{1}+L_{i}\frac{di_{1}}{dt}+M\frac{di_{2}}{dt}$$
- Total stored energy is:
$$W_{m}= 0.5L_1i_{1}^{2}+0.5L_{2}i_{2}^{2}+Mi_{1}i_{2}$$
