
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

## This lib has not already be tested for linuxs or ios, only
## for windows

import math
import threading, ImageFile, os, random
from time import sleep, time as now
from Tkinter import Tk
from PIL import ImageTk, Image
from subprocess import Popen, PIPE
from time import time as now
import time, math, random
##from subprocess import PIPE, STDOUT, Popen

def trygon_signs(a, b=None):
    a, b = [x for x in a] if (b is None) else (a, b)
    return (
                1 if a>0 else -1, # sin sign
                1 if b>0 else -1  # cos sign
        )

def ang(a, b=None):
    a, b = [x for x in a] if (b is None) else (a, b)
    signs = trygon_signs(a, b)
    tan = abs(b/float(a)) if a != 0 else 9999
    return math.atan(tan) if (
            signs == (1, 1)
        ) else (
            math.pi-math.atan(tan) if (
                signs == (-1, 1)
                ) else (
                    math.pi+math.atan(tan) if (
                        signs == (-1, -1)
                        ) else (
                            math.pi*2-math.atan(tan)
                            )
                    )
            )

def dist(a, _b, c=None, d=None):
    if (not(c)) and (not(d)) and ((type(a)==tuple)or(type(a)==list)) \
                             and ((type(_b)==tuple)or(type(_b)==list)):
        a, b = (a) if (type(a)==tuple) else (a[0], a[1])
        c, d = (_b) if (type(_b)==tuple) else (_b[0], _b[1])
    else:
        b = _b
        if (not(d)) and (c) and ((type(c)==tuple)or(type(c)==list)):
            c, d = (c) if (type(c)==tuple) else (c[0], c[1])
    return math.sqrt((a-c)**2+(b-d)**2)

def c3dto2d(a, b=None, c=None, visor=[1920/2, -1920, 1080/2], _int=False): #[x, y, z]
    x, y, z = (a) if (not(b) and not(c)) else (a, b, c)
    vx, vy, vz = visor
##    print (vx-x)/float((vz-z))*(0-z), \
##          '\n           ', (vy-y)/float((vz-z))*(0-z)
    return (
            int(x+(vx-x)/float((vy-y))*(0-y)), #x1
            int(z+(vz-z)/float((vy-y))*(0-y))  #y1
        ) if (_int) else (
            x+(vx-x)/float((vy-y))*(0-y), #x1
            z+(vz-z)/float((vy-y))*(0-y)  #y1
            )

def _rot(cords, center, angle):
    x0, y0 = cords if type(cords)==tuple else [c for c in cords]
    cx, cy = center if type(center)==tuple else [c for c in center]
##    rx, ry = angle if type(angle)==tuple else [a for a in angle]
    rz = angle
    a = dist((x0, y0),(cx, cy))# * (-1 if ((((x0-cx)>=0)and((y0-cy)<0))or\
##                                          (((y0-cy)>=0)and((x0-cx)<0))) else 1)
    
##    beta = (math.atan((y0-cy)/float(x0-cx)) if (x0-cx)<>0 else math.pi/2.0)
    beta = ang((x0-cx, y0-cy))
##    if ((y0-cy)<0)and((x0-cx)<0):
##        beta+=math.pi
##    elif ((y0-cy)>0)and((x0-cx)<0):
##        beta+=math.pi
    alpha_beta = rz + beta
##    print a, alpha_beta,
    return (
        cx + a * \
            math.cos(alpha_beta),
        cy + a * \
            math.sin(alpha_beta)
        )

def rot(cords, center, angle):
    rx, ry, rz = angle# if type(angle)==tuple else [a for a in angle]
    x0, y0, z0 = cords# if type(cords)==tuple else [c for c in cords]
    cx, cy, cz = center# if type(center)==tuple else [c for c in center]
##    print x0, y0, z0

    y0, z0 = _rot((y0, z0), (cy, cz), rx) if rx else (y0, z0)
##    print x0, y0, z0
    x0, z0 = _rot((x0, z0), (cx, cz), ry) if ry else (x0, z0)
