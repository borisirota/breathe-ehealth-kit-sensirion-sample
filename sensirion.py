#! /usr/bin/python
# -*- coding: utf-8 -*-

from sensirion_sensors import find_sensors_by_type, SensorReader

import argparse
import sys
import time

def main():
    # parse arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--frequency', '-f', type=int, default=10, help='read out frequency')
    args = parser.parse_args()

    # probe for sensors
    sensors_list = ['sfm3000', 'sdp600']	 
    sensors = find_sensors_by_type(sensors_list[0]) + find_sensors_by_type(sensors_list[1])
    if not sensors:
        sys.stderr.writelines('No sensors found!\n')
        return

    value_format = '{0:.3f}'
    
    # write data JSON to stdout
    def print_values(timestamp, values):
	i = 0
	sdata = ''
	sdata += '\"{'
        for sensor, sensor_values in values.iteritems():
            for value, unit in zip(sensor_values, sensor.get_units()):
                if value is None:
		    continue
                else:
		    if (i > 0):
			sdata += ','
		    sdata += '\\\"' + sensors_list[i] + '\\\":'
                    sdata += value_format.format(value)
		i += 1
	sdata += '}\"'
        sdata += '\n'
		
       	sys.stdout.write(sdata) 
	sys.stdout.flush()
	return True

    # run the sensor reader synchranously
    try:
        reader = SensorReader(sensors, args.frequency, print_values)
        reader.run()
    except:
        pass


if __name__ == '__main__':
    main()
