"""
This scripts implements changes required to meet the specifications descrideb by document ###need to include name of document###
"""
import os
import sys

# Creating function that makes it easy to do a recunsive chmod
def recursive_chmod(dir_name, permition):
"""
Recursive chmod.
###FIX-ME### I ONLY WORK WITH FOLDERS. I DONT WORK IF YOU PASS ME A FILENAME
"""
	for root, dirs, files in os.walk(dir_name):
		print >> sys.stdout, 'Changing permitions for forder:\t\t', root
		os.chmod(root, permition)
		for file in files:
			print >> sys.stdout, 'Changing permitions for file:\t\t', os.path.join(root, file)
			os.chmod(os.path.join(root, file), permition)

if __name__='__main__':
	# Seting up permitions to comply with GEN003080 specifications
	recursive_chmod('/var/spool/cron', 0600)
	recursive_chmod('/etc/cron.d', 0600)
	os.chmod('/etc/crontab', 0600)
	recursive_chmod('/etc/cron.daily', 0700)
	recursive_chmod('/etc/cron.hourly', 0700)
	recursive_chmod('/etc/cron.monthly', 0700)
	recursive_chmod('/etc/cron.weekly', 0700)
