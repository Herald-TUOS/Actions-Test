import pandas as pd
import numpy as np

from pvlive_api import PVLive

pvl = PVLive()

print(len(pvl.pes_ids))

print(len(pvl.gsp_ids))