##    print x0, y0, z0
    x0, y0 = _rot((x0, y0), (cx, cy), rz) if rz else (x0, y0)
##    print x0, y0, z0
    return x0, y0, z0
##    print math.atan((y0-cy)/float(x0-cx)), (y0-cy)/float(x0-cx)
##    return (
##        dist((x0, y0),(cx, cy)) * \
##            math.cos(rz+math.atan((y0-cy)/float(x0-cx))),
##        y0,
##        z0
##        )

if __name__ == '__main__':
##    for y in xrange(0, 1080, 100):
##        for x in xrange(0, 1920, 100):
##            x, y, z = x, y, 1
##            print [x, y, z], c2dto3d([x, y, z], _int=True)
##    for x in xrange(-1, 2, 2):
##        for y in xrange(-1, 2, 2):
####            for z in xrange(-1, 2, 2):
##            x, y, z = x, y, 0
##            print [x, y, z], rot((x, y, z), (0, 0, 0), [0, 0, 1])
##        math.pi/4.0,
##        math.pi/4.0,
##        math.pi/4.0])
    print rot(
##        rot((1, 0, 0), (0, 0, 0), (math.pi/2.0, 0, 1)),
        (1, 0, 0),
        (0, 0, 0), (0, 0, -1)
        )
# -*- coding: iso-8859-1 -*-

def unichrs():
    return [
        (unichr(x) if (x>0) else u'\x00')
        for x in xrange(256)
        ]

def colours():
    uc = unichrs()
    return [
                [
                    [
                        (uc[x]+uc[y]+uc[z])
                        for z in xrange(256)
                        ]
                    for y in xrange(256)
                    ]
        for x in xrange(256)
        ]

