# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 20:30:28 2024

@author: South
"""

from cuda_available import cuda_available

cnt = cuda_available.getCudaDeviceCount()
print(f"Cuda device count: {cnt}")
