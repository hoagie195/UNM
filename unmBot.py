from liveCapture import packetCapture


class UNMBot:
    capture = packetCapture()
    capture.start()