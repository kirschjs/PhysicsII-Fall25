# lecture:
1) Where does the theory come from? Which observations/experiments demanded it?  
    - $\frac{1}{r}$ from the force measurement between _cat-fur-charged_ spheres __and__ who did it? Faces, names, places, and anecdotes!

2) What motivated xyz to think about the problem, what tools were at his/her disposal, and what did s/he gain?  
    - development of precise time measurements as means in naval navigation 

3) What are limitations and where does the theory give way to different models of nature?  
    - What if we decrease the distance between charges? $\Rightarrow$ QED
    - What if we increase the distance? What is the E&M force acting between black holes?
    - What law governs moving charges?

# lab (theory tutorials):
The basic philosophy is based on the almost-too-obvious-to-spell-out understanding of the __AI companion__
as the _calulator_ or _abacus_ or _pancil_ or _mentor_ of our days!  
And as we did not ask for solutions to problems of the kind:

_Calculate the numerical value of the potential energy between two electrons with charge e each placed a distance R apart!_
  
we should not ask, today:

_Two identical conducting spheres, fixed in
place, attract each other with an electrostatic force of 0.108 N when
their center-to-center separation is 50.0 cm. The spheres are then
connected by a thin conducting wire. When the wire is removed,
the spheres repel each other with an electrostatic force of 0.0360 N.
Of the initial charges on the spheres, with a positive net charge,
what was (a) the negative charge on one of them and (b) the posi-
tive charge on the other? (Problem 9 in Fundamentals... ch. 21)_
  
which, if pasted to, e.g., the MS copilot, is solved as satisfactorily
as the number the prehistoric calculator displayed.  

We present __open-ended__ problems which require the straightforward employment of the lecture's
concepts but are impossible to solve within the time constraints of the course and which also allow for the
exploration of various avenues.

``All theory is gray $\Rightarrow$ project into the binary reality''  

## Tutorial week 1 (electrostatic potentials)

1. Split the students into triplets or quartets.  
    Each group must have access to a laptop/computer with a working python environment that is able to execute the following snippet:  
    ```python
    import matplotlib.pyplot as plt
    import numpy as np
    ```


1. Instead of setting the student's goal, I let them choose it:  

    _A charged projectile is incoming from the infinite distance, and your aim is to alter its trajectory by constructing a
    3-dimensional, localized, and charged object with an electrostatic field conducive to that aim.
    <font color="red">Formulate a concrete goal of how you want to change the trajectory!</font>_  

    What comes to my mind, i.e., suggested directions:  

    - [ ] deflect an incoming bullet
    - [ ] deflect an incoming bullet into a specific direction (e.g. reflect it back to its source)
    - [x] trap a charge

1. <font color="red">_Conjecture a geometry which you expect to induce the desired effect._</font>
    
    As I am interested in a trap, I would guide the students--if help is needed at all--by spelling out my own thoughts that
    are oriented by the classical analog:  
    _"How would we realize the analogue of a deep well? What characterizes the shape of the well?"_ __A pronounced minimum.__  
    It cannot be a closed cave, and neither a uniform attractor which would "glue" the projectile; we want to trap it in space as
    a "free" object.  

    $\curvearrowright$ place charges with alternating signs at the corners of a cube (essence of a so-called Paul trap)

    Another analogue way of thinking about the problem is to map it onto a 2-dimensional stretched canvas
    ([Feynman](https://www.feynmanlectures.caltech.edu/II_12.html)).

1. Represent the charge distribution as a collection of _discrete_ charges in space and find the Cartesian coordinates
    as a function of the particles index. This is a tricky part, and the simplicity for the coded example, i.e. the ring:
    ```python
    ring_charges_z0 = [
    charge(qq, [
        rho * np.cos(2*np.pi / nbr * nn),
        rho * np.sin(2*np.pi / nbr * nn),
        0.0
    ]) for nn in range(nbr)
    ]
    ```
    Should not obfuscate the challenge for less geometrically-thinking individuals.

1. As trivial as it might be, every group must have on paper the explicit formula for the potential:
    $$V_{\text{total}}(\vec{r})=k\sum_{n=1}^{nbr}\frac{q_n}{\vert\vec{r}-\vec{r}_n\vert}=\ldots\qquad.$$
    Here, the expression of the cartesian coordinates as a function of the particle label $n$ pays off!  
    Also, I deem this an __important__ moment to bring the hardly-to-underestimate importance of the superposition
    principle to the attention of the audience.

1. visualize in 2 dimensions as a warmup but write your code such that it can be recycled for the general, 3-dimensional case.

## Tutorial week 2 (electrostatic field/force)

We visualized the scalar function of the electrostatic potential resulting from a distribution of charges
in 3-dimensional space last week. We chose to characterize the charge's potential field by a contour map of
its magnitude in a 2-dimensional plane.  
You should have realized at least one problem if such a representation is interpreted too naively, namely, that
even if a potential minimum is plot at some $xy$ coordinate, the corresponding 
$\vec{r}=\begin{pmatrix}x,y,z\end{pmatrix}^\intercal$ is, in general, no attractor of the motion.  
To obtain a much better insight from a graph, we should encode the potential's strength not in 2 but in 3  
dimensions. As the, e.g., $z$ direction would then no longer indicate the magnitude of $V_{\text{total}}$ but
the third spatial dimension, that magnitude needs to be represented differently.

- [ ] Idea I: 
    - discretize space $\curvearrowright$ 3D grid of points.
    - make the color of each point represent $V_{\text{total}}$ $\curvearrowright$ "density plot".
- [x] Idea II: 
    - discretize space $\curvearrowright$ 3D grid of points. For instance, 
    $\vec{n}=(i,j,k)=i\cdot\hat{e}_x+j\cdot\hat{e}_y+k\cdot\hat{e}_z$ with cartesian "lattice" basis
    vectors $\hat{e}$ whose length quantifies the granularity of our space, $\vert\hat{e}\vert=:a$, and the
    size of the plotted volume is set by the range of $\vec{n}$, i.e.,
    $i,j,k\in\lbrace 1,\ldots,n_{\text{max}}\rbrace$.
    - draw __one__ arrow from each point in the direction of that neighboring point whose potential differs
    most from it: $\vec{E}(\vec{n})=\max_m\left\vert V_{\text{total}}(\vec{n})-V_{\text{total}}(\vec{m})\right\vert$, where $\vert\vec{m}-\vec{n}\vert<\sqrt{3}\,a~$ (why?).

With _idea II_, we have encountered a _vector field_ with the intuitive interpretation the the direction indicated at
each point would be that which a test charge placed there would take if released: "Motion towards the steepest 
descend."

# lab (experiments):