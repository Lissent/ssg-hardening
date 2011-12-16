"""
This scripts implements changes required to meet the specifications descrideb by document ###need to include name of document###
"""
import os
import sys

# Creating function that makes it easy to do a recunsive chmod
def recursive_chmod(dir_name, permition):
"""
Recursive chmod.
This function takes two arguments the first one is the name of the folder and the second is the permition you like to recursively set.
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
	# Attention if you don't set the x bit on folders and you need to run this script a second time
	# You will need to run it as root
	try:
		recursive_chmod('/var/spool/cron', 0600)
		recursive_chmod('/etc/cron.d', 0600)
		os.chmod('/etc/crontab', 0600)
		recursive_chmod('/etc/cron.daily', 0700)
		recursive_chmod('/etc/cron.hourly', 0700)
		recursive_chmod('/etc/cron.monthly', 0700)
		recursive_chmod('/etc/cron.weekly', 0700)
	except OSError as error:
		print >> sys.stderr, 'You got an OS error:\n', str(error)
	
	# Seting up auditd to comply with GEN002720 specifications
	chkconfig_exit_status = os.system('chkconfig auditd on')
	if chkconfig_ext_status == 0:
		print >> sys.stdout, "Audit service successfully setup to start at boot time."
	else:
		print >> sys.stderr, "There was a problem when seting up Audit service at boot time. Exit with error code: ", chkconfig_ext_status
		exit('error with chkconfig auditd on')
	
