import subprocess

AUDIO, VIDEO, SCREEN = 0, 1, 2
LINUX, MAC, WINDOWS = 0, 1, 2

# src: http://stackoverflow.com/a/377028/1044366
def which(program):
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

def detectPlatform():
    import sys
    if sys.platform.startswith('linux'):
        return LINUX
    elif sys.platform.startswith('win') or sys.platform.startswith('cyg'):
        return WINDOWS
    elif sys.platform.startswith('darwin'):
        return MAC
    else:
        return None

class FFmpeg(object):
    def __init__(self):
        # check if ffmpeg is installed on the system
        if not which('ffmpeg'):
            raise Exception('FFmpeg is not installed!')

        self.pid = 0

        self.formats = {
            LINUX: 'video4linux2',
            MAC: 'avfoundation',
            WINDOWS: ''
        }

        self.audioDevices = {
            LINUX: '', # TODO
            MAC: 'none:0'
        }

        self.videoDevices = {
            LINUX: '/dev/video0',  # try to detect this,
            MAC: '0:0'
        }

        self.screenDevices = {
            LINUX: '', # TODO
            MAC: '1:none'
        }

        platform = detectPlatform()

        self.cmds = {
            AUDIO: [
                ('-f', self.formats[platform]),
                ('-i', self.audioDevices[platform]),
                ('-y',),
                ('-vn',),
                ('-c:a', 'aac')
            ],
            # VIDEO: [
            #     ('-f', self.formats[platform]),
            #     ('-c:v', 'rawvideo'),
            #     ('-i', self.videoDevices[platform]),
            #     ('-qscale:v', '5'),
            #     ('-y',),
            #     ('-f', 'mp4'),
            #     ('-c:v', 'mpeg4'),
            #     ('-c:a', 'aac') 
            # ],
            VIDEO: [
                ('-r', '30'),
                ('-f', self.formats[platform]),
                ('-i', self.videoDevices[platform]),
                ('-y',)
            ],
            SCREEN: [
                ('-r', '30'),
                ('-f', self.formats[platform]),
                ('-c:v', 'rawvideo'),
                ('-an',),
                ('-i', self.screenDevices[platform]),
                ('-f', self.formats[platform]),
                ('-vn',),
                ('-i', self.audioDevices[platform]),
                ('-qscale:v', '5'),
                ('-y',),
                ('-f', 'mp4'),
                ('-c:v', 'mpeg4'),
                ('-c:a', 'aac')
            ]
        }


    def generateCmdString(self, kind, outputPath):
        cmd = ['ffmpeg']
        for item in self.cmds[kind]:
            cmd.extend(item)

        cmd.append(outputPath)

        return cmd

    def run(self, cmd):
        # import sys
        # p = subprocess.Popen(cmd, stdin=subprocess.PIPE, 
        #     stdout=sys.stdout, stderr=sys.stdout)
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        self.pid = p
        return p

    def kill(self, pid):
        p = subprocess.Popen(['kill', '-15', str(pid)], stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p.wait()

    def stop(self, proc):
        self.kill(proc.pid)

    def start(self, kind, outputPath):
        if kind not in (AUDIO, VIDEO, SCREEN):
            raise Exception("Invalid option")

        cmd = self.generateCmdString(kind, outputPath)
        # with open('/tmp/gt.log', 'a') as log:
        #     log.write(' '.join(cmd) + '\n')
        return self.run(cmd)
