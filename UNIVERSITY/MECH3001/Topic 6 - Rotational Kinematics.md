## Time Derivatives in Rotating Reference Frames
- A threshold concept
- If all rotations are always in the same direction, then finite rotations can be treated as vectors
## Derivative in a Rotating Coordinate System
- Rock rotating at $\hat\omega$ about a fixed coordinate system and there is an ant on the rock
- We want to find the total change in position and velocity of the ant, over a small time increment
- **Situation 1**
	- The rock is not rotating, but the ant is walking on the rock
	- Here, $\Delta \mathbf r$ is a small change in position of the ant w.r.t. the rock
	- Change in position: $$\frac{\delta \mathbf r}{\delta t}|_{asifrocknotrotate} = \frac{\Delta \mathbf r}{\Delta t}$$
	- Where, $\delta / \delta t$ signifies a small change of a vector w.r.t. time
- **Situation 2**
	- We will now consider the situation where the rock is rotating and the ant is not moving
	- $\mathbf R$ to show the position is w.r.t. the fixed coordinate system and the $\Delta \mathbf R$ is due to the rotation of the rock only
	- We can see that $\Delta R \approx \Theta R$ as due to the small angle, the length $\Delta R$ is a straight line
	- And in a simple 2D situation, $\Delta R \approx \omega . \Delta t . R$ 
	- The derivative of any vector is composed of two parts: the change in magnitude as if the axis is not rotating, and the change due to the axis rotating
	- $\frac{d\mathbf A}{dt} = \frac{\delta \mathbf A}{\delta t} + \mathbf \omega x \mathbf A$ 
	- The fixed coordinate is $[X, Y, Z]$ and the local coordinate system attached to the rock is $[x,y,z]$ rotating at $\mathbf \omega$ 
	- A vector $\mathbf A$ is described described relative to the rotating coordinate system but the time derivative must be expressed relative to a global or fixed coordinate system
## Summary
- Motion of Point (OXYZ) with respect to OXYZ
	- Position vector $\mathbf R (t)$ 
	- Velocity vector $\mathbf v = \frac{d\mathbf R}{dt}$
	- Acceleration $\mathbf a = \frac{d^{2}\mathbf R}{dt^{2}}$
- Motion of Point (oxyz) with respect to OXYZ
	- Position vector $\mathbf R (t) = \mathbf R_{0} (t) + \mathbf r (t)$ 
	- Differential Operator $\frac{d}{dt} = (\frac{\delta}{\delta t})_{rel}+\omega$
	- Velocity Vector $\mathbf v = \frac{d \mathbf R_{0}{dt}}+ \mathbf v_{rel} + \mathbf \omega \times \mathbf r$
	- Acceleration Vector $$\mathbf a = \frac{d^{2}\mathbf R_{0}}{dt^{2}} + \mathbf a_{rel} + 2\mathbf \omega \times \mathbf v_{rel}+ \mathbf  \omega ' \times \mathbf r + \mathbf \omega \times (\mathbf \omega \times \mathbf r)$$
