#!/usr/bin/env python

# filter data


import math
from sensor import *
import numpy

def mean(D):
    return sum(D)/len(D)


def median(D):
    D = sorted(D)
    n = len(D)
    m = n - 1
    return (D[n/2] + D[m/2]) / 2.


def report(data):
    mean = numpy.mean(data)
    median = numpy.median(data)
    std = numpy.std(data)
    print ' Mean        = ', mean
    print ' Std         = ', std
    print ' Median      = ', median
    print ' Maxium      = ', max(data)
    print ' Minimum     = ', min(data)

    outside_points = [d for d in data if d > (mean + std) or d < (mean - std)]
    print ' OutsideRate = ',float(len(outside_points))/len(data)


def filter_fun(function, raw_data, width):
    data = []
    for i in xrange(width-1):
        data.append(raw_data[0])
    #data.append(raw_data)
    data += raw_data
    for i in xrange(width-1):
        data.append(raw_data[len(raw_data)-1]) 

    filtered = []
    for i in xrange(len(raw_data)):
        filtered.append(function(data[i:i+width]))
    return filtered

if __name__ == '__main__':
    # user setting
    point_number = 100
    noise = 0.05
    filter_width = input('Filter width = ')

    # generate original sensor data
    data = generate_sensor_data(point_number, noise)
    print_sensor_data(data, 'raw')

    # mean filter
    filtered_data_mean = filter_fun(mean, data, filter_width)
    print_sensor_data(filtered_data_mean, 'filtered_mean')#+ str(filter_width)

    # median filter
    filtered_data_median = filter_fun(median, data, filter_width)
    print_sensor_data(filtered_data_median, 'filtered_median')#+ str(filter_width)


    print 'Statistics report-----------------------'
    print 'Origianl data:'
    print ' Number of point = ', point_number
    print ' Noise           = ', noise
    print ' Filter width    = ', filter_width
    print 'Mean filter:'
    report(filtered_data_mean)
    print 'Median filter:'
    report(filtered_data_median)
    print 'End-------------------------------------'


    # To plot width = 1 3 9 37
    # plot "raw" with line, "filtered_mean_1" with line, "filtered_median_1" with line, "filtered_mean_3" with line, "filtered_median_3" with line,"filtered_mean_9" with line, "filtered_median_9" with line, "filtered_mean_27" with line, "filtered_median_27" with line
