import io
import struct
hgrid = 513
vgrid = 513
filename = "/home/strangequark/testfile.bmp"
##with io.open(filename,mode='rb+') as file:
filename2 = "/home/strangequark/colormap.txt"


    
## have a dictionary called colormap which is pixel coordinate keyed
## and (r,g,b) tuple valued.  This is 24 bit color depth
## color planes originally set to 8
## setting to 1

header = { 'importantcolors':0, 'filesize':0,'undef1':0,
            'undef2':0, 'offset':54, 'headerlength':40, 'mn1':66, 
            'width':hgrid, 'height':vgrid, 'colorplanes':8, 
            'colordepth':24, 'compression':0, 'imagesize':0,
            'res_hor':0, 'res_vert':0,'palette':0, 'mn2':77 }
def padding(width, depth):
    
##    byte_len = width * depth / 8
##    pad = (4 - byte_len) % 4
    ##pad_byte = ''
    byte_len = width * depth /8
    pad = byte_len % 4
    pad = 4-pad
    for index in range(int(pad)):
      val = struct.pack("<B", 0)
      if index == 0:
          pad_byte = val
      pad_byte += val

    return pad_byte

##writestring = ""
##3.1.2 copy the header
    ##3.1.2.1 magic number

##writestring = struct.pack('<B',66)
##writestring += struct.pack('<B',77)
##
##writestring = ""

writestring = struct.pack('<B', header['mn1'])
writestring += struct.pack('<B', header['mn2'])        
writestring += struct.pack('<L', header['filesize'])
writestring += struct.pack('<H', header['undef1'])
writestring += struct.pack('<H', header['undef2'])
writestring += struct.pack('<L', header['offset'])
writestring += struct.pack('<L', header['headerlength'])
writestring += struct.pack('<L', header['width'])
writestring += struct.pack('<L', header['height'])
writestring += struct.pack('<H', header['colorplanes'])
writestring += struct.pack('<H', header['colordepth'])
writestring += struct.pack('<L', header['compression'])
writestring += struct.pack('<L', header['imagesize'])
writestring += struct.pack('<L', header['res_hor'])
writestring += struct.pack('<L', header['res_vert'])
writestring += struct.pack('<L', header['palette'])
writestring += struct.pack('<L', header['importantcolors'])

newcolor = [0,0,0]
##for i in range(vgrid-1,-1,-1):
##    for j in range(0,hgrid):
for i in range(0,vgrid,):
    for j in range(0,hgrid):
##    for i in range(vgrid-1,-1,-1):
    

        if (j,i) in colormap:
            newcolor = colormap[(j,i)]
        else:
            newcolor = (0,0,0)
        r,g,b = newcolor
        r = int(r)
        g = int(g)
        b = int(b)
        writestring += struct.pack('<BBB', b, g, r)
    writestring += padding(header['width'], header['colordepth'])
##        file.write(bin(newcolor[0]))
##        file.write(bin(newcolor[1]))
##        file.write(bin(newcolor[2]))
##writestring += padding(header['width'], header['colordepth'])
out = open(filename, 'wb')
out.write(writestring)
out.close()
