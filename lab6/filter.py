#!/usr/bin/env python

def mean(D):
    return sum(D)/len(D)

def mean_filter(raw_data, width):
    data = []
    for i in xrange(width-1):
        data.append(raw_data[0])
    #data.append(raw_data)
    data += raw_data
    for i in xrange(width-1):
        data.append(raw_data[len(raw_data)-1]) 

    filtered = []
    for i in xrange(len(raw_data)):
        filtered.append(mean(data[i:i+width]))
    return filtered
