import re
# import upload_youtube
import os

# if no upload, simply don't include $$.*$$ in the commit message
# if upload, include the following strings in the commit message:
# $$method=mm, location=ll, title=tt (optional), description=dd (optional)$$
# method
    # record: record from local camera
    # local: choose existing file from file picker
# location
    # commit: include video url in the commit message
    # x: insert video url as a comment in line x
# title: title of the video shown on Youtube
# description (optional): description of the video on Youtube
#
# e.g. This is a commit message $$method=record, location=58, title=Explain funcA$$


def has_upload_task(message):
    if re.search(r'\$\$.*\$\$', message):
        return True
    return False

def parse_message(message):
    if has_upload_task(message):
        method = re.search(r'\$\$method=(.*?),', message).group(1)
        location = re.search(r'location=(.*?),', message).group(1)
        title = re.search(r'title=([^\$]*)[,\$]', message).group(1)
        description = ''
        if re.search('description=',message):
            description = re.search('description=(.*?),', message).group(1)

    # more codes to be added to use method etc.

    if method == 'record':
        try:
            os.system('./ffmpeg.sh v')
        except KeyboardInterrupt:
            print '\n\n\n\n\n\n\n\n\n\n\n\n\n HELLO'
            pass
        print 'Hello OKAY'
    elif method == 'local':
        os.system('')
