# CAMERA
It is a project for making a camera with a PCB on KiCAD 9.0 and a box of metal designed on QCAD 3.32.

Thank to you for using it with the driver on Windows X11 or Linux Ubuntu 24.04 to see the images with the NI data acquisition board PCIe6509.

For linux you need to install Comedi and try to launch the driver :

sudo apt-get update

sudo apt-get install libcomedi-dev

sudo mknod -m 666 /dev/comedi0 c 98 0

sudo modprobe comedi comedi_num_legacy_minors=4

sudo modprobe ni_65xx

sudo comedi_config /dev/comedi0 ni_65xx
