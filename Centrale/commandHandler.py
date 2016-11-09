
class CommandHandler ():

	def processCommand(self, portThread, command, data):
		page = self.main.guiThread.pages[portThread.id]
		
		self.main.guiThread.addText(page.text, command + " " + str(data))
	
		#print(portThread.port.port + " sent command: '" + command + "' with data: '" + str(data) + "'")
		
		if(command == "baseTemperature"):
			self.main.guiThread.setPageType(portThread, "temperature")
		
		elif(command == "baseRemand"):
			self.main.guiThread.setPageType(portThread, "remand")
		
	#
		
	def __init__(self, main):
		self.main = main;