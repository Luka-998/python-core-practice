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

        self._change_count = 0
        self.temperature = temperature
        self._current_temperature = current_temperature

        

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self,value):
        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError
        elif value < 16 or value > 30:
            raise ValueError

        else:
            if not hasattr(self,"_temperature"):
                self._temperature = value
            
            else:
                if self._temperature == value:
                    return self._temperature
                self._temperature = value
                self._change_count+=1


    @property
    def current_temperature(self):
        if not hasattr(self,'_current_temperature'):
            self._current_temperature = self.current_temperature


    def update_sensor_reading(self,value):
        if not isinstance(value,(int,float)) or isinstance(value,bool):
            raise TypeError
        elif value < -40 or value > 80:
            raise ValueError

        self._current_temperature = value

    @property
    def change_count(self):
        return self._change_count


if __name__ == '__main__':
    thermo = SmartThermostat("T1", 22, 20)

    thermo.temperature = 22
    thermo.temperature = 25
    thermo.temperature = 25
    thermo.temperature = 27

    print(thermo.change_count)
