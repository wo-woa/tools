# -*- coding: utf-8 -*-

import json
import sys
import os
import cv2
import re

from bs4 import BeautifulSoup
import time
import json
import requests
from lxml import etree
import string
import random
from collections import Counter
from functools import reduce
import os
import threading
import multiprocessing
import numpy as np
import re
from lxml import etree
from ctypes import *
from PIL import Image
from concurrent import futures
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import webbrowser
import multiprocessing as mp

s='window["nonc"+"e"] = "1d6a2becfa87e642b6679f40a23e9d87";'
pattern='window\["nonc"\+"e"\] = "(.+?)"'
d=re.search(pattern,s)
print(d.group(1))