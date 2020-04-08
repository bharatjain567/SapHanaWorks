#!/bin/bash
cat configfile1.xml | /hana/HANA_EXPRESS_20/DATA_UNITS/HDB_LCM_LINUX_X86_64/hdblcm --read_password_from_stdin=xml --configfile=configfile1 -b