class pixels():

    def __init__(self, width=1920, height=None, dev=None, verbose=False):
        init = now()
        height=width*9/16 if not height else height
        self.width, self.height = width, height
        if verbose:
            print;print '[generating colours',
        self.clrs, self.last, self.lasts = colours(), (-1,-1,-1), u''
        self.time = round(now()-init,3)
        if verbose:
            print 'generated', round(now()-init,2),'s ]'
        self.bytes = Bytes()
        self.rad = 100+int(math.floor(random.random() * abs(height-100)))
        self.pxs = []
        self.black = []
        self.pxst = u''
        self.writing = False
        self.used = []
        self.w = None
        self.bpp = 3
        f = open('C:/tmp/values.txt','w');f.write('');f.close()

    def px2(self, a, b, c):
        if (a>255) or (b>255) or (c>255):
            a, b, c = min(a, 255), min(b, 255), min(c, 255)
        if (a<0) or (b<0) or (c<0):
            a, b, c = max(a, 0), max(b, 0), max(c, 0)
        if (a, b, c) == self.last:
            return self.lasts
        else:
            self.last = (a,b,c)
            self.lasts = self.clrs[a][b][c] if ((a)or(b)or(c)) else u'\x00\x00\x00'
        return self.lasts

    def toEmpty(self, w=None, h=None):
        w = self.width if not (w) else w
        h = self.height if not (h) else h
        self.pxs = [
            [
                u'' for x in xrange(w)
                ]
            for y in xrange(h)
            ]

    def newbitmap(self, w=None, h=None, verbose=False):
        if verbose:
            init=now();print;print '[generating new bitmap',
        self.toEmpty(w, h)
        self.paintFloor()
        if verbose:
            print 'generated', round(now()-init,2),'s ]'

    def newpx(self, x, y, style, ):
        if not(self.pxs):
            self.newbitmap()
        if(y in range(0, len(self.pxs)))and\
             (x in range(0, len(self.pxs[y]))):
            self.pxs[y][x] = self.px2(*style)

    def paintCircle(self, center, rad, style=None, verbose=False):
        if verbose:
            init=now();print;print '[painting circle',
        for y in xrange(center[1]-rad, center[1]+rad):
            for x in xrange(center[0]-rad, center[0]+rad):
                _dist = dist(x, y, center)
                if _dist<=rad:
                    self.newpx(x, y, (255, 0, 0) if not style else style)
        if verbose:
            print round(now()-init,2), 's ]'

    def paintCube(self, origin=(100, 100, 50), dim=(1000, 1000, 1000), \
                  style=(255, 0, 0), rotation=(0, 0, -1), res=[1920,1080]):
        ox, oy, oz = [int(o) for o in origin]
        dx, dy, dz = [int(d) for d in dim]
        center = (cx, cy, cz) = (ox+dx/2.0,
                                oy+dy/2.0,
                                oz+dz/2.0)        
        f = open('C:/tmp/values.txt','a');f.write(str(origin)+' '+str(dim)+\
                                                  ' '+str(center)+'\n')
        f.close()
        minx, miny, minz, maxx, maxy, maxz = ox, oy, oz, ox+dx, oy+dy, oz+dz
        permxy = [(minx, miny), (minx, maxy), (maxx, miny), (maxx, maxy)]
        permyz = [(miny, minz), (miny, maxz), (maxy, minz), (maxy, maxz)]
        permxz = [(minx, minz), (minx, maxz), (maxx, minz), (maxx, maxz)]
        for x in xrange(ox, ox+dx+1):
            for y in xrange(oy, oy+dy+1):
                if x==minx or x==(ox+dx) or y==miny or y==(oy+dy):
                    for z in xrange(oz, oz+dz+1):
                        if((x, y) in permxy) or \
                          ((y, z) in permyz) or \
                          ((x, z) in permxz):
                            nx, ny, nz = rot(
                                [x, y, z], center, rotation
                                )
                            a, b = c3dto2d([nx, ny, nz],
                                           visor=[res[0]/2.0,
                                                  -res[1]*2,
                                                  res[1]/2.0], _int=True)
                            self.newpx(a, b, style)

    def paintArc(self, origin=(100, 100, 100), rad=100, \
                 style=None, rotation=None, rot2=None,
                 res=[1920,1080], center=None):
        verts = []
        ox, oy, oz = [int(o) for o in origin]
        rx, ry, rz = rotation
        center = (cx, cy, cz) = origin if not center else center
        z = oz
        _max = int(math.ceil(2*math.pi*rad))
        a = 0
        for i in xrange(_max):
            rz = i/float(_max)*math.pi*2
            nx, ny, nz = rot(
                rot(
                    [ox+rad, oy, oz], center, (0,
                                               0,
                                               rz)
                ), center, rotation
                ) if rotation else rot(
                        [ox+rad, oy, oz], center, (0,
                                                   0,
                                                   rz)
                                    )
            nx, ny, nz = rot(
                (nx, ny, nz), center, rot2
                ) if rot2 else (nx, ny, nz)
            a, b = c3dto2d([nx, ny, nz],
                           visor=[res[0]/2.0,
                                  -res[1]*2,
                                  res[1]/2.0], _int=True)
            ns = style if style else (
                    int((nz-oz+rad)*255/float(2*rad)),
                    0,
                    int(255-(nz-oz+rad)*255/float(2*rad))
                   )
            self.newpx(a, b,
                       ns
                       )
        return a

    def paintSphere(self, origin=(100, 100, 100), rad=100, \
                 style=None, rotation=(0, 0, 0), res=[1280,1024]):
        ox, oy, oz = [o for o in origin]
        rx, ry, rz = rotation
        step=16
        for i in xrange(0, 180, step/2):
            rz1 = i/180.0*math.pi
            if not(i%step):
                self.paintArc(origin, rad, style, rotation=(
                                        math.pi/2.0,
                                        0,
                                        rz1
                    ), rot2=rotation, res=res)
            self.paintArc(origin=(ox,
                                  oy,
                                  oz+rad*math.sin(rz1-math.pi/2.0)),
                          rad=rad*math.cos(rz1-math.pi/2.0),
                          style=style,
                          rotation=(0, 0, 0),
                          rot2=rotation, res=res, center=origin)
        return self

    def paintFloor(self):
        for x in range(0, self.width, self.width/10):
            for y in xrange(self.width):
                a, b = c3dto2d([x, y, 0],
                               visor=[self.width/2.0,
                                      -self.height*2,
                                      self.height/2.0], _int=True)
                self.newpx(a, b, (0, 0, 255))
                a, b = c3dto2d([y, x, 0],
                               visor=[self.width/2.0,
                                      -self.height*2,
                                      self.height/2.0], _int=True)
                self.newpx(a, b, (0, 0, 255))

    def raster(self, filename=None, rangex=None, rangey=None, test='',
               verbose=False):
        if not(self.pxs):
            self.newbitmap()
        if not(rangex) and not(rangey):
            self.pxst =  bmp_head(len(self.pxs[0]),len(self.pxs))
            if verbose:
                init=now();print;print '[rastering',
            prcnt = 0
            self.pxst+=''.join([
                ''.join([
                    _p if _p else u'\x00\x00\x00'
                    for _p in p
                    ])
                for p in self.pxs
                ])
            if verbose:
                print 'rastered', round(now()-init,2), 's ]'
            self.writing=True
            bm = gen_bmp(self.pxst, len(self.pxs[0]), len(self.pxs), self.bpp,
                         0, self.bytes, _init=now(), fname=filename,
                         mem=self)

            bm.start()

    def getImage(self, verbose=False):
        if verbose:
            init = now();print;print '[completing bmp',
        self.st = comp_bmp(self.pxst, self.width, self.height, self.bpp,
                           self.bytes)
        if verbose:
            print 'complete', round(now()-init,3),'s]',

        p = ImageFile.Parser()

        p.feed(self.st.encode('iso-8859-1'))

        im = p.close()
        return im

    def raw_image(self, verbose=False):
        if verbose:
            print 'generating raw',
        return ''.join([
            ''.join([
                _p if _p else u'\x00\x00\x00'
                for _p in p
                ])
            for p in self.pxs[::-1]
            ])

