# class TrafficLight:
#
#     color = "c"
#
#     def stop(self):
#         print("Stop! Red now ")
#     def wait(self):
#         print("Wait! Yellow now")
#     def running(self):
#         print("Drive! Green now")
#
# t_light = TrafficLight()
# t_light.running()


from time import sleep


class TrafficLight:
    __color = "Цвет"

    def running(self):
        while True:
            print("Красный")
            sleep(7)
            print("Желтый")
            sleep(2)
            print("Зеленый")
            sleep(5)
            print("Желтый")
            sleep(2)


trafficlight = TrafficLight()
trafficlight.running()
