import cv2
import numpy as np
from scapy.all import *


size=320
rayon=10

packets = rdpcap('capture.pcap')

video = cv2.VideoWriter('illuminated.avi',cv2.VideoWriter_fourcc(*'DIVX'), 5, (size+1, size+1))

def process_packet_pair(data1, data2):
    img = np.ones((size+1, size+1, 3), dtype=np.uint8)
    img = 255 * img

    universe1, universe2 = data1[14], data2[14]
    if universe1 == 0:
        dmx_data1, dmx_data2 = data1, data2
    else:
        dmx_data1, dmx_data2 = data2, data1


    dmx_channels = dmx_data1[18:18+3*16*10+1] + dmx_data2[18:18+3*16*6+1]

    i=0
    for led_red, led_green, led_blue in zip(dmx_channels[0::3], dmx_channels[1::3], dmx_channels[2::3]):
        led_color = (led_blue, led_green, led_red)
        if (i//16) & 1:
            # DMX go rigth -> left
            sens = -1
            start = size - rayon
        else:
            # DMX go rigth -> left
            sens = 1
            start = rayon
        #cv2.circle(img, (start + sens*2*rayon*(i%16), rayon + 2*rayon*(i//16)), rayon-1, led_color, -1)
        cv2.rectangle(img, (start - rayon + sens*2*rayon*(i%16), 2*rayon*(i//16)), (start + rayon + sens*2*rayon*(i%16), 2*rayon + 2*rayon*(i//16)), led_color, -1)
        i += 1
    
    video.write(img)

for i in range(1, len(packets)-1, 2):
    process_packet_pair(packets[i].load, packets[i+1].load)
