#!/root/.pyenv/versions/backp/bin/python
#Filename:backup.sh

import os,time

source = '/root/python'

target_dir = '/tmp/backup/'

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
comment = input('Enter a comment -->')
if len(comment) == 0:
    target = today + os.sep + os.path.basename(source) + now + '.zip'
else:
    target = today + os.sep + os.path.basename(source) + now + '_' + comment.replace(' ','_') + '.zip'
if not os.path.exists(today):
    os.mkdir(today)
    print('Successed created directory',today)
zip_command = "zip -qr %s %s" % (target,''.join(source))

if os.system(zip_command) == 0:
    print('Successful backup to ',target)
else:
    print('Backup FAILED')


