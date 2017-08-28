import obd
import time
import numpy as np

class Current_Log:
 	'Current data object for logging the different parameters'
   	
 	#Gear Ratios for the KTM 390 Duke-Indian Version
 	gear ratio = np.zeroes(shape=(1,5))

 	def __init__(self):
    self.gear_number = 0										#Current gear the transmission is in
	  self.speed = 0											    #Vehicle speed
	  self.rpm =0 											    	#Engine RPM
	  self.tps = 0 												    #Throttle Position Sensor reading in %
	  self.cg_acceleration = 0								#Center of gravity Acceleration
	  self.oil_temperature = 0								#Engine Oil temperature	in celsius							
	  self.steering_wheel_angle = 0						#Steering wheel angle
	  self.gps = numpy.array[0,0,0]						#Current Global Positioning
	  self.fuel_level = 0										  #Fuel Level in %
	  self.engine_run_time = 0								#Total run time of engine in sec
	  self.time = datetime.datetime.now()			#Current Timestamp

	#Gear shifts
	def inc_gear_number():
		self.gear_number++
	def dec_gear_number():
		self.gear_number--

	##------------------------------------------------------------------------------------##
	#Setters
	#speed
	def set_speed(speed):
		self.speed=speed
   	#rpm
   	def set_rpm(rpm):
   		self.rpm=rpm
   	#tps
   	def set_tps(tps):
   		self.tps=tps
   	#cg_acceleration
   	def set_cg_acceleration(cg):
   		self.cg_acceleration=cg
  	#oil_temperature
  	def set_oil_temperature(temperature):
  		self.oil_temperature=temperature
  	#steering_wheel_angle
  	def set_steering_wheel_angle(angle):
  		self.steering_wheel_angle=angle
  	#fuel_level
  	def set_fuel_level(level):
  		self.fuel_level=level
  	#engine run time in seconds
  	def set_engine_run_time(seconds):
  		self.engine_run_time=seconds
  	##------------------------------------------------------------------------------------##
  	#Getters
  	#speed
	def get_speed():
		return self.speed
   	#rpm
   	def get_rpm():
   		return self.rpm
   	#tps
   	def get_tps(tps):
   		return self.tps
   	#cg_acceleration
   	def get_cg_acceleration():
   		return self.cg_acceleration
  	#oil_temperature
  	def get_oil_temperature()
  		return self.oil_temperature
  	#steering_wheel_angle
  	def get_steering_wheel_angle()
  		return self.steering_wheel_angle
	#fuel_level
  	def get_fuel_level()
  		return self.fuel_level
  	#engine run time	
  	def set_engine_run_time(seconds):
		return self.engine_run_time
  
##----------------------------------END OF CLASS-------------------------------------------##


#logging class object
log = Current_Log

#Async Connection with OBD-II module
connection = obd.Async()

##-----------------------------------------------------------------------------------------##
# Callback functions for different parameters for logging
# Engine RPM callback
def engine_rpm_cb(rpm):
     log.set_rpm(rpm)
     #firebase->send data to node
#Throttle Position
def throttle_cb(tps):
	log.set_tps(tps)
  #firebase->send data to node
#Engine Oil Temp
def oil_cb(temperature):
	log.set_oil_temperature(temperature)
  #firebase->send data to node
#Fuel Level
def fuel_level_cb(level):
	log.set_fuel_level(level)
  #firebase->send data to node
#Engine Run Time
def run_time_cb(runtime):
	log.set_engine_run_time(runtime)
  #firebase->send data to node

##-----------------------------------------------------------------------------------------##
#Continous checking for any parameter that changes
#Engine rpm 
connection.watch(obd.commands.RPM, callback=engine_rpm_cb)
#Throttle Position
connection.watch(obd.commands.THROTTLE_POS, callback= throttle_cb)
#Engine Oil Temp
connection.watch(obd.commands.OIL_TEMP, callback= oil_cb)
#Fuel Level
connection.watch(obd.commands.FUEL_LEVEL, callback = fuel_level_cb)
#Engine RUn Time
connection.watch(obd.commands.RUN_TIME, callback = run_time_cb)





connection.start()

#End OBD connection
connetcion.stop()