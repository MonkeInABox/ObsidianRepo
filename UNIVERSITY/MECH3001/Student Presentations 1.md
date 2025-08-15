# 1 Ferris Wheel
Modelling motion with diameter and period
Angular velocity, tangential velocity and centripetal 
Using generalised coordinates
$\theta$ and $\phi$ are the two coordinates, the angle of wheel and swing of cabin
These are independent
From the perspective of the gondola, a centrifugal force is experienced
Generalised coords + principle of virtual work = sufficient to provide study for real world systems with rotating parts and motion
# 2 Robot
Holonomic systems the constraints are integrable with respect to time
Two control inputs (left and right wheels)
3 DOF however, assume without slipping
Delta robots, 3 DOF - highly constrained as keeps in same orientation
UR5e robot - 6 DOF
Non holonomic because the hips need to move to adjust for other movement 
# 3 Astrobee
Implications of holonomicity: instant and independent movement in all generalised coordinates
- 6 DOF, with instantaneous thrust in any direction, same as generalised coordinates, so holonomic
Quadcopter drones, thrust generated downwards, diagonal motor pairs rotate in same direction
- For movement, roll, greater upwards thrust on one side than other
- One pair slowed on sped up to yaw
- 6 DOF, 4 independent
- Constrains lateral movement
Astrobee would need more thrust to work in atmosphere + not aerodynamic
Drones not used in ISS due to non-holonomic motion, causing issue in confined spaces and impractical fan control without gravity
# 4 Minimum Potential Energy
Virtual displacement is an infinitesimal imagined movement
- When considering all displacements that follow the constraints of a system, a body in equilibrium 
- Virtual work -> external potential energy, summation of change in ext potential and internal strain is 0, which is the minimum potential energy
- To find system stable point, then from x=0 to equilibrium how much lost potential energy
# 5 Foucault's Pendulum
- Proves Earth is rotating
- Forces of a pendulum gravity and the force of the pendulum arm
- Observer outside rotation of earth, only 1 DOF, the angle $\theta$ 
	- Complete and independent, angle changes with time
- No velocities therefore it is holonomic
- Intensity of twisting effect depends on latitude angle
- D'Alembert's principle introduces inertial force to virtual work to allow a description of this movement
# 6 Kaleidocycles 
- Mobility is number of independent input to control configuration of system
- Equation cant be wrong but can be contrary to expectations (special geometry or internal mobility), combine revolute joints along parallel axis. 
- Kaleidocycle: Symmetry around 3 axes, it gets an extra degree of motion. Mobius kaleidocycle has always 1 degree of freedom
# 7 ?
- Special geometries allow for parallel members to be treated as one link
- Precise manufacturing is needed for a structures that are over constrained so they can still move, adds more stability, better load distribution
- Issues with 3D equation is that it assumes it can move in all 6 freedoms, therefore can model constraints that the mechanism does not have
# 8 !?
- Slider crank turning rotary motion into linear reciprocating motion, transforms into 1 DOF
# 9 its the same shit idk
- Degree of constraint = 1 - m
- To simplify to remove constraints: mechanisms with links running parallel, joints in series acting on different planes, multiple joints acting in the same plane
# 10 