import lldb
import time

def auto(debugger, command, result, internal_dict):
	args = command.split(" ")
	if not len(args) == 3:
		print "Usage: auto [nb] [nb] [nb]"
		exit()

	debugger.SetAsync(True)
	debugger.HandleCommand("breakpoint set --line 16")
	time.sleep(0.5)
	debugger.HandleCommand("breakpoint set --line 19 -o")
	time.sleep(0.5)
	debugger.HandleCommand("breakpoint set --line 32 -c 'tmp=min[0]+min[1]+min[2]'")
	time.sleep(0.5)
	debugger.HandleCommand("breakpoint set --line 44 -c 'biggest=(min[0]>min[1]?min[0]:min[1])>min[2]?(min[0]>min[1]?min[0]:min[1]):min[2]'")
	time.sleep(0.5)
	debugger.HandleCommand("process launch")
	time.sleep(0.5)
	debugger.HandleCommand("exp $rsi -= 4")
	time.sleep(0.5)
	debugger.HandleCommand("process continue")
	debugger.GetSelectedTarget().GetProcess().PutSTDIN(args[0]+'\n')
	time.sleep(0.5)
	debugger.HandleCommand("process continue")
	debugger.GetSelectedTarget().GetProcess().PutSTDIN(args[1]+'\n')
	time.sleep(0.5)
	debugger.HandleCommand("exp $rsi += 4")
	time.sleep(0.5)
	debugger.HandleCommand("process continue")
	debugger.GetSelectedTarget().GetProcess().PutSTDIN(args[2]+'\n')
	time.sleep(0.5)
	debugger.HandleCommand("exp count=0")
	time.sleep(0.5)
	debugger.HandleCommand("process continue")
	time.sleep(0.5)
	debugger.HandleCommand("process continue")
	time.sleep(0.5)
	debugger.HandleCommand("process continue")
	time.sleep(0.5)

def __lldb_init_module(debugger, internal_dict):
	debugger.HandleCommand('command script add -f auto.auto auto')
