#! /usr/bin/python
# -*- coding: utf-8 -*-

import ctypes
import platform
import sys
import time
import subprocess
import commands
import json

MAX_DATA_LENGTH = 2048

system = platform.system()
if system == "Linux":
    sdk_lib = ctypes.cdll.LoadLibrary("/root/RF/FSP_SSS_STREAM/libclient_sdk_c.so")
elif system == "Windows":
    sdk_lib = ctypes.cdll.LoadLibrary("libclient_sdk_c.dll")
else:
    sys.exit("Sorry, platform {0} was not support yet".format(system))

class sample_callback(ctypes.Structure):
    _fields_ = [("data", ctypes.c_void_p),
                ("data_len", ctypes.c_uint),
                ("from_id", ctypes.c_uint),
                ("from_param", ctypes.c_uint)]

class client_sdk(object):
    def __init__(self):
        self._sdk_lib = sdk_lib
        self._handle = ctypes.c_ulonglong()

    def init(self):
        func = self._sdk_lib.CreateSDKInstance
        func.restype = ctypes.c_ulonglong

        self._handle = func()

    def cleanup(self):
        func = self._sdk_lib.DestroySDKInstance
        func.argtypes = [
            ctypes.c_ulonglong
        ]

        func(self._handle)

    def login(self, cp_addr, client_token):
        func = self._sdk_lib.Login
        func.argtypes = [
            ctypes.c_ulonglong,
            ctypes.c_char_p,
            ctypes.c_char_p
        ]
        func.restype = ctypes.c_uint

        return func(self._handle, cp_addr, client_token)

    def logout(self):
        func = self._sdk_lib.Logout
        func.argtypes = [
            ctypes.c_ulonglong
        ]

        func(self._handle)

    def publish_video(self, stream_id, publish_token):
        func = self._sdk_lib.PublishVideo
        func.argtypes = [
            ctypes.c_ulonglong,
            ctypes.c_char_p,
            ctypes.c_char_p
        ]
        func.restype = ctypes.c_void_p

        return func(self._handle, stream_id, publish_token)

    def publish_audio(self, stream_id, publish_token):
        func = self._sdk_lib.PublishAudio
        func.argtypes = [
            ctypes.c_ulonglong,
            ctypes.c_char_p,
            ctypes.c_char_p
        ]
        func.restype = ctypes.c_void_p

        return func(self._handle, stream_id, publish_token)

    def unpublish(self, stream_id):
        func = self._sdk_lib.Unpublish
        func.argtypes = [
            ctypes.c_ulonglong,
            ctypes.c_char_p
        ]

        func(self._handle, stream_id)

    def subscribe_video(self, stream_id, subscribe_token, cb):
        func = self._sdk_lib.SubscribeVideo
        func.argtypes = [
            ctypes.c_ulonglong,
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint)
        ]
        func.restype = ctypes.c_uint

        return func(self._handle, stream_id, subscribe_token, cb)
    
    def subscribe_video_callback(self,stream_id,subscribe_token):
        def on_subscribe_video(data, data_len, from_id, from_param):
            print "ssssssssSSSSSSSSSS",data_len, from_id, from_param

        SUBSCRIBE_VIDEO_FUNC = ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint)
        cb_fn = SUBSCRIBE_VIDEO_FUNC(on_subscribe_video)

        return self.subscribe_video(stream_id, subscribe_token, cb_fn)

    def subscribe_audio(self, stream_id, subscribe_token, cb):
        func = self._sdk_lib.SubscribeAudio
        func.argtypes = [
            ctypes.c_ulonglong,
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint)
           # ctypes.CFUNCTYPE(None, None, ctypes.POINTER(sample_callback)),
        ]
        func.restype = ctypes.c_uint

        return func(self._handle, stream_id, subscribe_token, cb)

    def subscribe_audio_callback(self,stream_id,subscribe_token):
        def on_subscribe_audio(data, data_len, from_id, from_param):
            print "aaaaaaaaaSSSSSSSSSS",data_len, from_id, from_param

        SUBSCRIBE_AUDIO_FUNC = ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint)
        cb_fn = SUBSCRIBE_AUDIO_FUNC(on_subscribe_audio)

        return self.subscribe_audio(stream_id, subscribe_token, cb_fn)	
	# def subscribe_audio_callback(self,stream_id,subscribe_token):
        # def on_subscribe_audio(response):
            # print response.data_len
        # sample = sample_callback()
        # CALLBACK = ctypes.CFUNCTYPE(None,ctypes.POINTER(sample))
        # cb_fn = CALLBACK(on_subscribe_audio)
        # ret = subscribe_audio(stream_id,subscribe_token,cb_fn)
        # return ret

    def unsubscribe(self, stream_id):
        func = self._sdk_lib.Unsubscribe
        func.argtypes = [
            ctypes.c_ulonglong,
            ctypes.c_char_p,
        ]

        func(self._handle, stream_id)

    def play_video(self, pathname, sink):
        func = self._sdk_lib.PlayVideo
        func.argtypes = [
            ctypes.c_char_p,
            ctypes.c_ulonglong,
            ]
        func.restype = ctype.c_uint
		
        return func(pathname, sink)
		
    def stop_video(self):
        func = self._sdk_lib.StopVideo
        func()
		
    def play_audio(self, pathname, sink):
        func = self._sdk_lib.PlayAudio
        func.argtypes = [
            ctypes.c_char_p,
            ctypes.c_ulonglong,
            ]
        func.restype = ctypes.c_uint
		
        return func(pathname,sink)
		
    def stop_audio(self):
        func = self._sdk_lib.StopAudio
        func()
		
if __name__=='__main__':
    a = client_sdk()
    a.init()
#    x = sys.argv[1]
#    b = a.login(x,"1;xxx")
#    print b
    lscommand =' curl -H "Content-Type:application/json;charset=UTF-8" --http2 -s -k --data \'{"sequence":1,"requestType":1,"appID":"app123","verificationCode":"vc123"}\' https:/192.168.7.160:8444/api/v1.0/login'
    (status,output) = commands.getstatusoutput(lscommand)
    print output
    c = json.loads(output)
    d = c["appToken"]
    print d
    cscommand = ' curl -H "Content-Type:application/json;charset=UTF-8" --http2 -s -k --data \'{"sequence":1,"requestType":1,"streamType":1,"streamProperty":1,"appToken":"%s"}\' https:/192.168.7.160:8444/api/v1.0/create_stream'%d
    print cscommand
    (status1,output1) = commands.getstatusoutput(cscommand)
    print output1
    e = json.loads(output1)
    f = e["stream"]
    print f
    g = f["streamID"]
    h = f["streamPublishToken"]
    i = f["streamSubscribeToken"]
    print g,h,i
    a.login("192.168.7.73:54321","1;cyn")
    j = a.publish_audio(g,h)
    print j
    filepath = "/usr/lib/python2.7/site-packages/client_sdk/audio.dat"
    k = a.play_audio(filepath,j)
    print k
    time.sleep(3)
    aa =client_sdk()
    aa.init()
    aa.login("192.168.7.73:54321","1;ling")
    time.sleep(2)
    l = aa.subscribe_audio_callback(g,i)
    print "SUB,%d"%l
    time.sleep(6)
    a.stop_audio()
    sys.exit(5)
