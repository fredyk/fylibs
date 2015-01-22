import os, threading
from _3dlibs import *
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
                         size = '%dx%d' % (width, height)#,
                         # other args
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
    width = 1280
    height = width*3/4
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
