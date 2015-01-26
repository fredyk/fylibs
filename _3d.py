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

