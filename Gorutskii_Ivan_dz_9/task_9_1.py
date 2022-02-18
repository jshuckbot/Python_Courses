class TrafficLight:
    """Класс регугировки сфетофора"""
    __color: tuple = {
        'red': 4,
        'yellow': 2,
        'green': 3,

    }

    def running(self):
        """Запуск светофора"""
        count = 0
        break_trafic_light = True
        order_trafic_light = []
        for color, seconds in TrafficLight.__color.items():
            if break_trafic_light:
                for sec in range(1, seconds + 1):
                    if color == 'red' and sec == seconds and count % 3 == 0:
                        order_trafic_light.append(color)
                        count += 1
                        continue
                    elif color == 'yellow' and sec == seconds and\
                            count % 3 == 1:
                        order_trafic_light.append(color)
                        count += 1
                        continue
                    elif color == 'green' and sec == seconds and\
                            count % 3 == 2:
                        order_trafic_light.append(color)
                        continue
                    if sec == seconds and count != 2:
                        break_trafic_light = False

        if len(order_trafic_light) == 3:
            for color, seconds in TrafficLight.__color.items():
                print(f'{color} {seconds} сек')
        else:
            print('Нужна диагностика светофору! Нарушен порядок')


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
