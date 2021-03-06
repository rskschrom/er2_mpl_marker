# er2_mpl_marker

The function `make_plane` within `plane_path.py` creates a Matplotlib `Path` object in the shape of the [NASA ER2 aircraft](https://www.nasa.gov/centers/armstrong/aircraft/ER-2/index.html). Requires Matplotlib and Numpy.

## Usage:

```python
plane_path = make_plane(rot_ang)
```

where `rot_ang` is the desired rotation angle (in degrees) of the aircraft marker. One can then use this path as a marker in a Matplotlib plot with

```python
ax.plot(x, y, marker=plane_path)
```

![alt text](https://github.com/rskschrom/er2_mpl_marker/blob/master/plane.png)
