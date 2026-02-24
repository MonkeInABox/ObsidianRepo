# Slider-Crank
$$r_{p}=r_{2}+r_{3}= r_{1}+ r_{4}$$
$$r_{2}(cos\theta_{2}\mathbf i+sin\theta_{2}\mathbf j)+r_{3}(cos\theta_{3}\mathbf i+sin\theta_{3}\mathbf j) = r_{1}(cos\theta_{1}\mathbf i+sin\theta_{1}\mathbf j)+r_{4}(cos\theta_{4}\mathbf i+sin\theta_{4}\mathbf j)$$
- Solution to Position Equations when $\theta_2$ is Input
	- Isolate $r_{3}cos\theta_{3}$ i's and $r_{3}sin\theta_{3}$ for j's
$$r_{3}^{2}(cos^{2}\theta_{3}+sin^{2}\theta_{3})=(r_{1}cos\theta_{1}+r_{4}cos\theta_{4}-r_{2}cos\theta_{2})^{2}+(r_{1}sin\theta_{1}+r_{4}sin\theta_{4}-r_{2}sin\theta_{2})^{2}$$
$$\theta_{3}=tan^{-1}\frac{r_{1}sin\theta_{1}+r_{4}sin\theta_{4}-r_{2}sin\theta_2}{r_{1}cos\theta_{1}+r_{4}cos\theta_{4}-r_{2}cos\theta_2}$$

# Inverse Kinematics
- The kinematics problem is vector $X$ that describes orientation and position of end effector $$X=\Phi(q)$$
- Vector enclosure equation $$\mathbf r_{E}=\mathbf r_{1}+...+\mathbf r_{n}$$
- So for a 6 DOF System: $$X=\begin{bmatrix} X_{E}\\Y_{E}\\Z_{E}\\ \Phi \\ \theta \\ \gamma \end{bmatrix},q=\begin{bmatrix} \theta_{1}\\\theta_{2}\\\theta_{3}\\ \theta_{4} \\ \theta_{5} \\ \theta_{6} \end{bmatrix}$$
- In component form: $$X=R_{1}cos\theta _{1}+R_{2}cos(\theta_{1}+\theta_{2}), Y=R_{1}sin\theta _{1}+R_{2}sin(\theta_{1}+\theta_{2})$$
- Cancelled: $$X^{2}+Y^{2}=l_{1}^{2}+l_{2}^{2}+2l_{1}l_{2}c_{2}$$
# Jacobian
- The Jacobian is the partial derivative of the left hand side of the constraint equations with respect to the generalised coordinates
- For slider crank mechanism: $$\lfloor\begin{bmatrix} \frac{\delta constant X}{\delta \theta_{2}} & \frac{\delta constant X}{\delta \theta_{3}} & \frac{\delta constant X}{\delta X_{c}} \\ \frac{\delta constant Y}{\delta \theta_{2}}& \frac{\delta constant Y}{\delta \theta_{3}} & \frac{\delta constant Y}{\delta X_{c}}\end{bmatrix} \rfloor$$
- Number of rows = number of constraint equations
- Number of columns = number of generalised coordinates
