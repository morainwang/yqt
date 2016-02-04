#!/usr/bin/env python
#coding=utf-8

import subprocess

x = subprocess.check_output("ls")
print x