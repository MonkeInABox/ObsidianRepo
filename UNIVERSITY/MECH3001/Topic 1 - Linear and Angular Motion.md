# Coordinate Systems
## Rectangular Coordinates
- Good when x and y components are independently determined
#### Vector Representation
$$r=xi+yj, v = \dot{r}, a = \dot{v}$$
- We know:
$$v^{2}= v_{x}^{2}+ v_{y}^{2}, v = \sqrt{v_{x}^{2}+ v_{y}^{2}}, tan\theta =\frac{v_{y}}{v_{x}}$$
	- and similar for $a$
#### Projectile Motion
$$v_{x}=v_{x0}, v_{y}= v_{y0}-gt$$
$$x=x_0+v_{x0}t, y = y_{0}+v_{y0}t-0.5gt^{2}$$
$$v^{2}_{y}=v_{y0}^{2}-2g(y-y_{0})$$
- These equations work at each point for the parabolic projectile motion
## Normal and Tangential Components (n-t)
- Positive direction of n at any position is always taken toward the centre of the curvature
- Introduce unit vector $e_{t}$
- Radius of curvature is $\rho$ with $ds = \rho d\beta$
$$\mathbf{v}=ve_{t}=\rho\dot{\beta}e_{t}$$
$$\mathbf{a}=\frac{v^{2}}{\rho}e_{n}+\dot{v}e_{t} | a_n=\frac{v^{2}}{\rho}$$
## Circular Motion
$$v_{r}=\dot r, v_{\theta}=r\dot{\theta}, a_{n}=\frac{v^{2}}{r}=r\dot{\theta}\dot{\theta}$$
$$a_{r}=\ddot r - r \theta ^{2}, a_{\theta}=r \ddot \theta + 2\dot r \dot \theta$$
## Polar Coordinates (r-$\theta$)
- Position vector $\mathbf{r}$
$$\mathbf{r}=r\mathbf{e_r}$$
$$\dot{\mathbf{e}}_{r}=\dot{\theta}\mathbf{e_{\theta}}, \dot{\mathbf{e}}_{\theta}=-\dot{\theta}\mathbf{e_{r}}$$
$$\mathbf{v}=\dot{r}\mathbf{e_{r}}+r\dot{\theta}\mathbf{e_{\theta}}$$
$$a=(\ddot{r}-r\dot{\theta}^{2})\mathbf{e}_{r}+(r\ddot{\theta}+2\dot{r}\dot{\theta})\mathbf{e}_{\theta}$$
$$a_{r}=\ddot{r}-r\dot{\theta}^{2}, a_{\theta}=r\ddot\theta+2\dot{r}\dot\theta$$
# Forces, Impulse and Momentum
## Linear Impulse and Momentum
$$\Sigma F=m\dot{v}=\dot{G}$$
- Where G is the linear momentum $G=mv$ in $Ns$ or $kgm/s$ 
## Angular Impulse and Momentum
$$\mathbf{H}_{O}=\mathbf{r} \times m\mathbf v$$
- Where H is angular momentum
## Momentum of Point Mass
$$\vec p = mv, F=\frac{d}{dt}\vec p$$
$$\vec F = \vec{0} \implies \vec P = const$$
- This is the momentum conservation principle
# Newton's Laws
1. No forces $\implies$ constant $v$, there exists an inertial coordinate system for which we can write first law (valid only in inertial coordinate system (not rotating and no accelerating))
2. $\vec a \propto \vec F \implies m\vec a = \vec F$
3. Reaction = - Action
# Equivalence of Inertial and Gravitational Mass
$$F =ma  \text{     vs.     } G = Mg$$
- The equivalence principle
	- *It's a MYSTERY~~~ in classical physics*

# Spring System Example
- box (m) with spring (k) pushing against wall
$F_x$ acts on the box
- Its shape doesn't affect our analysis, therefore we can treat it as a point mass
$$\vec F=m\vec a$$
$$\rightarrow ^{+}F_{x}=ma_{x}=m \ddot x = -kx$$
$$\ddot x = \frac{-kx}{m} \longleftarrow \text{this is a differential eq}$$
- Initial condition $\rightarrow x_{0} = 0, v_{0} =0$
$$x(t) =x_{0}cos(\omega t) + \frac{v_{0}}{\omega}sin(\omega t) | \omega = \sqrt\frac{x}{m}$$
$$\dot x = -x_{0}\omega sin(\omega t) + v_{0}cos(\omega t)$$
$$\ddot x = -x\omega ^ {2}cos(\omega t) + v_{0}\omega sin(\omega t)$$
$$m\ddot x = -kx_{0}cos(\omega t) - v_{0}\sqrt{km}sin(\omega t)$$
$$m\ddot x = -k(x_{0}cos(\omega t) + \frac{v_{0}\sqrt{km}}{k}.sin(\omega t))=-kx | x(t) = x_{0}cos(\omega t)+\frac{v_0}{\omega}sin(\omega t)$$
