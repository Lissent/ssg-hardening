#!/usr/bin/python
# encoding: utf-8
#
#Copyright 2011 Frédéric Masi
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
"""
This scripts implements changes required to meet the specifications descrideb by document ###need to include name of document###
"""

import os
import sys
import grp


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


def gen003080():
	'''
	Seting up permitions to comply with GEN003080 specifications
	# Attention if you don't set the x bit on folders and you need to run this script a second time
	# You will need to run it as root
	'''
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


def gen000580():
	'''
	This function sets up pam.d and falgs all passwords as expired so that the system will comply with: "GEN000580 PASSWORD LENGTH"
	###FIX ME###
	# need to force all users to change password
	'''
	try:
		os.rename('./etc/pam.d/system-auth', '/etc/pam.d/system-auth')
		os.rename('./etc/pam.d/system-auth-ac', '/etc/pam.d/system-auth-ac')
	except OSError as error:
		print >> sys.stderr, "There was a problemm setuing up the password configuration files:\n", str(error)


def gen002720_gen002740_gen002760():
	'''
	This fuction configurs auditd to comply with GEN002720 GEN002740 and GEN002760 specifications
	'''
	# TURNING AUDITD ON
	chkconfig_exit_status = os.system('chkconfig auditd on')
	if chkconfig_ext_status == 0:
		print >> sys.stdout, "Audit service successfully setup to start at boot time."
	else:
		print >> sys.stderr, "There was a problem when seting up Audit service at boot time. Exit with error code: ", chkconfig_ext_status
		exit('error with chkconfig auditd on')
	# SETING UP THE AUDIT.RULES FILE
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


def gen003200():
	'''
	Seting up permitions of /etc/cron.deny to comply with GEN003200
	'''
	try:
		os.chmod('/etc/cron.deny', 0700)
		print >> sys.stdout, 'Premitions of /etc/cron.deny setup to 0700'
	except OSError as error:
		print >> sys.stderr, "There was a problem seting up premitions for /etc/cron.deny error:\n", str(error)


def gen005320_gen005360():
	'''
	Seting up permitions of /etc/snmp/snmpd.conf to comply with GEN005320.
	Seting up ownership of snmpd.conf and .mib to comply with GEN005360 root and sys
	'''
	try:
		os.chmod('/etc/snmp/snmpd.conf', 0700)
	except OSError as error:
		print >> sys.stderr, "There was a problem seting up permitions for /etc/snmp/snmpd.conf:\n", str(error)
		
	# This is an alternative to hardcoding the group number. No need to do that for root as its always 0
	sys_gid = grp.getgrnam('sys')[2]
	root_uid = 0
	try:
		os.chown('/etc/snmp/snmpd.conf', root_uid, sys_gid)
	except OSError as error:
		print>> sys.stderr, "There was a problem seting up permitions for --------:\n", str(error)
	'''
	###FIX-ME###
	# For the mib files it might be better to first collect the resulf of a find comand. This would be required if the customer setup the lastes custom assertion mib
	'''


def gen005400():
	'''
	Seting up ownership and permitions of /etc/rsyslog.conf to comply with GEN005400.
	###FIX ME###
	Need to be sure we only use rsyslog
	'''
	try:
		os.chown('/etc/rsyslog.conf', 0, 0)
		os.chmod('/etc/rsyslog.conf', 0640)
	except OSError as error:
		print >> sys.stderr, "There was a problem setting up the ownership and/or permitions of /etc/rsyslog.conf:\n", str(error)

def lnx00440():
	# Seting up file permitions for /etc/security/access.conf to comply with LNX00440
	"Note that by default on a ssg 6.1 the permition of this file is 640"
	try:
		os.chown('/etc/security/access.conf', 0640)
	except OSError as error:
		print >> sys.stderr, "There was a problem setting up the permitions of /etc/security/access.conf:\n", str(error)


def main():
	pass


if __name__ == '__main__':
	main()

