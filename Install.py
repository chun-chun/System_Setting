#!/usr/bin/env python

import os
import platform


## setting
vimrcFile = ".vimrc"
MacAddPath = None
WinAddPath ="C:\\Users\\USER\\Desktop\\tool\\Sublime Text Build 3114 x64;"


LocalPath = os.getcwd()
System 	= platform.system()

# print(System)
# print(LocalPath+"\\"+ vimrcFile)

# os.popen("ln -s ~/.vimrc ~/.vim/vimrc")

# print(os.popen("ls").read())


def setting_vimrc(sys = None):
	if (sys == "Windows" ):
		basicPath = os.popen("echo %Path%").read().strip()
		path = basicPath+WinAddPath
		os.popen("setx Path \""+path+"\" /M")
		print(path)
		pass
	elif (sys == "Mac" ):

		# ln -s "/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl" /usr/local/bin/sublime
		pass
	else:
		pass

def setting_path(sys = None):
	if (sys == "Windows" ):

		pass
	elif (sys == "Mac" ):

		# ln -s "/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl" /usr/local/bin/sublime
		pass
	else:
		pass


def main():
	# setting_path(System)
	setting_vimrc(System)




if __name__ == '__main__':
	main()