## This function obtains a .bmp image head

def bmp_head(width, height, chanels=3):
    return 'BM'+rev_num(54+chanels*width*height)+u'\x00\x00\x00\x00'+\
           u'\x36\x00\x00\x00'+\
         u'\x28\x00\x00\x00'+rev_num(width)+rev_num(height)+\
         u'\x01\x00'+u'\x18\x00\x00\x00\x00\x00'+rev_num(chanels*width*height)+\
         u'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'+\
         u'\x00\x00\x00'
         
## This function converts RGP to BGR (for .bmp Pictures)

def correct(st, width, height, verbose=False):
    _st = ''
    prcnt = 0
    if verbose:
        init=now();print;print '[converting to BGR bitmap',
    init = now()
    st=st[::-1]
    for y in xrange(height):
        for x in xrange(width-1, -1, -1):
            _st+=st[(y*width+x)*3]+st[(y*width+x)*3+1]+st[(y*width+x)*3+2]
        nprcnt = y*100/height*0.5
        if nprcnt<>prcnt:
            print 50+nprcnt, '%'
            prcnt = nprcnt
    if verbose:
        print 'converted', round(now()-init,3), 's]'
    ttime = round(now()-init,3)
    return _st

## This function obtains the reversed hexadecimal string of an integer (256 --> \x00\x01)

def rev_num(num):
    st = ''
    hnum = '{:0>8s}'.format(hex(num)[2:])
    for x in xrange(3, -1, -1):
        st+=unichr(int(hnum[x*2:x*2+2],16))
    return st

