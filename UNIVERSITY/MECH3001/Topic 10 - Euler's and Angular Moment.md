# Angular Momentum
- Consider a rigid body moving with any general motion in space
- Axes $x-y-z$ are attached to the body with origin at the mass centre $G$, $\omega$ is the angular velocity of the body as observed from $X-Y-Z$ 
- $H_{G}=\sum (\rho_{i}\times m_{i}v_{i})$
- $H_{O}=\int [r\times (\omega \times r)]dm$
$$I_{xx}= \int (y^{2}+ z^{2})dm, I_{xy}= \int xy dm$$
$$I_{yy}= \int (z^{2}+ x^{2})dm, I_{xz}= \int xz dm$$
$$I_{zz}= \int (x^{2}+ y^{2})dm, I_{yz}= \int yz dm$$
$$H_{x}=I_{xx}\omega_{x}-I_{xy}\omega _{y}- I_{xz}\omega_{z}$$
$$H_{y}=-I_{yx}\omega_{x}+I_{yy}\omega _{y}- I_{xz}\omega_{z}$$
$$H_{z}=-I_{zx}\omega_{x}-I_{zy}\omega _{y}+ I_{zz}\omega_{z}$$
# Principal Axes
- The array of the moments and products of inertia is the inertia matrix or the inertia tensor
- There is one unique orientation of the axes for a given origin for which the products of inertia vanish and the matrix becomes diagonalised
- These are the principal axes, giving the minimum, maximum and intermediate values of the moments of inertia
# Transfer Principle for Angular Momentum
- Although $H_G$ is the vector about the mass centre and has the properties of a free vector, we represent it as $G$
- About point $P$: $$H_{P}=H_{G}+\bar r \times G$$
# Kinetic Energy
$$0.5mv^{2}=0.5 m\dot{r}.\dot{r}=0.5 \bar v.G$$
- For a rigid body, the relative term becomes kinetic energy due to rotation about the mass centre $$\dot \rho_{i}=\omega \times \rho_{i}$$$$\sum 0.5 m_{i}|\dot{\rho}|^{2}=\sum0.5m_{i}(\omega \times \rho_{i}).(\omega \times \rho_{i})=0.5\omega . H_G $$$$T=0.5\bar{v}.G+0.5\omega . H_{G}$$
- When pivoted about a fixed axis $O$ or point in body which momentarily has zero velocity$$T=0.5\omega . H_{0}$$
# Momentum and Energy Equations of Motion
$$\sum F=\dot G, \sum M = \dot H$$
$$\sum M_{x}=\dot{H}_{x}- H_{y}\omega_{z}+H_{z}\omega_{y}$$
$$\sum M_{y}=\dot{H}_{y}- H_{z}\omega_{x}+H_{x}\omega_{z}$$
$$\sum M_{z}=\dot{H}_{z}- H_{x}\omega_{y}+H_{y}\omega_{x}$$

# Gyroscopic Grinding Mills
## Edge Mills
- A gyroscopic grinder used for crushing ore, seeds, etc
- Uses mullers to roll on the bottom of the pan and revolve about a vertical shaft
- Mullers are heavy flywheels with thick rims
![[Pasted image 20251001072240.png]]
$$\frac{\Phi}{sin(\theta-\alpha)}=\frac{\Omega}{sin\alpha}$$
$$M = Wlsin(\theta)+\Omega^{2}(Ccot\alpha sin^{2}\theta - 0.5Asin2\theta)$$
## Griffin Grinding Mill
- Grinds by intense pressure due entirely to gyroscopic action done by a pendulous cylinder attached to a vertical shaft by a Hooke or universal joint