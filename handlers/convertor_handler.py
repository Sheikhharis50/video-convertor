from utils.helpers import log
from converter import Converter
import os

INPUTS_DIR = 'inputs'
OUTPUTS_DIR = 'outputs'


class ConvertHandler:
    def __new__(cls, filename):
        path = os.path.join(INPUTS_DIR, filename)
        if not os.path.isfile(path):
            log('Invalid filename or file does not exists: "{}"'.format(path))
            return None
        return super().__new__(cls)

    def __init__(self, filename):
        self.conv = Converter()
        self.filename = filename
        self.path = os.path.join(INPUTS_DIR, filename)
        self.input = self.conv.probe(self.path)
        self.supported_formats = [
            'ogg', 'avi',
            'mkv', 'webm',
            'flv', 'mov',
            'mp4', 'mpeg'
        ]

    def get_format(self):
        return self.input.format.format

    def get_duration(self):
        return self.input.format.duration

    def get_streams(self):
        return len(self.input.streams)

    def get_video_codec(self):
        return self.input.video.codec

    def get_video_width(self):
        return self.input.video.video_width

    def get_video_height(self):
        return self.input.video.video_height

    def get_video_dimensions(self):
        return f'{self.get_video_width()}x{self.get_video_height()}'

    def get_audio_codec(self):
        return self.input.audio.codec

    def get_audio_channels(self):
        return self.input.audio.audio_channels

    def convert(self, video_format='mp4', audio_format='mp3'):
        if not video_format in self.supported_formats:
            log('Cannot support given format: "{}"'.format(video_format))
            return None
        options = {
            'format': video_format,
            'audio': {
                'codec': audio_format,
                # 'samplerate': 11025,
                # 'channels': 2
            },
            'video': {
                'codec': 'h264',
                # 'width': 720,
                # 'height': 400,
                # 'fps': 15
            },
            # 'subtitle': {
            #     'codec': 'copy'
            # },
            # 'map': 0
        }
        output_path = os.path.join(OUTPUTS_DIR, '{}.{}'.format(
            self.filename.split(".")[0],
            video_format
        ),)
        convert = self.conv.convert(
            self.path,
            output_path,
            options
        )

        for timecode in convert:
            print(f'\rConverting ({timecode:.2f}) ...')
