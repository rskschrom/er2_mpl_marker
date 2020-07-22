import numpy as np
from matplotlib.path import Path

# plane path
def make_plane(rot_ang):
    # create plane dimensions
    l = 1.
    lw = 0.25*l
    lt = 0.15*l
    ln = l-lw-lt
    w = 0.6*l
    wt = 0.3*w
    wn = 0.25*w
    ww = 0.15*w

    # create plane vertices
    v1 = (0., l)
    v2 = (wn, l-ln)
    v3 = (w-wn, lt+0.55*lw)
    v4 = (w, lt+lw)
    v5 = (w, lt)
    v6 = (0.6*wt, lt)
    v7 = (wt, 0.)

    v8 = (-wt, 0.)
    v9 = (-0.6*wt, lt)
    v10 = (-w, lt)
    v11 = (-w, lt+lw)
    v12 = (-w+wn, lt+0.55*lw)
    v13 = (-wn, l-ln)

    # create polygon path and rotate
    verts = [v1, v2, v3, v4, v5, v6, v7, v8,
             v9, v10, v11, v12, v13, v1]
    xv = np.array([v[0] for v in verts])
    yv = np.array([v[1] for v in verts])
    xv = xv-np.mean(xv)
    yv = yv-np.mean(yv)
    xvr = xv*np.cos(rot_ang/180.*np.pi)-yv*np.sin(rot_ang/180.*np.pi)
    yvr = xv*np.sin(rot_ang/180.*np.pi)+yv*np.cos(rot_ang/180.*np.pi)

    np_verts = np.vstack((xvr, yvr)).T

    pplane = Path(np_verts)
    return pplane
