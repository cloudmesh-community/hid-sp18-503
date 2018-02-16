## Writing image on an sd card on Linux (ubuntu 16.04)

* in the file explorer, right clichk on the sd card and format the sd card
* run ```df -h``` to list all the drives in the computer
* insert the sd card and run the command again
* now a new entry will be listed which is the sd card
* The left column of the results from df -h command
gives the device name of your SD card.
It will be listed as something like /dev/mmcblk0p1 or /dev/sdX1,
where X is a lower case letter indicating the device.
The last part (p1 or 1 respectively) is the partition number.
* Note down the name of the sd card (without the partition)
* Unmount the card so that the card can not be read from or written to
* run ```unmount dev/mmcblk0p1``` (use correct name for the card)
* if your card has multiple partitions unmount all partitions
* next write the image to the sd card.
* run ```dd bs=4M if=<path to .img> of=/dev/mmcblk0 status=progress conv=fsunc```
* make sure ```if=``` contains the path to image and
```of=``` contains the name of the sd card otherwise you may ruin your hard disk

### Checking that the image was written properly

* create an image again from the sd card
* run ```dd bs=4M if=/dev/sdX of=from-sd-card.img```
* truncate the image to be the the same size as that of the raspbian image
```truncate --reference <original raspbian image> from-sd-card.img```
* run diff to see if the two files are same
* run ```diff -s from-sd-card.img <odiginal raspbian image>```
* diff should say that the two files are same