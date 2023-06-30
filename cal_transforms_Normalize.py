import torch
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder

# 設置圖像讀取和轉換
transform = transforms.Compose([
    transforms.ToTensor()
])

# 載入自己的圖像數據集
dataset = ImageFolder(root=r'MobileNetV3\media\data2\chenjiarong\ImageData\BYO Tableware', transform=transform)

# 計算平均值和標準差
data_loader = torch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False)
mean = 0.
std = 0.
total_samples = 0

for inputs, _ in data_loader:
    batch_samples = inputs.size(0)
    inputs = inputs.view(batch_samples, inputs.size(1), -1)
    mean += inputs.mean(2).sum(0)
    std += inputs.std(2).sum(0)
    total_samples += batch_samples

mean /= total_samples
std /= total_samples

print('Mean:', mean)
print('Std:', std)
