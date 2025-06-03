Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import nidaqmx
>>> from nidaqmx.constants import LineGrouping
>>> with nidaqmx.Task() as task:
...     task.di_channels.add_di_chan("Dev1/port0", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)
... 
...     data = task.read()
...     print(f"Acquired data: {data:#x}")
... 
...     
DIChannel(name=Dev1/port0)
Acquired data: 0x0
