from scikits.image.backend import register
register(backend="opencv", module="scikits.image.color", source="colorconv_opencv", \
    functions=["rgb2grey", "rgb2hsv", "hsv2rgb", "rgb2xyz", "xyz2rgb"])
