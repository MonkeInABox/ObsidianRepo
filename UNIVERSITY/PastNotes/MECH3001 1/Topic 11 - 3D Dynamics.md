# Gyroscopic Motion: Steady Precession
- Gyroscopic motion occurs whenever the axis about which a body is spinning is itself rotating about another axis
- With a mounting in gimbal rings, the gyro is free from rotation of the structure to which it is attached, allowing to be free from external moments
- With the addition of a pendulous mass to the inner gimbal ring, the earth's rotation causes the gyro to precess so that the spin axis will always point north
![[Pasted image 20251007113252.png]]
- $\Omega$ is the precession velocity and precession axis, $p$ is the spin axis, $M$ is the torque axis
$$M = I\Omega p, \mathbf M =I\Omega \times \mathbf p$$
- Assume spin is large and precession is small generally
- The spin axis makes an angle of $\theta$ with the vertical z-axis around which precession occurs $$d\psi = \frac{M_{0}dt}{Ipsin\theta} | M_{0}= mgrsin\theta$$$$\Omega = \frac{gr}{k^{2}p}$$
$$H_{x}=I_{xx}\omega_{x}=I_{0}\dot{\theta}, H_{y}=I_{yy}\omega_{y}=I_{0}\dot{\phi}sin\theta, H_{z} =I_{zz}\omega _{z}=I(\dot{\phi}cos\theta + p)$$
![[Pasted image 20251007115412.png]]
- When rotor precesses at a steady rate $\dot\psi = const$, $\theta = const$, $p = const$, the $y, z$ components of $M$ become $0$
# Gyroscopic Action in Rotating Bodies
![[Pasted image 20251007115907.png]]
- $C$ is the moment of inertia of the gyro about its axis of spin
- Rolling is most common form of motion for a ship
- $\alpha$ is the angle the ship's mast makes with the vertical at time $t$, $\Phi$ is the maximum numerical value of $\alpha$: $\alpha = \Phi sin \beta$
	- $\beta$ is an auxiliary variable such that $\beta = 0.5\pi$ when $\alpha = \Phi$ $$\frac{d\alpha}{dt}=\Phi cos \beta \frac{d\beta}{dt}$$
- The period $T$ is given by $T= \frac{2\pi}{\frac{d\beta}{dt}} \therefore \frac{d\beta}{dt}= \frac{2\pi}{T}$
- $K = C\Omega \omega = \frac{2\pi\Phi C\omega}{T}$ 
- 