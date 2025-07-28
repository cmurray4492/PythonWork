from cuda_available import cuda_available

cnt = cuda_available.getCudaDeviceCount()
for idx in range(cnt):
    info = cuda_available.CudaDeviceInfo(idx)
    print(f"ID: {info.id}")
    print(f"Name: {info.name}")
    print(f"ComputeCapability: {info.computeCapability}")
    print(f"TotalGlobalVmem: {info.totalGlobalVmem}")
    print(f"PciId: {info.pciId}")
    print(f"UsingTccDriver: {info.isTccDriver}")
    print("===================================")
