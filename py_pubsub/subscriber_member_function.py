# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy

#import sys
#sys.path.append("/ros2_ws/install/py_pubsub/lib/python3.10/site-packages/py_pubsub")

#added from motor control
from .motor_control.imported import motorDriver

from rclpy.node import Node

from std_msgs.msg import String

from geometry_msgs.msg import Twist

import time

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(Twist, '/cmd_vel', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard for linear x: "%f"' % msg.linear.x)
        self.get_logger().info('I heard for angular z: "%f"' % msg.angular.z)

        #section for controlling motor from twist msg
        motorCon = motorDriver(22, 7, 16, 18, 13, 11)
        if msg.linear.x > 0:
            motorCon.forward(msg.linear.x)

        if msg.linear.x < 0:
            #multiplied by -1 to make positive
            i = msg.linear.x * -1
            motorCon.backward(i)

        if msg.angular.z > 0:
            motorCon.left(msg.angular.z)

        if msg.angular.z < 0:
            #multiplied by -1 to make positive
            i = msg.angular.z * -1
            motorCon.right(i)



def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)
    


    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
