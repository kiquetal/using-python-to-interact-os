#### Bash Scripting

	Basic Linux Commands
	Redirecting streams
	Pipes and Pipelines
	Singalling Processes


#### Redirection

	Process of sending a stream to a different destination.

	echo "as" > bla.txt

	2> for error

	0 input
	1 output


#### Pipes

	Piping: pipes you could connect multiple programs
	Pass data between programs.

	

#### Links

	Variables bash

	line="----"
	echo $line
	conditionals:

	if grep "127.0.0.1" /etc/hosts; then
		echo "ok"
	else
		"asda"
	fi

	if [ -n "$PATH" ]; then echo "your path is not empyu"; fi

	n=1
	while [$n -le 5]; do
	echo "iteration"
        ((n+1=1))
	done

	
