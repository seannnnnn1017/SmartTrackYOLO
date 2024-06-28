import torch

# 檢查CUDA是否可用
cuda_available = torch.cuda.is_available()
print(f"CUDA 可用: {cuda_available}")

if cuda_available:
    # 獲取CUDA設備的數量
    num_cuda_devices = torch.cuda.device_count()
    print(f"CUDA 設備數量: {num_cuda_devices}")
    
    # 獲取每個CUDA設備的信息
    for i in range(num_cuda_devices):
        print(f"設備 {i}: {torch.cuda.get_device_name(i)}")
        print(f"  - 記憶體總量: {torch.cuda.get_device_properties(i).total_memory / 1e9:.2f} GB")
        print(f"  - CUDA計算能力: {torch.cuda.get_device_properties(i).major}.{torch.cuda.get_device_properties(i).minor}")
        print(f"  - 浮點計算性能: {torch.cuda.get_device_properties(i).multi_processor_count} 個多處理器")
else:
    print("沒有可用的CUDA設備")
