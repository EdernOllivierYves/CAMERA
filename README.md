# CAMERA
It is a perfect project for making a camera with a PCB on KiCAD 9.0.4 and a box of metal designed on QCAD 3.32.

Thank to you for using it with the driver on Windows X11 or Linux Ubuntu 24.04 LTS to see the images with the NI data acquisition board PCIe6509.

For linux you need to install Comedi and try to launch the driver :

sudo apt-get update

sudo apt-get install libcomedi-dev

sudo mknod -m 666 /dev/comedi0 c 98 0

sudo modprobe comedi comedi_num_legacy_minors=4

sudo modprobe ni_65xx

sudo comedi_config /dev/comedi0 ni_65xx

About the circuit, I want to say that the wires should be longer and better routed, with respect to the FPGA and the sensor.

Maybe an amplifier of the output signals can be added, and also an operationnal amplifier for the following voltages of the controls of the sensor can be done.

After you plug the supply, the blue LED will blink, then you must download the VHDL file of .SOF into the mother board with the QUARTUS 17.0.0.595 software.

Then you can see the signals with the scope on the Arduino connector and plug the mother board to the daugther board made of the image sensor with MT9M413.

At last the image sensor will heat a lot and you will plug the NI board on the daugther board to see the images.

PS :  Sorry but in this PCB design there is one wire which seem that has not been routed at this time, it seems to be the PG_N.

You should route the PG_N signal wire under KiCad 9.0.4 in order to make the camera to work fine.

NB :  On the PCB it seems to be wired, and also I have checked the connectivity of the wire PG_N from the Arduino connector to the image sensor with a voltmeter.

Moreover I have applied the supply on the FPGA board, with the Cyclone 10 LP Altera FPGA, and have seen the PG_N signal in yellow on my scope VOLTCRAFT DSO-2154.

BR, EO.
