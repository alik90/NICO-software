import logging
import sys
import time
from os.path import abspath, dirname

import pypot.dynamixel.error
from nicomotion import Motion

logger = logging.getLogger(__name__)


if __name__ == '__main__':

    logging.basicConfig(
        level=logging.WARNING,
        format='%(asctime)s - %(levelname)s - %(name)s: %(message)s')

    poses = (
        "thumbsUp",
        "pointAt",
        "okSign",
        "pinchToIndex",
        "keyGrip",
        "pencilGrip",
        "closeHand",
        "openHand",
        "prepareGrab")

    if len(sys.argv) < 2 or sys.argv[1] not in ("left", "right"):
        message = ("Please specify which hand to use as first argument " +
                   "(left or right) and add at least one pose argument. " +
                   "Multiple poses will be executed in sequence.\n" +
                   "The known poses are: \n{}".format(', '.join(poses)))
        sys.exit(message)

    hand = sys.argv[1][0].upper() + "Hand"

    arm = sys.argv[1][0]

    if len(sys.argv) < 3:
        message = ("Please add at least one pose as argument. Multiple " +
                   "arguments will be executed in sequence.\nKnown poses " +
                   "are: \n{}".format(', '.join(poses)))
        sys.exit(message)

    for pose in sys.argv[2:]:
        if pose not in poses:
            sys.exit("Unknown pose {}, try one of the following: {}".format(
                pose, ', '.join(poses)))

    robot = Motion.Motion(dirname(abspath(__file__)) +
                          "/../../../../json/nico_humanoid_upper_rh7d.json",
                          vrep=False)

    prefix = 1. if arm == "l" else -1.

    robot.setAngle(arm + "_shoulder_z", prefix * 0., .03)
    robot.setAngle(arm + "_shoulder_y", prefix * -20., .03)
    robot.setAngle(arm + "_elbow_y", prefix * 80., .03)
    for pose in sys.argv[2:]:
        robot.setHandPose(hand, pose, .2)
        time.sleep(5.0)

    robot.setAngle(arm + "_shoulder_y", prefix * 0, .03)
    robot.setAngle(arm + "_elbow_y", prefix * 80, .03)
    robot.openHand(hand, .2)
    time.sleep(3)
    robot.disableTorqueAll()
