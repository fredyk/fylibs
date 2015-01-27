
"""

 Copyright (c) 2015 Jhon Fredy Magdalena
 
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
"""

## This program has only be tested for windows

## -*- coding: iso-8859-1 -*-
import os, threading
import ImageFile, random, math
from time import sleep, time as now
from PIL import ImageTk, Image
from subprocess import Popen, PIPE
import sys
from _3dlib import *

def test():
    width, height = exch(320, 320*3/4)
    name = 'tmp'
    print width, height
    seconds = 10
    f = open('C:/tmp/values.txt','w');f.write('');f.close()
    path = './tmp.png'
    rate = 24
    nframes = rate*seconds
    
    mem = pixels(width, height)

    vi = video(
                width   = width,
                height  = height,
                rate    = rate,
                name    = name
        )
    init = now();print '[ generating video',
    for i in xrange(nframes):
        _init=now();print;print '[generating frame', i, 'of', nframes,
        gen_scene(mem, width, height,
                  i*2 if i < nframes/2 else nframes-2*(i-nframes/2),
                  path, nframes, sphere=True, rframe=i)
        vi.addFrame(mem.raw_image())
        print '; generated',round(now()-_init,3),'s] remaining:',\
              round((nframes-i+1)*(now()-init)/float(i+1)/(
                    1.0 if (((nframes-i+1)*(now()-init)/float(i+1))<60) \
                    else 60.0
                  ),3),\
                  's' if (((nframes-i+1)*(now()-init)/float(i+1))<60) else \
                  'm'
        if i and not (i%23) and not vi.writing:
            print '                                             ', vi.writing,
            vi.saveVideo()
            sleep(0.1)
    print;print 'generated', round(now()-init,3), nframes,'s ]'
    vi.ov.end()
    vi.name = 'sphere%dx%d' % (width, height)
    vi.saveVideo(force=True)
    
if __name__ == '__main__':
    test()

