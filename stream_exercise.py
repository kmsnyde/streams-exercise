#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:16:17 2018

@author: kmsnyder2
"""
import io

class StreamProcessor():
    
    
    
    def __init__(self, stream):
        self.stream = stream
        
    def process(self):
        
        count = 0
        total = 0
    
        while count < 10 and total <= 200:
            digits = self.stream.read(2) #read 2 bytes as string
            if len(digits) < 2:
                break
            
            count += 1
            
            n = int(digits)
            
            total += n
            
            
        return count


if __name__ == '__main__':
    
    # researched internet on ways to generated various size random strings of digits
    #def id_generator(size=6, chars=string.digits):
    #    return ''.join(random.choice(chars) for _ in range(size))
    
    # use to modify how many strings of digits to use in test
    expected = 20
    #value = "234761640930110349378289194"
    value = "23476"
    my_stream_processor = StreamProcessor(io.StringIO(value))
    result = my_stream_processor.process()
    print(result)