class gen_bmp(threading.Thread):
    def __init__(self, st, width, height, bpp, test, __bytes, e=None, _init=0,
                 fname='', mem=None, verbose=False):
        threading.Thread.__init__(self)
        self.st, self.width, self.height, self.bpp, self.test, self.__bytes = \
             st,      width,      height,      bpp,      test,      __bytes
        self.e, self._init = e, _init
        self.fname = fname
        self.fin = False
        self.mem = mem
        self.image = None
        self.verbose = verbose

    def run(self):
        if self.verbose:
            init = now();print;print '[completing bmp',
        self.st = comp_bmp(self.st, self.width, self.height, self.bpp, self.__bytes)
        if self.verbose:
            print 'complete', round(now()-init,3),'s]',

        p = ImageFile.Parser()

        p.feed(self.st.encode('iso-8859-1'))

        im = p.close()
        if not(self.fname):
            print 'no fname'
            path = 'C:/Pictures/colours/'
            if not os.path.lexists(path):
                os.makedirs(path)

            fname = [path+"colours_"+'{:0>4d}'.format(self.test)+"_"+str(self.width)+"x"+str(self.height)+\
                    ("_tmp" if not(self.e) else "")+\
                    ".png"]
            if(self.e)and(self.width>256):
                self.fin = True
                try:
                    os.remove(path+"colours_"+'{:0>4d}'.format(self.test)+"_"+str(self.width)+"x"+str(self.height)+\
                          "_tmp.png")
                except WindowsError:pass
            else:
                self.fin = False
        else:
            fname = self.fname
        for fn in fname:im.save(fn)
        print 'saved file', fname, round(now()-self._init,3), 's]'
        if self.mem:
            self.mem.writing=False

def gen_scene(mem, width, height, frame, path='C:/tmp/tmp.png',nframes=30,
              sphere=True, rframe=None, verbose=False):
    mem.newbitmap()
    coef = 1/float(1800)
    coef2, coef3 = 2, 8
    rad = width/4.0
    width-=2*rad
    x = frame*width/float(nframes+1)
    x2 = (rframe if rframe else frame)*width/float(nframes)
    if verbose:
        init=now();print;print '[ calculating pixels',
    if sphere:
        mem.paintSphere(rad=rad,
                      origin=[
                              rad+x,
                              rad,
                              rad+10
                              ],

                      rotation=(
                                 0,
                                x2/float(width)*math.pi*2,
                                -x2/float(width)*math.pi*2),
                      res=[width, height])
    if verbose:
        print 'calculated', round(now()-init,2), 's ]'

class Video():

    def __init__(self,
                 binary='./ffmpeg/ffmpeg.exe',
                 ifor='rawvideo',
                 ivco='rawvideo',
                 size='480x270',
                 pfor='rgb24',
                 rate=25,
                 ofor='mp4',
                 ovco='libx264',
                 ofnm='test.mp4'
                 ):

        self.FFMPEG_BIN = binary
        self.ifor, self.ivco, self.size, self.pfor, self.rate, self.ofor = \
            ifor,       ivco,      size,      pfor,  str(rate),     ofor
        self.ovco, self.ofnm = \
             ovco,      ofnm
        self.writing = False

    def newVideo(self):
        self.writing = True
        self.p = Popen(
            [
                self.FFMPEG_BIN,
                '-y',
                '-f', self.ifor,
                '-vcodec', self.ivco,
                '-s', self.size,
                '-pix_fmt', self.pfor,
                '-r', self.rate,
                '-i', '-',
                '-an',
                '-f', self.ofor,
                '-vcodec', self.ovco,
                self.ofnm
                ],
            stdin = PIPE
            )

    def save(self, master=None, st=None):
        if not(master) and not(st):
            print 'no enough args!';
            raise
        elif (master):
            st=master.st
        else:pass
        self.p.stdin.write(st)

    def end(self):
        self.p.stdin.close()
        self.writing = False
            
if __name__ == '__main__':
    width, height = 400, 300
    p = pixels(width, height);p.newbitmap()
    init=now();print '[generating sphere',
    p.paintSphere(res=[width,height])
    print 'generated', round(now()-init,3), 's]'
    p.raster()

def _16b(a=None):return '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'+\
                        '\x00\x00\x00\x00' if not(a) else \
                        u'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'+\
                        u'\xff\xff\xff\xff'
