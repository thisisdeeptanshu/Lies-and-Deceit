from __future__ import print_function
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

sessions = AudioUtilities.GetAllSessions()
for session in sessions:
    volume = session._ctl.QueryInterface(ISimpleAudioVolume)
    print("volume atm: %s" % volume.GetMasterVolume())
    volume.SetMasterVolume(1, None)
    print("volume after change: %s" % volume.GetMasterVolume())