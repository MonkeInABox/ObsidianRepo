## Kinematics
- Study of position and its time derivatives. Specifically we are concerned with the $p, v, a$ 0f a point and likewise for angular
## Mechanisms
- Assemblages of solid members connected by joints
![[Pasted image 20250812135919.png]]
- A lower pair joint is one in which contact between two rigid members occurs over geometrically congruent surfaces (low contact stresses)
- High pair joint occurs only at isolated points or along line segments
- Number of degrees of freedom (connectivity) of a joint is the minimum number of independent parameters required to define the positions of all points in one of the bodies it connects
## Constraint Analysis
- DoF is the number of independent coordinates needed to specify uniquely the position of that body relative to a given reference frame
- In a plane, a moving body has 3 degrees of freedom, in a given linkage there are $n$ links, if they all are free to move independently the mobility is $3n$. If one link is chosen as the frame link, it loses all it's DoF, therefore total mobility is $3(n-1)$ with no joints found between the members.
![[Pasted image 20250812141415.png]]
## Constraint Analysis of Spatial Linkages
- The constraint criterion equation \[the Kutzbach Criterion]
$$\mathbf M = 6(n-j-1)+\sum^{j}_{i=1}f_{i}$$
![[Pasted image 20250812142201.png]]
- Closures $c$ 
$$\mathbf M = \sum^{j}_{i=1}f_{i}-6c$$
	- When a closure is formed, the number of members does not increase, but the number of joints increases by one
$$c=j+1-n$$
## Idle Degrees of Freedom 
- A degree of freedom that does not affect the input-output relationship of the linkage
- 