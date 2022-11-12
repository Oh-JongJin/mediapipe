import sys
import vlc

from PySide6.QtWidgets import QWidget, QFrame
from PySide6.QtCore import QObject


class VideoWidget(QWidget):

    def __init__(self, parent: QObject = None):
        super().__init__(parent)

        args = [
            '--rtsp-frame-buffer-size=400000',
            '--quiet',
            '--sout-x264-keyint=25',
        ]

        self.instance = vlc.Instance(args)
        self.instance.log_unset()

        self.media_player = self.instance.media_player_new()
        self.media_player.video_set_aspect_ratio('16:9')

        self.video_frame = QFrame()
        self.video_frame.mouseDoubleClickEvent = self.video_DoubleClickEvent

        if sys.platform == 'win32':
            self.media_player.set_hwnd(self.video_frame.winId())

    def on_camera_change(self, uri):
        # if uri[:4] == 'rtsp':
        #     self.media_player.set_media(self.instance.media_new(uri))
        #     self.media_player.play()
        # else:
        self.media_player.set_media(self.instance.media_new(uri))
        self.media_player.play()


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = VideoWidget()
    window.on_camera_change(0)
    sys.exit(app.exec())

