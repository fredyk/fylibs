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

import time
from pipeffmpeg import *  # Download this module from https://github.com/kanryu/pipeffmpeg by kanryu
##from graph_lib import *
from _3dlibs import *
from PIL import Image
from time import time as now
import BmpImagePlugin, os, threading
import cStringIO as StringIO

class video():

    class save(threading.Thread):

        def __init__(self, sup):
            threading.Thread.__init__(self)
            self.sup = sup
            self.ov = sup.ov
            self.name = sup.name
            self.nframes = sup.nframes
            self.frames = sup.frames

        def run(self):
            self.ov.writing = True
            self.ov.open('./video/'+self.name+'.mp4', self.nframes)
            init=now();print;print '[writing video',
            for i, x in enumerate(self.frames):
    ##            print 'writing frame', i
                self.ov.writeframe(x)
            self.ov.close()
            self.ov.writing = False
            self.sup.writing = False
            print;print 'wroten',round(now()-init,3),'s]'

    def __init__(self, width, height, nframes, rate, name):
        self.ov = OutVideoStream(res=str(width)+'x'+str(height))
        self.frames = []
        self.name = name
        self.nframes = nframes
        self.ov.rate = rate
        self.writing = False

    def addFrame(self, st):
        self.frames.append(st.encode('iso-8859-1'))

    def saveVideo(self, force=False):
        if not os.path.lexists('./video/'):
            os.makedirs('./video/')
        if force and (self.ov.writing):
            print 'forcing subprocess to close'
            self.ov.close()
        if (not self.ov.writing) or force:
            print self.ov.writing,
            self.writing = True
            self.save(self).start()

def test():
    width = 480
    height = width*9/16
    name = 'tmp'
    print width, height
    seconds = 10
    f = open('C:/tmp/values.txt','w');f.write('');f.close()
    path = './tmp.png'
    rate = 24
    nframes = rate*seconds
    
    
    mem = pixels(width, height)

    vi = video(
                width = width,
                height  = height,
                nframes = nframes,
                rate    = rate,
                name    = name
        )
    init = now();print '[ generating video',
    for i in xrange(nframes):
        gen_scene(mem, width, height, i, path, nframes)
##        image = Image.open(path)
        _init=now();print '[coding frame', i,
        vi.addFrame(mem.raw_image())
        print 'coded',round(now()-_init,3),'s]'
##        if i and not (i%23) and not vi.writing:
##        if not vi.writing:
        if i and not (i%23) and i<24:
            print '                                             ', vi.writing,
            vi.saveVideo()
            time.sleep(0.1)
    print;print 'generated', round(now()-init,3), nframes,'s ]'
    try:
        vi.ov.close()
    except:pass
    vi.name = 'sphere%dx%d' % (width, height)
    vi.saveVideo(True)
    
if __name__ == '__main__':
    test()
