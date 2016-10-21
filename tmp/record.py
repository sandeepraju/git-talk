import subprocess as sp
import sys
import upload_youtube


arg = sys.argv[1]
p = None

try:
	# audio and video command
	av_cmd = ['ffmpeg',
		'-f', 'avfoundation',
		'c:v', 'rawvideo',
		'-framerate', '30',
		'-i', '"0:0"',
		'-y', '-f', 'mp4', 		
		'-c:v', 'libx264', 
		'-c:a', 'aac', 
		'out.mp4']

	# audio and screen grab command
	as_cmd = ['ffmpeg',
		'-f', 'avfoundation',
		'c:v', 'rawvideo',
		'-framerate', '30',
		'-i', '"1:0"',
		'-y', 
		'-f', 'mp4', 
		'-c:v', 'libx264', 
		'-c:a', 'aac', 
		'out.mp4']

	# audio command
	a_cmd = ['ffmpeg',
		'-f', 'avfoundation',
		'-i', '"none:0"',
		'-vn',
		'c:a', 'aac',
		'-y', '-vn', 
		'-f', 'mp4', 
		'-c:a', 'aac',
		'out.mp4']

	# parse argument for media type selection
	if arg is 'v':
		print 'Recording video'
		cmd = av_cmd
	elif arg is 'a':
		print 'Recording audio'
		cmd = a_cmd		
	elif arg is 's':
		print 'Recording audio and screen'
		cmd = as_cmd
	else:
		print 'Argument not valid'
		raise Exception

	# Open Ffmpeg subprocess and direct output to stdout
	p = sp.Popen(cmd, stdout=sys.stdout)

	while True:
		pass
		# might be unnecessary - just to make sure script doesn't exist while ffmpeg is running

except KeyboardInterrupt:
	pass

except:
	raise

finally:
	# find output file and give it to Youtube API to upload
	upload_youtube('output/out.mp4', 'Test media title', 'Test media description')