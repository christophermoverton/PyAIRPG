
import struct
hgrid = 2048
vgrid = 2048
filename = "/home/strangequark/testfile.bmp"
filename2 = "/home/strangequark/colormap.txt"
inp = open(filename2, 'r')
t = inp.readline()
inp.close()
t = t.split('{')
t = t[1]
t = t.split('}')
t = t[0]
t = t.split(', ')
colormap = {}
for index, i in enumerate(t):
    if index % 4 == 0:
        k0 = int(i.split('(')[1])
        
    elif index % 4 == 1:
        k = i.split(': ')
        k0 = (k0,int(k[0].split(')')[0]))
        k1 = float(k[1].split('(')[1])
    elif index % 4 == 2:
        k1 = [k1,float(i),0.0]
    elif index%4 == 3:
        k1[2] = float(i.split(')')[0])
        colormap[k0] = k1
        k0 = None
        k1 = None
##with io.open(filename,mode='rb+') as file:
    
####3.0 filewrite to file
##	##3.1 Begin the file
##	##3.1.1 open filewrite file
##ofstream file
##file.open(oname, ofstream::binary)
##if (!(file.is_open())){
##        cfile << "Target file opening error"<<endl
##        exit(0)
##}
header = { 'importantcolors':0, 'filesize':0,'undef1':0,
            'undef2':0, 'offset':54, 'headerlength':40, 'mn1':66, 
            'width':hgrid, 'height':vgrid, 'colorplanes':8, 
            'colordepth':24, 'compression':0, 'imagesize':0,
            'res_hor':0, 'res_vert':0,'palette':0, 'mn2':77 }
def padding(width, depth):
    
    byte_len = width * depth / 8
    pad = (4 - byte_len) % 4
    pad_byte = ''

    for index in range(pad):
      val = struct.pack("<B", 0)
      pad_byte += val

    return pad_byte

writestring = ""
##3.1.2 copy the header
    ##3.1.2.1 magic number

writestring += struct.pack('<B',66)
writestring += struct.pack('<B',77)

writestring = ""

writestring += struct.pack('<B', header['mn1'])
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
for i in range(vgrid):
    for j in range(0,hgrid):
##        if i == vgrid/2:
##            c = (255-i)%255
##            newcolor = [c,c,c]
##        else:
##            newcolor = [i%255,i%255,i%255]
        if (j,i) in colormap:
            r,g,b = colormap[(j,i)]
        else:
            r,g,b = newcolor
        writestring += struct.pack('<BBB', b, g, r)
    writestring += padding(header['width'], header['colordepth'])
##        file.write(bin(newcolor[0]))
##        file.write(bin(newcolor[1]))
##        file.write(bin(newcolor[2]))

out = open(filename, 'wb')
out.write(writestring)
out.close()
