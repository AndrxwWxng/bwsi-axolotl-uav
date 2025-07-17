#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# import our new fizzbuzz message type
from fizzbuzz_interfaces.msg import FizzBuzz 

# TODO import the number message useld for the numbers topic
from std_msgs.msg import Int64

class FizzBuzzNode(Node):
    def __init__(self):
        super().__init__('fizzbuzz')
        self.get_logger().info("Starting fizzbuzz node")

        self.total_numbers = 0
        self.total_fizz = 0
        self.total_buzz = 0
        self.total_fizzbuzz = 0

        # create a publisher object to send data
        self.fizzbuzz_pub = self.create_publisher(FizzBuzz, "fizzbuzz_stats", 10)

        # TODO fill in the TOPIC_NAME and MESSAGE_TYPE
        self.number_sub = self.create_subscription(Int64, "number", self.number_callback, 10)

    def number_callback(self, msg):
        # this function is called whenever a number is received.

        number = msg.data 

        fizzbuzz_str = self.fizzbuzz(number)
        # loginfo to print the string to the terminal
        self.get_logger().info(fizzbuzz_str)

        fizzbuzz_msg = FizzBuzz()
        fizzbuzz_msg.fizzbuzz = fizzbuzz_str
        fizzbuzz_msg.fizz_ratio = self.total_fizz / self.total_numbers # TODO fill in this value
        fizzbuzz_msg.buzz_ratio =  self.total_buzz / self.total_numbers # TODO fill in this value
        fizzbuzz_msg.fizzbuzz_ratio = self.total_fizzbuzz / self.total_numbers  # TODO fill in this value
        fizzbuzz_msg.number_total = self.total_numbers # TODO fill in this value

        # publish the message
        self.fizzbuzz_pub.publish(fizzbuzz_msg)

    def fizzbuzz(self, number):
        # TODO complete this function
        # This should return a string equal to:
        #      "fizz" if number divisible my 3
        #      "buzz" if number divisible my 5
        #      "fizzbuzz" if number divisible my 15
        #      an empty string otherwise
        self.total_numbers+=1
        if number % 15 == 0:
            self.total_fizzbuzz += 1
            return 'fizzbuzz'
        elif number % 3 == 0:
            self.total_fizz+=1
            return 'fizz'
        elif number % 5 == 0:
            self.total_buzz+=1
            return 'buzz'
        else:
            return ''



def main(args=None):
    rclpy.init()
    node = FizzBuzzNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()