def _32b():   return ''.join([_16b() for x in xrange(2)])
def _64b():   return ''.join([_32b() for x in xrange(2)])
def _128b():  return ''.join([_64b() for x in xrange(2)])
def _256b():  return ''.join([_128b() for x in xrange(2)])
def _512b():  return ''.join([_256b() for x in xrange(2)])
def _1024b(): return ''.join([_512b() for x in xrange(2)])
def _2048b(): return ''.join([_1024b() for x in xrange(2)])
def _4096b(): return ''.join([_2048b() for x in xrange(2)])
def _2kb():   return ''.join([_4096b() for x in xrange(2)])
def _4kb():   return ''.join([_2kb() for x in xrange(2)])
def _8kb():   return ''.join([_4kb() for x in xrange(2)])
def _16kb():  return ''.join([_8kb() for x in xrange(2)])
def _32kb():  return ''.join([_16kb() for x in xrange(2)])
def _64kb():  return ''.join([_32kb() for x in xrange(2)])
def _128kb(): return ''.join([_64kb() for x in xrange(2)])
def _256kb(): return ''.join([_128kb() for x in xrange(2)])
def _512kb(): return ''.join([_256kb() for x in xrange(2)])
def _1mb():   return ''.join([_512kb() for x in xrange(2)])
def _2mb():   return ''.join([_1mb() for x in xrange(2)])
def _4mb():   return ''.join([_2mb() for x in xrange(2)])
def _8mb():   return ''.join([_4mb() for x in xrange(2)])
##/*
def _177kb(): return _128kb()+_32kb()+_16kb()+_1024b()      #//
##*/
class Bytes():

    def __init__(self):
        
        self._16b, self._32b, self._64b, self._128b, self._256b, self._512b = \
             _16b(),    _32b(),    _64b(),    _128b(),    _256b(),    _512b()
        
        self._16kb, self._32kb, self._64kb, self._128kb, self._256kb, self._512kb = \
             _16kb(),    _32kb(),    _64kb(),    _128kb(),    _256kb(),    _512kb()
        
        self._4mb, self._2mb, self._1mb = \
             _4mb(),    _2mb(),    _1mb()

def comp_bmp(_st, width, height, bpp, __bytes=None,
             _len=None): # '...', n, n, (def:24)
    if(not(__bytes)):__bytes=Bytes()
    _b = __bytes
    st = _st
    _len, ilen = (0x36+bpp/0x8*width*height) if not _len else _len, len(st)
    _top = _len+0x1
    __512kb,     __256kb,   __128kb,   __64kb,   __32kb,   __16kb = \
    _b._512kb, _b._256kb, _b._128kb, _b._64kb, _b._32kb, _b._16kb
    __4mb, __2mb, __1mb = _b._4mb, _b._2mb, _b._1mb
##    while(len(st)<_top-0x80000):st+=__512kb;print '512kb',
##    while(len(st)<_top-0x40000):st+=__256kb;print '256kb',
##    while(len(st)<_top-0xb1):st+=_177kb();print '177kb',     
##//
    while(len(st)<_top-0x400000):st+=__4mb;print '4mb',
    while(len(st)<_top-0x200000):st+=__2mb;print '2mb',
    while(len(st)<_top-0x100000):st+=__1mb;print '1mb',
    while(len(st)<_top-0x80000):st+=__512kb;print '512kb',
    while(len(st)<_top-0x40000):st+=__256kb;print '256kb',
    while(len(st)<_top-0x20000):st+=__128kb;print '128kb',
    while(len(st)<_top-0x10000):st+=__64kb;print '64kb',
    while(len(st)<_top-0x8000):st+=__32kb;print '32kb',
    while(len(st)<_top-0x4000):st+=__16kb;print '16kb',
    while(len(st)<_top-0x2000):st+=_8kb();print '8kb',
    while(len(st)<_top-0x1000):st+=_4kb();print '4kb',
    while(len(st)<_top-0x800):st+=_2kb();print '2kb',
    while(len(st)<_top-0x400):st+=_1024b();print '1kb',
    while(len(st)<_top-0x200):st+=_512b();print '512b',
    while(len(st)<_top-0x100):st+=_256b();print '256b',
    while(len(st)<_top-0x80):st+=_128b();print '128b',
    while(len(st)<_top-0x40):st+=_64b();print '64b',
    while(len(st)<_top-0x20):st+=_32b();print '32b',
    while(len(st)<_top-0x10):st+=_16b();print '16b',
    while(len(st)<_len):st+='\x00'
    return st

