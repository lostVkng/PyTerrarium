"""
	Py Terrarium
    - Control LEDs w/ Python
    - Uses cron jobs
"""
from datetime import datetime
from subprocess import call
from crontab import CronTab


"""
	Config
"""
led_py_path="/home/pi/dev/PyTerrarium/src/leds.py"
led_on_hr = 18
led_off_hr = 0


"""
	Setup Cron Jobs
"""
if __name__ == "__main__":

	# turn on/off leds if past time time
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
    
	if now.hour >= led_on_hr:
		call(['python', 'leds.py', '-on'])
	else:
		call(['python', 'leds.py'])
	
	# Setup cron
	# access crontab
	cron = CronTab(user="root")

	# remove all cron jobs
	cron.remove_all()

	# add PyTerrarium to call on reboot
	job = cron.new(command="python3 " + "/home/pi/dev/PyTerrarium/src/app.py", comment="PyTerrarium - main")
	job.setall('@reboot') # set all time slices
	cron.write()

	# set led on
	job = cron.new(command="python3 " + led_py_path + " -on", comment="PyTerrarium - LEDs On")
	job.setall('0 ' + str(led_on_hr) + ' * * *') # set all time slices
	cron.write()

	# set led off
	job = cron.new(command="python3 " + led_py_path, comment="PyTerrarium - LEDs Off")
	job.setall('0 ' + str(led_off_hr) + ' * * *') # set all time slices
	cron.write()

	print("PyTerrarium is setup")