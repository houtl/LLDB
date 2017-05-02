import lldb

def reverse(debugger, command, result, internal_dict):
	name = debugger.GetSelectedTarget()
	print 'FT_'+''.join(reversed(str(name)))

def __lldb_init_module(debugger, dict):
	debugger.HandleCommand('command script add -f reverse.reverse reverse')  