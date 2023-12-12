import rclpy
from my_cpp_py_pkg.module_to_import import my_node

def main(args = None):
    rclpy.init(args=args)
    node = my_node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()