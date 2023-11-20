import os
import webbrowser
import ctypes
import comtypes.client
import pycaw
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume



devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# Control volume
volume.SetMasterVolumeLevel(-0.0, None)
# Unmute the volume
volume.SetMute(0, None)

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 
webbrowser.open_new(url)
