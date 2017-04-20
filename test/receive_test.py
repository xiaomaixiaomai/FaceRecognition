# encoding: utf-8

"""
@author: liubo
@software: PyCharm Community Edition
@file: receive_test.py
@time: 2016/11/16 10:48
@contact: ustb_liubo@qq.com
@annotation: receive_test
"""
import sys
import logging
from logging.config import fileConfig
import os
from PIL import Image
from StringIO import StringIO
import time
import tornado.ioloop
import tornado.web
import pdb
import json
import hashlib
import numpy as np
import cv2


reload(sys)
sys.setdefaultencoding("utf-8")
# fileConfig('logger_config.ini')
# logger_error = logging.getLogger('errorhandler')

result = 'faces num: 3\n702.0000,100.0000,113.0000,129.0000\n-2.1235,-2.4381,0.8430,0.0933,0.5992,0.2447,-1.3567,1.9776,1.4637,-2.1003,-0.1953,0.3855,0.1598,-0.2763,0.9677,-0.2265,0.2883,-1.1091,0.8081,-1.7453,-1.2697,-1.5282,1.5782,-0.6568,0.2870,-0.1589,1.2638,-1.4515,-0.0160,-1.8047,-2.1090,-2.2912,0.1238,0.2171,3.1681,2.2566,1.6125,1.2370,0.7433,-0.8322,0.2310,1.1002,0.7396,-0.5005,0.5717,2.0278,2.4278,0.5549,-0.4268,0.9484,-2.0245,-0.8077,1.3822,-0.3189,0.9401,0.3748,0.4586,1.0103,-0.6384,-0.2416,-1.0178,-0.2327,1.4179,-0.5712,1.0238,3.4909,1.1707,0.0589,0.9987,-0.6071,1.3602,3.0252,-0.0665,-0.9468,-0.8002,-1.2177,1.6999,-0.6238,-0.0454,-1.1060,-1.4943,-1.3460,-0.8763,-1.5079,1.5125,1.6069,0.6112,-0.7855,0.7335,-0.0766,2.6400,2.0141,0.9342,-0.4511,0.1471,0.3833,-0.9021,0.4714,0.2485,-0.5610,-2.5850,-1.5308,0.4464,-1.1034,-0.7176,-1.2987,-1.8428,-0.7796,1.2022,-1.0939,-0.5144,-0.7478,0.0450,0.2560,1.9794,0.3467,1.5295,-0.2892,0.3615,1.5242,-0.4732,-2.0827,1.7497,-1.5827,-0.1657,2.6541,-1.0002,-0.7709,-0.3521,0.6389,-0.1112,-0.3781,-1.6488,-1.7090,1.5853,-0.5146,-3.3066,-0.2181,0.1433,0.4683,2.2214,0.4739,0.3666,-0.3018,2.8634,0.2962,-0.3477,-0.4154,-0.6722,1.1900,-0.6394,-0.6886,0.0846,-0.1421,0.2603,2.0240,2.0324,1.0164,-2.1253,0.5716,-0.4861,-0.5114,0.6221,0.5003,-0.3685,0.8010,0.9648,0.9572,-0.5956,0.6562,1.3485,0.7392,-3.0018,-1.2163,2.7583,-0.2059,1.4020,-0.6845,0.3670,3.1120,1.5469,0.7820,0.8421,-0.2222,0.6569,-1.4414,1.8774,-1.9516,-2.0429,-0.3534,2.0528,1.1087,-1.6804,0.0701,-1.7195,0.2540,0.1915,-1.3078,-0.7061,0.9879,0.0277,2.5368,-0.3115,-2.5965,1.1882,0.1035,0.5258,1.7114,-0.5754,0.1514,-0.1484,-1.1597,0.1207,1.1407,0.0056,-0.4843,-2.6300,-0.2397,2.5710,-0.7952,0.7572,0.6471,-0.7887,-0.5851,-0.9266,-1.2609,0.3861,0.1311,-1.2959,0.7854,-3.0060,-1.6603,-0.7266,0.5702,-0.0248,-1.9566,1.0472,-1.8397,0.5752,-0.9358,1.8838,2.3550,-0.4924,-1.6580,-2.0017,-2.0128,-0.4899,-0.7450,2.1264,0.2778,0.1306,-1.1832,-0.8643,-1.8086,-1.3468,-1.3821,\n419.0000,46.0000,121.0000,134.0000\n-3.2611,-1.2546,0.0773,-1.1134,2.0214,1.1228,-2.1380,0.2988,-0.7680,-0.5010,-0.8115,-0.5861,-0.6413,-0.4462,1.1788,0.8065,-1.5848,-1.4617,0.0504,-3.1107,-0.3624,0.5252,0.2439,-2.3228,0.2515,-0.9350,-0.4812,-2.3518,-0.0341,-1.6399,1.1307,-1.4668,1.3934,-1.2012,3.5757,0.5274,0.4082,2.0687,0.3450,0.7906,-2.2188,-1.6306,-0.9603,0.7998,-1.8995,-0.4177,-2.7029,0.9116,-0.8375,3.5617,-3.6185,-2.8941,1.7536,-2.0049,0.8013,-0.2950,-1.9934,0.2811,-0.1004,0.9364,-1.0375,-0.2277,-1.0104,-2.3148,0.4318,3.8640,-0.7802,-0.0863,-0.5965,-1.8741,0.2022,1.6585,-1.7599,0.7063,1.1098,-0.0112,-0.2187,-1.3945,0.9789,-1.2082,-0.3943,-0.1798,1.3414,-0.8812,-0.8659,0.7476,-3.1950,-1.5094,2.5602,-1.7395,-1.0980,0.4157,-0.3339,0.3033,-2.4633,2.6623,-1.2291,0.0597,-2.0189,-2.1406,-2.1991,-1.5171,0.6688,1.5486,1.1275,-0.2328,0.0083,-0.8322,0.7417,1.9015,-2.6746,-1.4898,1.5030,0.3861,2.7640,0.1664,1.1711,-0.6762,2.2639,0.7295,0.4092,2.3111,1.3017,-0.8982,0.3691,-0.6952,-0.8303,-1.0989,-1.0770,-2.3494,-0.0059,0.5800,-0.8441,-2.2043,-1.5956,-0.4790,-1.8351,-1.7019,-0.4792,-1.6274,2.3809,-0.4397,1.5552,-1.6691,-0.8361,-3.4254,-0.3799,-1.3693,-1.2964,2.2225,0.6724,-1.7933,-1.2594,-4.2661,-1.8711,1.1016,-1.7725,-1.9780,0.2959,-2.0925,2.0027,-0.7918,-0.5824,0.3708,0.0776,-0.5998,-0.4131,-0.3036,2.0547,-1.7051,0.1858,-0.7970,-3.4776,-1.3023,0.6398,-0.9456,1.2927,-1.2766,0.6523,1.6596,-0.4646,-1.1463,-0.8458,-1.3631,0.3174,-2.1269,-0.7072,-1.3842,0.3996,1.1862,0.8913,-1.2673,-1.8370,-0.2080,-2.5732,0.6574,-0.2148,-0.4961,-2.5145,-0.9509,-1.1034,1.1207,-0.2263,1.1817,-0.2385,0.2374,-0.2389,1.1508,-0.8291,1.0531,0.1260,1.2880,-1.7885,-0.5712,0.7044,0.9129,-1.6811,0.8777,-1.4303,-2.8434,-1.1884,-0.7909,-2.3368,1.7269,-0.3800,0.5377,-2.8856,1.2873,-3.4690,-0.2098,-0.2039,-3.0359,-0.1231,-3.6405,2.4918,1.3336,-1.1337,-2.8049,-0.4824,-0.3112,0.0592,-0.9847,-0.9808,-1.6253,-0.9174,-1.4758,-1.8991,1.0703,-0.7966,1.1044,1.6450,0.8961,-0.9278,-2.3289,-2.3698,0.8072,\n917.0000,221.0000,101.0000,123.0000\n-3.1450,0.3242,3.3090,-0.0450,2.4944,-0.2140,-0.3353,-0.8770,-0.2802,-2.0135,0.4033,0.1143,-1.6856,-0.3076,0.0477,0.3208,-1.4628,0.8608,-1.3910,-3.3224,0.3842,-1.9238,0.6336,-3.0880,0.3882,-0.6281,-1.2386,-3.2552,0.8406,-1.8620,-0.1130,-1.9442,2.3832,0.1802,1.3894,1.4701,3.4019,0.7332,0.9534,0.4591,-0.9853,-1.1040,-1.9616,-0.1222,-0.3048,-1.7620,-0.8778,-0.4873,-1.9893,1.7706,-2.8702,-2.0720,1.2723,-3.0394,-1.0261,-0.8332,-1.5563,0.4836,-0.5421,-0.2934,-1.0230,-1.3740,-0.2663,-3.3535,-1.5510,1.7679,-2.7345,0.4496,-0.2717,-2.0008,0.6568,2.1079,-0.4059,-0.3240,-0.3906,-1.5174,-0.4400,-1.3166,1.3773,-1.1420,1.7359,-1.2685,0.9717,-0.8330,-1.1966,0.8406,-1.2926,-2.4072,2.6879,-0.2693,-0.9445,0.5365,-0.7347,1.6741,-1.6189,0.6340,-2.4802,1.1743,-3.0367,-3.4329,-1.4470,-2.5913,1.4612,0.0001,0.0128,-2.3998,1.4283,0.7825,0.9465,0.3743,0.1189,-1.4195,0.5741,-0.6462,1.3051,1.8961,-1.4770,-0.9087,1.0899,3.3442,0.9108,1.1214,-0.8793,-1.1716,1.4357,2.5344,-2.5213,0.0761,-0.2025,-2.7067,1.5638,-0.8218,-0.8569,-1.7734,-0.3905,0.4554,-0.5314,-0.0013,0.3725,0.6310,0.9951,-0.4019,-0.3967,-2.0399,0.9542,-0.4275,-0.7315,-1.0878,-2.6502,1.0347,0.2880,-2.4566,-0.9700,-1.7138,-0.5104,2.2758,-0.7854,-1.2448,-0.3410,-0.4078,1.9755,-0.4593,-0.1677,-0.6329,-0.9325,-1.0986,0.7526,0.9026,0.7567,-0.5162,-0.1098,0.0511,-2.3675,-0.6732,-0.5391,-2.5016,-0.7926,-0.7281,0.1722,1.2840,0.1266,-0.3790,-2.0832,-0.8338,1.6940,-0.2535,-0.6077,-1.4056,1.2314,-0.0980,-0.2776,1.3509,-2.9080,-0.3091,-3.5190,-0.4649,0.0823,-0.1436,1.1929,0.3334,0.2550,0.4805,0.8467,-0.1482,-2.4948,-1.3806,1.3285,0.6188,-0.2616,0.8721,0.4269,1.1828,0.7418,-0.0127,1.0162,2.2014,-0.8736,-0.7498,0.6199,-1.4513,-0.1472,-0.9567,-0.9419,-0.1925,-0.0104,0.2197,-0.6835,0.4697,0.7839,0.7233,1.6206,-2.4947,-0.1282,-2.3784,0.5695,0.4202,-2.1777,-3.8906,-0.5304,-1.0136,1.5317,-0.2005,-1.5773,-1.7565,-2.0868,-3.3382,-3.4438,-0.5646,1.0142,0.7704,-0.5043,1.5319,-0.8204,0.4866,-3.3093,0.2440,\n'
# result = ''

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        pic_binary_data = self.request.body
        img_buffer = StringIO(pic_binary_data)
        img_array = np.array(Image.open(img_buffer))
        img_array_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        self.write(result)



if __name__ == '__main__':
    port = 7777
    application = tornado.web.Application([(r"/", MainHandler), ])
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()

