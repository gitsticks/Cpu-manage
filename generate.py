import os
print("How many total physical cores are on your system? (Task Manager / 2)")
physcores = input("Phsical Cores:")
physcoresint = int(physcores)
if physcoresint < 3:
  print("Running on Dual / Single core is not supported! ")
print("Does Core 0,1 or 2 Have L1 Cache access? (check lstopo)")
cachecore = input("First Core with L1:")
cachecoreint = int(cachecore)
print("Please select one of the following performance modes:")
print("1 - Low Performance")
print("2 - Balanced Performance")
print("3 - High Performance")
selection = int(input("Mode:"))
if selection == 1:
  print("erm")
if selection == 3:
  outputFile = open("output.txt" , "w")
  outputFile.write("systemctl set-property --runtime -- user.slice AllowedCPUs=")
  for x in range(physcoresint-2):
    outputFile.write(str(x))
    if x < physcoresint-3:
      outputFile.write(",")
  outputFile.write("\n")

  outputFile.write("systemctl set-property --runtime -- system.slice AllowedCPUs=")
  for x in range(physcoresint-2):
    outputFile.write(str(x))
    if x < physcoresint-3:
      outputFile.write(",")
  outputFile.write("\n")

  outputFile.write("systemctl set-property --runtime -- init.scope AllowedCPUs=")
  for x in range(physcoresint-2):
    outputFile.write(str(x))
    if x < physcoresint-3:
      outputFile.write(",")
  outputFile.write("\n")


outputFile.close()
