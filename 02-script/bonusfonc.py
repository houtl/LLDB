import lldb

def colorR(debugger, command, result, dct):
	debugger.HandleCommand('script print "\033[31m"')

def colorG(debugger, command, result, dct):
	debugger.HandleCommand('script print "\033[32m"')

def colorB(debugger, command, result, dct):
	debugger.HandleCommand('script print "\033[34m"')

def colorW(debugger, command, result, dct):
	debugger.HandleCommand('script print "\033[39m"')

def colorT(debugger, command, result, dct):
	debugger.HandleCommand('script print "\033[36m"')

def __lldb_init_module(debugger, internal_dict):
	debugger.HandleCommand("command script add -f bonusfonc.colorR colorR")
	debugger.HandleCommand("command script add -f bonusfonc.colorG colorG")
	debugger.HandleCommand("command script add -f bonusfonc.colorB colorB")
	debugger.HandleCommand("command script add -f bonusfonc.colorW colorW")
	debugger.HandleCommand("command script add -f bonusfonc.colorT colorT")
