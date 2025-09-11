# Classification of Mechanical Systems
$$x_{v}= x_{v}(q_1....q_{n}, t), y_{v}= y_{v}(q_1....q_{n}, t), z_{v}= z_{v}(q_1....q_{n}, t) [2]$$$$\mathbf r_{v}=\mathbf r_{v}(q1, ..., q_{n}, t)[3]$$
## Scleronomic and Rheonomic Systems
- Scleronomic systems occur when time $t$ does not enter explicitly in the equations $(2) or (3)$
	- Like a cylinder rolling without slipping
- In others where moving constraints occur, are rheonomic
	- Like a particle moving on a very long frictionless wire which rotates at constant angular speed about horizontal axis
## Holonomic and Non-holonomic
- If all the constraints can be expressed as some amount of the generalised coordinates is equal to zero, it is holonomic
# Lagrange's Equations
- Generalised force can be related to KE $$\frac{d}{dt}(\frac{\delta T}{\delta\dot{q_{a}}})-\frac{\delta T}{\delta q_{a}} = \phi _{a}$$
	- Where $q$ is the generalised velocities
- If $L=T-V$ $$ $$$$\frac{d}{dt}(\frac{\delta L}{\delta\dot{q_{a}}})-\frac{\delta T}{\delta q_{a}} = 0$$
	- This is the Lagrangian function of the system, which are valid for holonomic systems
## For non-holonomic systems
 $$\frac{d}{dt}(\frac{\delta T}{\delta\dot{q_{a}}})-\frac{\delta T}{\delta q_{a}} = \phi _{a}+\lambda_{1}A_{a}+...$$
 - Where $\lambda$ are the Lagrange multipliers
 - If conservative then like above, the $T$s can be swapped with $L$s and $\phi_a$ as 0
# Reduction of Kinematics to Statics
- If we consider the negative product of mass $m$ and acceleration $a$ formally as a force called d'Alembert's inertial force $F_{1}=-ma$$$F+F_{1}=0$$
- This is a fictitious force
- The dynamic equilibrium conditions $$F_{x}+F_{1x}=0, F_{y}+F_{1y}= 0, M_{C}+ M_{1C}= 0$$
## D'Alembert's Principle
- Motion of point mass according to Newton's laws $$ma = F + F_{2}$$
- Where $F$ is the applied force and $F_{2}$ is the constraint force
- Since the constraint forces are perpendicular to the path and consequently to $\delta r$: $$F_{2}.\delta r=0$$
	- This is Camemberts principle
> The motion of a point mass takes place such that the sum of the virtual works of the applied forces and d'Alembert's inertial force vanishes at all times

$$\delta U+\delta U_{1}= 0$$
# Lagrange Equations of the Second Kind
- Number of degrees of freedom $f$ of a system of $n$ point masses in space, subjected to $r$ kinematic constraints is $f=3n-r$ (3 is 2 in a plane)
- Lagrangian of a conservative system can be expressed as
$$L=T-V=0.5ml_{0}^{2}(\dot{q_{1}^2}+q_{1}^{2}\dot{q_{2}^2})-0.5kl^{2}_{0}(q_{1}- 1)^{2}+mgl_{0}q_{1}cosq_{2}$$
