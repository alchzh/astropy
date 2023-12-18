# Licensed under a 3-clause BSD style license - see LICENSE.rst
from astropy import config as _config


class Conf(_config.ConfigNamespace):
    """
    Configuration parameters for `astropy.visualization.wcsaxes`.
    """

    coordinate_range_samples = _config.ConfigItem(
        50,
        "The number of samples along each image axis when determining "
        "the range of coordinates in a plot.",
    )

    frame_boundary_samples = _config.ConfigItem(
        1000,
        "How many points to sample along the axes when determining tick locations.",
    )

    grid_samples = _config.ConfigItem(
        1000, "How many points to sample along grid lines."
    )

    contour_grid_samples = _config.ConfigItem(
        200, "The grid size to use when drawing a grid using contours"
    )
conf = Conf()
