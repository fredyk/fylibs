import os, threading
from _3dlibs import *
from PIL import Image
from time import sleep, time as now

class video():

    class save(threading.Thread):

        def __init__(self, sup):
            threading.Thread.__init__(self)
            self.sup = sup
            self.ov = sup.ov
            self.name = sup.name
            self.frames = sup.frames

        def run(self):
            self.ov.ofnm = './video/'+self.name+'.mp4'
            self.ov.newVideo()
            init=now();print;print '[writing video',
            for i, x in enumerate(self.frames):
                if self.sup.force:
                    print 'writing frame', i
                self.ov.save(st=x)
            self.ov.end()
            self.sup.writing = False
            print;print 'written',round(now()-init,3),'s]'

    def __init__(self, width, height, rate, name):
        self.frames = []
        self.name = name
        self.ov = Video(
                         size = '%dx%d' % (width, height),
                         rate = rate
            )
        self.writing = False
        self.force = False

    def addFrame(self, st):
        self.frames.append(st.encode('iso-8859-1'))

    def saveVideo(self, force=False):
        self.force = force
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
    width = 320
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
                width   = width,
                height  = height,
                rate    = rate,
                name    = name
        )
    init = now();print '[ generating video',
    for i in xrange(nframes):
        gen_scene(mem, width, height, i, path, nframes, sphere=True)
        _init=now();print '[coding frame', i,
        vi.addFrame(mem.raw_image())
        print 'coded',round(now()-_init,3),'s]'
        if i and not (i%23) and not vi.writing:
##        if i and not (i%23) and i<24:
            print '                                             ', vi.writing,
            vi.saveVideo()
            sleep(0.1)
    print;print 'generated', round(now()-init,3), nframes,'s ]'
    vi.ov.end()
    vi.name = 'sphere%dx%d' % (width, height)
    vi.saveVideo(force=True)
    
if __name__ == '__main__':
    test()
