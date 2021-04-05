#!/usr/bin/env python3

import pandas as pd
import seaborn as sns

traffic = pd.read_excel('data/tra8901.ods', engine="odf", skiprows=3)

print(traffic.head())

