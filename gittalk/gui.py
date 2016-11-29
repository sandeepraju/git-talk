import Tkinter as tk
import os
from capture import FFmpeg, VIDEO, SCREEN
from upload import upload_to_youtube


class GUI:

    def __init__(self, commit_message):
        self.commit_message = commit_message
        self.root = tk.Tk()
        self.proc = None
        self.frame = None
        self.ffmpeg = None

        # start gui
        self.addFrame1()
        self.show()

    def show(self):
        '''  '''
        w = 300  # width for the Tk root
        h = 150  # height for the Tk root

        # get screen width and height
        ws = self.root.winfo_screenwidth()  # width of the screen
        hs = self.root.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        # self.root.lift()
        # self.root.attributes("-topmost", True)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.mainloop()

    def addFrame1(self):
        '''  '''
        self.root.title('GitTalk')

        # FRAME 1
        self.frame = tk.Frame(self.root)
        tk.Button(self.frame, text='Screen Capture', command=lambda: self.addFrame2(
            SCREEN)).pack(anchor=tk.N, fill=tk.BOTH)
        tk.Button(self.frame, text='Web Cam Recording', command=lambda: self.addFrame2(
            VIDEO)).pack(anchor=tk.S, fill=tk.BOTH)
        self.frame.pack(side=tk.TOP, anchor=tk.W, expand=1, fill=tk.X)
        # -----------

    def addFrame2(self, type):
        '''  '''
        self.frame.destroy()

        # FRAME 2
        self.frame = tk.Frame(self.root)
        tk.Button(self.frame, text='Start', command=lambda: self.start_record(
            type)).pack(anchor=tk.N, fill=tk.BOTH)
        self.frame.pack(side=tk.TOP, anchor=tk.W, expand=1, fill=tk.X)
        # -----------

    def addFrame3(self):
        '''  '''
        self.frame.destroy()

        # FRAME 3
        self.frame = tk.Frame(self.root)
        tk.Button(self.frame, text='Stop', command=self.stop_record).pack(anchor=tk.N, fill=tk.BOTH)
        self.frame.pack(side=tk.TOP, anchor=tk.W, expand=1, fill=tk.X)
        # -----------

    def addFrame4(self):
        '''  '''
        self.frame.destroy()

        # FRAME 4
        self.frame = tk.Frame(self.root)
        tk.Label(self.frame, text="Uploading your video. Please wait...").pack(anchor=tk.CENTER)
        # self.button_1 = tk.Button(self.frame, text='Stop', command=self.stop_record).pack(
        #     anchor=tk.S, fill=tk.BOTH)
        self.frame.pack(side=tk.TOP, anchor=tk.W, expand=1, fill=tk.X)
        # -----------

    def start_record(self, type):
        # TODO: CHECK IF ALREADY RECORDED - ASK FOR OVERWRITE
        # print 'RECORD HERE'
        self.addFrame3()
        # self.root.iconify()
        self.ffmpeg = FFmpeg()
        self.proc = self.ffmpeg.start(type, os.path.join(
            os.environ['HOME'], '.gittalk/output.mp4'))

    def stop_record(self):
        # TODO: GET FILE PATH AND PASS IT TO UPLOADING FUNCTION
        self.addFrame4()

        if self.proc:
            self.ffmpeg.stop(self.proc)

        # upload to youtube here
        video_file_path = os.path.join(
            os.environ['HOME'], '.gittalk/output.mp4')
        upload_to_youtube(
            video_file_path, self.commit_message, self.commit_message)

        self.root.destroy()
