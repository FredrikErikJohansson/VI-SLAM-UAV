# LDSO V101
```
source.scale(2, source.get_center())
source.rotate(get_rot_mat('x', -math.pi/2 - math.pi/8), source.get_center())
source.rotate(get_rot_mat('z', -math.pi/2 + math.pi/8), source.get_center())
```

# LDSO V102
```
source.scale(20, source.get_center())
source.rotate(get_rot_mat('x', math.pi/16 + math.pi), source.get_center())
source.rotate(get_rot_mat('z', -math.pi/2 + math.pi/4), source.get_center())
source.translate((2,0,2))
source = source.crop(target.get_axis_aligned_bounding_box())
source.translate((0,0,-1))
source.scale(1.4, source.get_center())
```

# LDSO V103
```
source.scale(2, source.get_center())
source.rotate(get_rot_mat('x', math.pi/4 + math.pi), source.get_center())
source.rotate(get_rot_mat('z', -math.pi/2 + math.pi/8), source.get_center())
source.translate((0,0,2))
```

# LDSO V201
```
source.scale(4, source.get_center())
source.rotate(get_rot_mat('x', -math.pi/2), source.get_center())
source.rotate(get_rot_mat('z', math.pi/2), source.get_center())
```

# LDSO V202
```
source.scale(0.25, source.get_center())
source.rotate(get_rot_mat('x', -math.pi/2), source.get_center())
source.rotate(get_rot_mat('z', math.pi/2), source.get_center())
source.translate((-6,0,2))
source.rotate(get_rot_mat('y', -math.pi/8), source.get_center())
```

# ORB V102
```
source.scale(0.15, source.get_center())
source.rotate(get_rot_mat('x', -math.pi/8), source.get_center())
source.rotate(get_rot_mat('y', math.pi/2 + math.pi/4 - math.pi/16), source.get_center())
source.rotate(get_rot_mat('x', -math.pi/2), source.get_center())
source.translate((-10,0,-1))
```

# ORB V202
```
source.rotate(get_rot_mat('x', -math.pi/2), source.get_center())
source.rotate(get_rot_mat('z', math.pi/2), source.get_center())
source.translate((-4,0,1))
source.rotate(get_rot_mat('y', -math.pi/8), source.get_center())
```

