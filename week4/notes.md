#### Managing Data and Processes

	Reading data interactively
	
	hours = int(input("Enter numbers of hours"))
	minutes = int(input("Enter numbers of minutes"))
	seconds = int(input("Enter numbers of seconds"))
	convert_to_seconds(hours,minutes,seconds)

#### Standrad Stremas

	IO manipulate input and output
	STDIN, STDOUT,STDERR
	
#### Environments variables

	Shell commnand-line interface to interact with the OS.

#### Path environment

	echo $MY_VAR

#### Commandline arguments

	import sys
	print(sys.argv)
#### Status codes

	import os
	import sys
	
	filename = sys.argv[1]
	if not os.path.exists(filename):
		with open(filename,"w") as f:
			f.write("new file")

	else:
		sys.exit(1)

#### Subprocesses 

	A script from python script.
	subprocess module

	import subprocess
	subprocess.run(["date"])



	my_env = os.environ.copy()
	my_env["PATH"] = os.pathsep.join(["/opt/myapp",my_env["PATH"]])
	
	result = subprocess.run(["myapp"],env=my_env)		

	logfile = sys.argv[1]
	with open(logfile) as f:
	  for line in f:
            if "CRON" not in line:
              continue
            println(line.strip())


