from hand import AbstractHand


class RH4DHand(AbstractHand):
    """This class represents the Seed Robotics RH4D Hand."""

    current_limit = 250

    sensitive_motors = ("thumb_x", "indexfingers_x")

    current_ports = {"wrist_z": 0,
                     "wrist_x": 1,
                     "thumb_x": 2,
                     "indexfingers_x": 3}

    poses = {"openHand": {"thumb_x": (-160., 1.),
                          "indexfingers_x": (-160., 1.), },
             "closeHand": {"thumb_x": (100., 1.),
                           "indexfingers_x": (100., 1.), },
             "openHandVREP": {"thumb_x": (0., 1.),
                              "indexfingers_x": (0., 1.), },
             "closeHandVREP": {"thumb_x": (-30., 1.),
                               "indexfingers_x": (-30., 1.), },
             }

    def __init__(self, robot, isLeft, monitorCurrents=True, vrep=False):
        super(RH4DHand, self).__init__(robot, isLeft, monitorCurrents, vrep)
