Remember to chmod +x the files.
allocate unhooks and blocks the configured cores from host
free frees every core on the system

if you tun cpus with a different topology, you need to customize the scripts. 
you can use this as a preset.

These scripts are made for Xeon e5 v4 2687W Cpus. (You can customize the allocate/free script with lstopology)

--If you clone these 3 files to the same directory, you can simply run the start script, and it will dynamically unhook cores,
  start your vm with looking glass, and when shutting down the vm reallocate your cores.
  So it basically does everything for you :P
