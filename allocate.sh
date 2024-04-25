systemctl set-property --runtime -- user.slice AllowedCPUs=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30
systemctl set-property --runtime -- system.slice AllowedCPUs=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30
systemctl set-property --runtime -- init.scope AllowedCPUs=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30

