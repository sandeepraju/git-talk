import os
import Tkinter, Tkconstants, tkFileDialog
from gittalk import upload_youtube

class VideoRecordControlFrame(Tkinter.Frame):
    def __init__(self, root):
        self._root = root
        Tkinter.Frame.__init__(self, self._root)

        # options for buttons
        button_opt = {
            'fill': Tkconstants.BOTH, 
            'padx': 5, 
            'pady': 5
        }

        Tkinter.Button(self, text='Select Video', 
            command=self.ask_open_filename).pack(**button_opt)

    def ask_open_filename(self):
        file_opt = {
            # 'defaultextension': '.mp4',
            'filetypes': [
                ('All files', '.*'), 
                ('MPEG 4', '.mp4'),
                ('Windows Media Video', '.wmv'),
                ('Web Media', '.webm'),
                ('Flash Video', '.flv'),
                ('Matroska Video', '.mkv'),
                ('Quick Time Video', '.mov')
            ],
            'initialdir': os.getcwd(),
            'parent': self._root,
            'title': 'Select a video file to upload'
        }
        filename = tkFileDialog.askopenfilename(**file_opt)
        # print 'TODO: upload file: {}'.format(filename)

        url = upload_youtube.upload_youtube(filePath=str(filename), title='put title here', description='line1 description\nline2 description')
        # upload_youtube.upload_youtube(filename)
        
        # close the window
        self._root.destroy()

        print url