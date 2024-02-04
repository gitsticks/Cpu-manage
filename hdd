//This QEMU snippet passes a HDD disk device through to KVM
------------------------------------------------------
<disk type="block" device="disk">
  <driver name="qemu" type="raw" cache="none"/>
  <source dev="/dev/sdd1"/>
  <target dev="vdc" bus="virtio"/>
  <address type="pci" domain="0x0000" bus="0x01" slot="0x00" function="0x0"/>
</disk>
------------------------------------------------------
