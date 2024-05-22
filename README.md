Remember to chmod +x the files.
"allocate.sh" unhooks and blocks the configured cores from host
"free.sh" frees every core on the system

If you run cpus with a different topology, you can run the generate.py file, that will ask you questions about your cpu, 
and will generate the perfect scripts for your cpu! THIS IS HEAVILY WIP!!! (Doesnt work properly yet pwq) i hate python

The premade scripts are made for Xeon e5 v4 2687W Cpus. (You can customize the allocate/free script with lstopology)

--If you clone these 3 files to the same directory, you can simply run the start script, and it will dynamically unhook cores,
  start your vm with looking glass, and when shutting down the vm reallocate your cores.
  So it basically does everything for you :P
