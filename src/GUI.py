from Tkinter import *
import tkFileDialog
import os

class GUI(Frame):


	def __init__(self):
		self.root = Tk()
		self.v1 = IntVar()
		self.v2 = IntVar()
		self.file_title = StringVar()
		self.file_path = ''
		self.file_url = ''
		self.root.title('GitTalk')
		self.done = False

		# TITLE FRAME
		title_frame = Frame(self.root)
		Label(title_frame, justify=LEFT, text='Enter recording title').pack(side=LEFT)
		Entry(title_frame, textvariable=self.file_title, width=15).pack(side=LEFT)
		title_frame.pack(side=TOP, anchor=W, expand=1, fill=X)
		# -----------

		# OPTION FRAME
		option_frame = Frame(self.root)
		Label(option_frame, justify=LEFT, text='Select an option').pack(side=TOP, anchor=W)
		Radiobutton(option_frame, text='Existing file', padx=15, variable=self.v1, value=1, command=self.popup_browse).pack(anchor=W, side=TOP)
		Radiobutton(option_frame, text='Existing url', padx=15, variable=self.v1, value=2, command=self.popup_url).pack(anchor=W, side=TOP)
		Radiobutton(option_frame, text='New recording', padx=15, variable=self.v1, value=3, command=self.popup_record).pack(anchor=W, side=TOP)		
		option_frame.pack(side=TOP, anchor=W, expand=1, fill=BOTH)
		# -----------

		# BUTTON FRAME
		button_frame = Frame(self.root)		
		Button(button_frame, text='Finish', command=self.finish).pack(side=RIGHT)
		Button(button_frame, text='Cancel', command=self.cancel).pack(side=RIGHT)
		button_frame.pack(side=TOP, anchor=W, expand=1, fill=X)
		# -----------

		self.root.mainloop()


	def finish(self):
		val = self.v1.get()
		title = self.file_title.get()
		if title == '':
			title = 'Default title here'
		print 'Title: '+title
		if val == 0:
			print 'No option selected'
		if val == 1:
			print 'Using file: '+self.file_path
		if val == 2:
			print 'Using url: '+self.file_url
		if val == 3:
			print 'Using recorded file '+self.file_path

		# TODO: PASS FILE_PATH TO UPLOAD_YOUTUBE OR PASS FILE_URL TO GIT HOOK

		self.done = True
		self.root.destroy()


	def cancel(self):
		self.root.destroy()


	# GET METHODS
	# -----------------------------------------------------------
	def get_input(self):
	""" returns tuple. first element is file path/url, second element specifies whether to upload or not"""

		if not self.is_done():
			raise Exception

		val = self.v1.get()
		if val == 0:
			print 'User has not selected anything yet'
			raise Exception
		if val == 1 or val == 3:
			print 'Upload file from: '+self.file_path
			return (self.file_path, True)
		if val == 2:
			print 'Use URL: '+self.file_url
			return (self.file_url, False)

	def is_done(self):
		return self.done



	# FILE SELECTION FUNCTIONS
	# -----------------------------------------------------------
	def popup_browse(self):
		self.browse_window = Tk()
		self.browse_window.title('Enter file path')
		self.path_entry = Entry(self.browse_window, width=30)
		self.path_entry.pack(side=LEFT, padx=5, pady=5)
		Button(self.browse_window, text='Browse', command=self.ask_open_filename).pack(side=LEFT, padx=5)
		Button(self.browse_window, text='Use', command=self.destroy_browse).pack(side=LEFT, padx=5)
		self.browse_window.mainloop()

	def ask_open_filename(self):
		self.file_opt = {# 'defaultextension': '.mp4',
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
            'parent': self.browse_window,
            'title': 'Select a video file to upload'}
		self.path = tkFileDialog.askopenfilename(**self.file_opt)
		self.path_entry.insert(0, self.path)

	def destroy_browse(self):
		self.file_path = self.path_entry.get()
		self.browse_window.destroy()
	# -----------------------------------------------------------


	# URL FUNCTIONS
	# -----------------------------------------------------------
	def popup_url(self):
		self.url_window = Tk()
		self.url_window.title('Enter URL')
		self.url_entry = Entry(self.url_window, width=30)
		self.url_entry.pack(side=LEFT, padx=5, pady=5)
		Button(self.url_window, text='Use', command=self.destroy_url).pack(side=LEFT)
		self.url_window.mainloop()

	def destroy_url(self):
		self.file_url = self.url_entry.get()
		self.url_window.destroy()
	# -----------------------------------------------------------


	# RECORD FUNCTIONS
	# -----------------------------------------------------------
	def popup_record(self):
		record_window = Tk()
		record_window.title('Record')

		option_frame2 = Frame(record_window)
		Radiobutton(option_frame2, text='Audio & Screen Capture', padx=15, variable=self.v2, value=1).pack(anchor=NW, side=TOP)
		Radiobutton(option_frame2, text='Audio & Webcam', padx=15, variable=self.v2, value=2).pack(anchor=NW, side=TOP)
		Radiobutton(option_frame2, text='Audio', padx=15, variable=self.v2, value=3).pack(anchor=NW, side=TOP)

		self.status = Label(record_window, text='Ready', justify=LEFT)
		self.status.pack(side=TOP, anchor=W)

		button_frame2 = Frame(record_window)
		Button(button_frame2, text='Stop', command=self.stop_record).pack(side=RIGHT)
		Button(button_frame2, text='Start', command=self.start_record).pack(side=RIGHT)
		button_frame2.pack(side=TOP, anchor=W, expand=1, fill=X)

		record_window.mainloop()

	def start_record(self):
		# TODO: CHECK IF ALREADY RECORDED - ASK FOR OVERWRITE
		self.status.config(text='Recording..')
		print 'RECORD HERE'

	def stop_record(self):
		# TODO: GET FILE PATH AND PASS IT TO UPLOADING FUNCTION
		self.status.config(text='Done')
		print 'STOP RECORDING HERE'
	# -----------------------------------------------------------


if __name__ == '__main__':
    window = GUI()
