"""
Smart thermostat Simulation
"""

class SmartThermostat:
    def __init__(self,device_id,temperature,current_temperature):
        if not device_id:
            raise ValueError
        elif not isinstance(device_id,str):
            raise TypeError
        self.device_id = device_id

        
        self.temperature = temperature

        self.current_temperature = current_temperature

        self._change_count = 0

    @property
    def temperature(self):
        return self.temperature

    @temperature.setter
    def temperature(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError
        elif isinstance(value,bool):
            raise TypeError
        elif value <= 16 or value >= 30:
            raise ValueError
        elif value == self.temperature:
            self.temperature = value
        self.temperature = value
        self.change_count+=1

    @property
    def current_temperature(self):
        return self.current_temperature

    def update_sensor_reading(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError
        elif value < -40 or value > 80:
            raise ValueError

        self.current_temperature = value

    @property
    def change_count(self):
        return self._change_count


if __name__ == '__main__':
    thermo1 = SmartThermostat('13',29,19)
    print(thermo1.current_temperature)
    thermo1.temperature = 22
    print(thermo1.temperature)
    print(thermo1.change_count)
    thermo1.temperature = 23
    print(thermo1.change_count)
    thermo1.temperature = 23
    print(thermo1.change_count)
    thermo1.temperature = 23
    print(thermo1.change_count)
    thermo2 = SmartThermostat('1512',22,20)
    print(thermo2.change_count)
    print(issubclass(bool,int))


()