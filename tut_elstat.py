import matplotlib.pyplot as plt
import numpy as np
'''
define numerical values of physical constants
kc:type real:units [Nm^2/C^2]:phys Coulomb constant 1/(4pie0)
'''
kc = 8.99 * 10**9


class charge:

    def __init__(self, q, pos):
        self.q = q
        self.pos = pos


def v_point(q, a, rx, ry, rz=0):
    """Return the electric Coulomb potential at a point in space due to a point charge.

    input:
    q : type real : units [C] : phys charge
    a : type list : units [m,m,m] : phys position of the charge
    rx, ry, rz : type real : units [m] : phys position where the potential is calculated
    """
    return kc * q / np.sqrt((rx - a[0])**2 + (ry - a[1])**2 + (rz - a[2])**2)

def e_point_xy(q, a, rx, ry):
    """Return the electric field at any point on the XY plane due to a point charge.
    input:
    q : type real : units [C] : phys charge
    a : type list : units [m,m,m] : phys position of the charge
    rx, ry: type real : units [m] : phys position where the field is calculated
    """
    r = np.sqrt((rx - a[0])**2 + (ry - a[1])**2)
    ex = (kc * q * (rx - a[0])) / r**3 #if r != 0 else 0
    ey = (kc * q * (ry - a[1])) / r**3 #if r != 0 else 0
    return np.array([ex, ey])

def e_pointsum(x, y, charges=[charge(-1, [0, 0, 0])]):
    """Return the x and y components of the total electric field at some point on the XY plane
    input:
    charges:type list<charge>:units [C,m,m]:phys defines the object as a set of point charges
    x,y    :type real,real   :units [m]    :phys cartesian coordinates in space
    """
    Ex, Ey = 0, 0
    for C in charges:
        E = e_point_xy(C.q, C.pos, x, y)
        Ex += E[0]
        Ey += E[1]
    return np.array([Ex, Ey])

def v_pointsum(x, y, z=0, charges=[charge(-1, [0, 0, 0])]):
    """Return the total potential

    input:
    charges:type list<charge>:units [C,m,m]:phys defines the object as a set of point charges
    x,y    :type real,real   :units [m]    :phys cartesian coordinates in space

    output:
    vtot   :type real        :units [V=J/C]:phys electrostatic potential 
    """

    vtot = 0
    for C in charges:
        Vp = v_point(C.q, C.pos, x, y, z)
        vtot += Vp
    return vtot


# suggestions for charge configurations
## ring of charges in the xy-plane (z=0)

nbr = 3
rho = 2
rhoscale = 4.
zshift = 0.0

qq = 2

ring_charges_z0 = [
    charge((+1)**nn*qq, [
        rhoscale*rho * np.cos(2*np.pi / nbr * nn),
        rhoscale*rho * np.sin(2*np.pi / nbr * nn),
        -zshift
    ]) for nn in range(nbr)
]

ring_charges_z1 = [
    charge(-qq, [
        rho * np.cos(2*np.pi / nbr * nn),
        rho * np.sin(2*np.pi / nbr * nn),
        zshift
    ]) for nn in range(nbr)
]

## a number of charges randomly placed within a 2d rectangular sheet parallel to the xy plane

n_random = nbr
x0, x1 = -2 * rho, 2 * rho
y0, y1 = -2 * rho, 2 * rho
x_random = np.random.uniform(low=x0, high=x1, size=n_random)
y_random = np.random.uniform(low=y0, high=y1, size=n_random)
z_random = [zshift for _ in range(n_random)]

random_charges = [charge(qq, [x, y, z]) for x, y, z in zip(x_random, y_random, z_random)]

## 2 point charges

dipole_charges = [
    charge(-qq,  [0, zshift,0]),
    charge(qq, [0, -zshift,0])
]
# combine charge distributions
charges = ring_charges_z0

# plot boundaries
x0, x1 = -15 * rho, 15 * rho
y0, y1 = -15 * rho, 15 * rho
z0, z1 = -15 * rho, 15 * rho

# plot resolution
numcalcv = 50
nbrofplanes = 5

X, Y = np.meshgrid(np.linspace(x0, x1, numcalcv),
                   np.linspace(y0, y1, numcalcv),)

zplanes = np.linspace(1, 15, nbrofplanes)

vContours = [ v_pointsum(X, Y, zplane, charges) for zplane in zplanes]

levels = np.linspace(np.min(vContours[0]), np.max(vContours[0]), numcalcv)

efield = e_pointsum(X, Y, charges)


# 3D surface plot

qcol = ['r' if C.q > 0 else 'b' for C in charges]
lcol = 2 * np.log(np.hypot(efield[0], efield[1]))

fig = plt.figure(figsize=(15, 15*(nbrofplanes+1)))



for nn in range(nbrofplanes):
    ax1 = plt.subplot(nbrofplanes+1,1, nn+1)
    ax1.contourf(X, Y, vContours[nn], levels=nn+levels, cmap='RdGy')
    ax1.set_title(f"electrostatic potential in the z={zplanes[nn]} plane",fontsize=15)
#ax1.scatter(*zip(*[C.pos[:2] for C in charges]), c=qcol, marker='o', s=150)
#ax1.plot_surface(X, Y, vContour, alpha=0.5, linewidth=0.3, edgecolor='black')
#ax1.scatter3D(*zip(*[C.pos for C in charges]), c=qcol, s=150)
#ax1.set_zlabel(f'V(z={zplane})', labelpad=10, fontsize=22,color='blue')

ax1.set_xlabel('X', labelpad=20, fontsize=22,color='blue')
ax1.set_ylabel('Y', labelpad=20, fontsize=22,color='blue')

ax2 = plt.subplot(nbrofplanes+1, 1, nbrofplanes+1)
ax2.streamplot(X, Y, efield[0], efield[1], density=2.0, linewidth=1.0,color=lcol, arrowsize=1.5)
ax2.scatter(*zip(*[C.pos[:2] for C in charges]), c=qcol, marker='o', s=150)
ax2.set_xlabel('X', labelpad=20, fontsize=22,color='blue')
ax2.set_ylabel('Y', labelpad=20, fontsize=22,color='blue')
ax2.set_title(f"electric field $E=(E_x,E_y)$ in the z={zplanes[0]*0} plane",fontsize=15)

fig.tight_layout(pad=0.5)

plt.savefig('el_pot.png', dpi=250, bbox_inches="tight", pad_inches=0.02)

plt.show()