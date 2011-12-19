"""
This scripts implements changes required to meet the specifications descrideb by document ###need to include name of document###
"""
import os
import sys
import grp

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
	
	# Seting up auditd to comply with GEN002720 GEN002740 and GEN002760 specifications
	# Turning Auditd on
	chkconfig_exit_status = os.system('chkconfig auditd on')
	if chkconfig_ext_status == 0:
		print >> sys.stdout, "Audit service successfully setup to start at boot time."
	else:
		print >> sys.stderr, "There was a problem when seting up Audit service at boot time. Exit with error code: ", chkconfig_ext_status
		exit('error with chkconfig auditd on')
	# Seting up the audit.rules file
	'''
	###FIX ME###
	Using relative path names is bad. 
	If this script is called form outside the folder were the remaining files are located this will not work.
	Idealy we need a way to figure out the location of the script and the remaining files and then move to tha directory.
	'''
	try:
		os.rename('./etc/audit/audit.rules', '/etc/audit/audit.rules')
	except OSError as error:
		print >> sys.stderr, 'There was a problem seting up the Audit rules file:\n', str(error)
	
	# Seting up permitions of /etc/cron.deny to comply with GEN003200
	try:
		os.chmod('/etc/cron.deny', 0700)
		print >> sys.stdout, 'Premitions of /etc/cron.deny setup to 0700'
	except OSError as error:
		print >> sys.stderr, "There was a problem seting up premitions for /etc/cron.deny error:\n", str(error)
	
	# Seting up permitions of /etc/snmp/snmpd.conf to comply with GEN005320
	try:
		os.chmod('/etc/snmp/snmpd.conf', 0700)
	except OSError as error:
		print >> sys.stderr, "There was a problem seting up permitions for /etc/snmp/snmpd.conf:\n", str(error)
		
	# Seting up ownership of snmpd.conf and .mib to comply with GEN005360 root and sys
	# This is an alternative to hardcoding the group number. No need to do that for root as its always 0
	sys_gid = grp.getgrnam('sys')[2]
	root_uid = 0
	try:
		os.chown('/etc/snmp/snmpd.conf', root_uid, sys_gid)
	except OSError as error:
		print>> sys.stderr, "There was a problem seting up permitions for --------:\n", str(error)
	'''
	# for the mib files it might be better to first collect the resulf of a find comand. This would be required if the customer setup the lastes custom assertion mib
	'''
	
	# Seting up ownership and permitions of /etc/rsyslog.conf to comply with GEN005400.
	"Needs to be root and permition 600"
	try:
		os.chown('/etc/rsyslog.conf', 0, 0)
		os.chmod('/etc/rsyslog.conf', 0640)
	except OSError as error:
		print >> sys.stderr, "There was a problem setting up the ownership and/or permitions of /etc/rsyslog.conf:\n", str(error)
		
	# Seting up file permitions for /etc/security/access.conf to comply with LNX00440
	"Note that by default on a ssg 6.1 the permition of this file is 640"
	try:
		os.chown('/etc/security/access.conf', 0640)
	except OSError as error:
		print >> sys.stderr, "There was a problem setting up the permitions of /etc/security/access.conf:\n", str(error)
