import os
import urllib2
import sys

# Place this in the root folder
paths = ['lsfx/', 'sfx/', 'music/']
site_url = 'http://zmi-cdnstatic.s3.amazonaws.com/wolfenstein.bethsoft.com'

for path in paths:
    if not os.path.exists(path):
        current_path = path[:-1]
        print "Couldn't find the %s folder. Check you are running this from the root folder or the %s folder is not missing." % (current_path, current_path)
    else:
        for infile in os.listdir(path):
                if os.path.splitext(infile)[1] == '.ogg':
                    mp3_file_name = path + infile[:-4] + '.mp3'
                    remote = urllib2.urlopen('%s/%s' % (site_url, mp3_file_name))
                    try:
                        print 'Downloading %s' % mp3_file_name
                        open(mp3_file_name, 'wb').write(remote.read())
                    except urllib2.URLError, e:
                        raise "An error occured while downloading: %r" % e
