#!/usr/bin/env python3


#Se importan todos los modulos y paquetes necesarios para el código

from pickletools import uint8
import time
import rospy
import sys
from getkey import getkey, keys
from geometry_msgs.msg import Twist
from std_msgs.msg import Int8
from std_msgs.msg import UInt8
from std_msgs.msg import Empty



class Keyboard_control:
    def __init__(self):
        self.pub_takeoff = rospy.Publisher('/tello/takeoff', Empty, queue_size=10)
        self.pub_land = rospy.Publisher('/tello/land', Empty, queue_size=10)
        self.pub_flip = rospy.Publisher('/tello/flip', UInt8, queue_size=10)
        self.pub_cmd_vel = rospy.Publisher('/tello/cmd_vel', Twist, queue_size=10)
        self.pub_override = rospy.Publisher('keyboard_control/override', Int8, queue_size=10)
        self.vel_msg = Twist()
        self.flip_msg = 0
        self.ovr_msg = 0
        self.speed_value = 0.5
        self.cmd_vel()

    def cmd_vel(self):
        #Función que corre siempre y cuando el nodo no esté terminado
        while not rospy.is_shutdown():
            key = getkey()
            
            if key == keys.T:
                msg = Empty()
                self.pub_takeoff.publish(msg)
                print('Despegando')

            elif key == keys.SPACE:
                msg = Empty()
                self.pub_land.publish(msg)
                print('Aterrizando')
            
            elif key == keys.W:
                self.vel_msg.linear.x = round(self.speed_value, 2)
                self.vel_msg.linear.y = 0.0
                self.vel_msg.linear.z = 0.0
                self.vel_msg.angular.z = 0.0
                self.pub_cmd_vel.publish(self.vel_msg)
                print("Avanzando")
                time.sleep(3)
                self.vel_msg.linear.x = 0.0
                self.vel_msg.linear.y = 0.0
                self.vel_msg.linear.z = 0.0
                self.vel_msg.angular.z = 0.0
                self.pub_cmd_vel.publish(self.vel_msg)
                print("Reposo")


            elif key == keys.S:
                self.vel_msg.linear.x = -round(self.speed_value, 2)
                self.vel_msg.linear.y = 0.0
                self.vel_msg.linear.z = 0.0
                self.vel_msg.angular.z = 0.0
                self.pub_cmd_vel.publish(self.vel_msg)
                print("Retrocediendo")
                time.sleep(3)
                self.vel_msg.linear.x = 0.0
                self.vel_msg.linear.y = 0.0
                self.vel_msg.linear.z = 0.0
                self.vel_msg.angular.z = 0.0
                self.pub_cmd_vel.publish(self.vel_msg)
                print("Reposo")

            elif key == keys.D:
                self.vel_msg.linear.x = 0.0
                self.vel_msg.linear.y = -round(self.speed_value, 2)
                self.vel_msg.linear.z = 0.0
                self.vel_msg.angular.z = 0.0
                self.pub_cmd_vel.publish(self.vel_msg)
                print("Derecha")
                time.sleep(3)
                self.vel_msg.linear.x = 0.0
                self.vel_msg.linear.y = 0.0
                self.vel_msg.linear.z = 0.0
                self.vel_msg.angular.z = 0.0
                self.pub_cmd_vel.publish(self.vel_msg)
                print("Reposo")

            elif key == keys.A:
                self.vel_msg.linear.x = 0.0
                self.vel_msg.linear.y = round(self.speed_value, 2)
                self.vel_msg.linear.z = 0.0
                self.vel_msg.angular.z = 0.0
                self.pub_cmd_vel.publish(self.vel_msg)
                print("Izquierda")
                time.sleep(3)
                self.vel_msg.linear.x = 0.0
                self.vel_msg.linear.y = 0.0
                self.vel_msg.linear.z = 0.0
                self.vel_msg.angular.z = 0.0
                self.pub_cmd_vel.publish(self.vel_msg)
                print("Reposo")

            elif key == keys.E:
                self.vel_msg.linear.x = 0.0
                self.vel_msg.linear.y = 0.0
                self.vel_msg.linear.z = 0.0
                self.vel_msg.angular.z = -round(self.speed_value, 2)
                self.pub_cmd_vel.publish(self.vel_msg)
                print("Giro S. Horario")
                time.sleep(3)
                self.vel_msg.linear.x = 0.0
                self.vel_msg.linear.y = 0.0
                self.vel_msg.linear.z = 0.0
                self.vel_msg.angular.z = 0.0
                self.pub_cmd_vel.publish(self.vel_msg)
                print("Reposo")

            elif key == keys.Q:
                self.vel_msg.linear.x = 0.0
                self.vel_msg.linear.y = 0.0
                self.vel_msg.linear.z = 0.0
                self.vel_msg.angular.z = round(self.speed_value, 2)
                self.pub_cmd_vel.publish(self.vel_msg)
                print("Giro S. Anti-Horario")
                time.sleep(3)
                self.vel_msg.linear.x = 0.0
                self.vel_msg.linear.y = 0.0
                self.vel_msg.linear.z = 0.0
                self.vel_msg.angular.z = 0.0
                self.pub_cmd_vel.publish(self.vel_msg)
                print("Reposo")

            elif key == keys.Z:
                self.vel_msg.linear.x = 0.0
                self.vel_msg.linear.y = 0.0
                self.vel_msg.linear.z = round(self.speed_value, 2)
                self.vel_msg.angular.z = 0.0
                self.pub_cmd_vel.publish(self.vel_msg)
                print("Subiendo")
                time.sleep(3)
                self.vel_msg.linear.x = 0.0
                self.vel_msg.linear.y = 0.0
                self.vel_msg.linear.z = 0.0
                self.vel_msg.angular.z = 0.0
                self.pub_cmd_vel.publish(self.vel_msg)
                print("Reposo")

            elif key == keys.X:
                self.vel_msg.linear.x = 0.0
                self.vel_msg.linear.y = 0.0
                self.vel_msg.linear.z = -round(self.speed_value, 2)
                self.vel_msg.angular.z = 0.0
                self.pub_cmd_vel.publish(self.vel_msg)
                print("Bajando")
                time.sleep(3)
                self.vel_msg.linear.x = 0.0
                self.vel_msg.linear.y = 0.0
                self.vel_msg.linear.z = 0.0
                self.vel_msg.angular.z = 0.0
                self.pub_cmd_vel.publish(self.vel_msg)
                print("Reposo")

            elif key == keys.F:
                self.flip_msg = 1
                self.pub_flip.publish(self.flip_msg)
                print("Flip")


def main():
    #Se inicializa el nodo
    rospy.init_node('keyboard_control', anonymous=True)
    keyboard_control = Keyboard_control()
    #Inicializamos el loop para que se ejecute el nodo mientras esté activo
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass


if __name__ == '__main__':
    main()