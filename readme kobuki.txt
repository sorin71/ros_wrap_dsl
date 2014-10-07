
Follow the instructions to install ROS and Kobuki simulator demo.

The unmodified launch file is installed at:
	
	/opt/ros/indigo/share/kobuki_softapps/launch/nav_demo.launch

How to run the internal DSL demo:

1) Launch the robot (without base_move node):

   Change directory to where the modified launch file is:

	cd /home/sorin/FRSC2014_etc/Kobuki
   
   and launch the simulator:
   
        roslaunch nav_demo.launch

2) Start the wrapping node in another terminal command line (wrapping/running the base_move node):
   
   Init the environment:
	
	sdu

   Start the Python commnad line interface:
	
	python

   Type the wrapping node or execute the file containing all the commands supposed to by typed on the python's command line interface:

	execfile('/home/sorin/roswork_FRSC2014/src/EnhanceRosNode/Kobuki_test.py')