def test_mem():
    max = 0.0
    for x in xrange(0x40):
        st = u''
        sst = ''
        cf = 1
        inc = 0x20000
        print '                   ', x
        while len(sst)<0x1000000:
            init = now()
            try:
                st+=sst
            
                if((now()-init)>0)and((len(sst)/float(now()-init))>max):
                    max = len(sst)/float(now()-init)
                    print len(sst), (now()-init)*7*0x1000000/float(len(sst)), max, len(sst)/float(1024),'kB'
##                    inc = 0x1
            except MemoryError:break
##                st, sst = '', ''
            sst+=''.join('\x00' for x in xrange(inc))
##            time.sleep(0.001)

def aleatCenters(a, b, c,mem):#width, height
    return [
        (
            int(math.floor(random.random()*a)),
            int(math.floor(random.random()*b))
            ) for x in range(c)
        ]
##    centers = []
##    for x in xrange(c):
##        centers.append(
##            (
##            int(math.floor(random.random()*a)),
##            int(math.floor(random.random()*b))
##                )
##            )
##        while(len(centers)>1) and (dist(centers[-1],centers[-2])>mem.rad):
##            centers[-1] = (
##                (
##                int(math.floor(random.random()*a)),
##                int(math.floor(random.random()*b))
##                    )
##                )
##    return centers

def distances(a, b, _centers):
##    print _centers
    return (
        math.sqrt((a-_centers[x][0])**2+(b-_centers[x][1])**2) \
        for x in range(len(_centers))
        )



def calcx(y, width, height, mem, arr=None):
    centers = arr
    st = u''
    for x in xrange(width):
    ##    a, b, c = 255-int(math.floor(((y*raty)+(x*ratx))/2.0)), \
    ##              int(math.floor(y*raty)), \
    ##              int(math.floor(x*ratx))
        _i = _intensities = [((255-int(math.ceil(n*255/float(mem.rad)))) \
                              if (n<mem.rad) else 0)
                             for n in distances(x, y, centers)]
    ##    a,b, c = \
    ##         int(math.floor(random.random()*255)), \
    ##         int(math.floor(random.random()*255)), \
    ##         int(math.floor(random.random()*255))
    ##    a, b, c = 0, \
    ##              int(math.floor(x*255/float(width))), \
    ##              int(math.floor((width-x)*255/float(width)))
        a, b, c = max(_i[0], _i[3], _i[5]),\
                  max(_i[1], _i[3], _i[4]), \
                  max(_i[2], _i[4], _i[5])

        if (a, b, c)<>mem.last:
            st+=mem.px2(a,b,c)
        else:
            st+=mem.lasts
    return st

def calcy(width, height, bpp, test, st, mem, gen_bmp, arr=None):
    init=now();print;print 'Generating BMP bitmap..',
    centers = arr
    prcnt = 0
    for y in xrange(height-1, -1, -1):

        st+=calcx(y, width, height, mem, centers)

        nper = ((height-y)*width)/float(width*height)
        if(nper>=prcnt+0.1):
            _init = now()
            print '[',
            prcnt = nper
            print round(prcnt*100,1),'%',
            bm = gen_bmp(st, width, height, bpp, test,mem.bytes,_init=_init)
            bm.start()
    print '[generated', round(now()-init,3), 's]'
    return st

if __name__ == '__main__':pass
##    test_mem()
##    print _1mb()
