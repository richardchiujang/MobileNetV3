import os
import random
import shutil

# data_folder = "MobileNetV3\media\data2\chenjiarong\ImageData\BYO Tableware\Yes"
# train_folder = "MobileNetV3\media\data2\chenjiarong\ImageData\BYO Tableware train\Yes"
# val_folder = "MobileNetV3\media\data2\chenjiarong\ImageData\BYO Tableware val\Yes"
# train_ratio = 0.7  # 訓練集比例

# # 確保目標資料夾存在
# os.makedirs(train_folder, exist_ok=True)
# os.makedirs(val_folder, exist_ok=True)

# # 讀取資料夾中的圖片檔案列表
# print(os.getcwd())
# image_files = os.listdir(data_folder)
# print("圖片總數:", len(image_files))
# print("圖片檔案列表:", image_files[:10])
      

# # 隨機洗牌圖片檔案列表
# random.shuffle(image_files)

# # 計算訓練集和驗證集的分界索引
# train_split = int(train_ratio * len(image_files))

# # 將圖片檔案分配到訓練集和驗證集資料夾
# for i, file_name in enumerate(image_files):
#     source_path = os.path.join(data_folder, file_name)
#     if i < train_split:
#         target_path = os.path.join(train_folder, file_name)
#     else:
#         target_path = os.path.join(val_folder, file_name)
#     shutil.copyfile(source_path, target_path)

# print("拆分完成！")
# print("訓練集大小:", len(os.listdir(train_folder)))
# print("驗證集大小:", len(os.listdir(val_folder)))


data_folder = "MobileNetV3\media\data2\chenjiarong\ImageData\BYO Tableware\\No"
train_folder = "MobileNetV3\media\data2\chenjiarong\ImageData\BYO Tableware train\\No"
val_folder = "MobileNetV3\media\data2\chenjiarong\ImageData\BYO Tableware val\\No"
train_ratio = 0.7  # 訓練集比例

# 確保目標資料夾存在
os.makedirs(train_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)

# 讀取資料夾中的圖片檔案列表
print(os.getcwd())
image_files = os.listdir(data_folder)
print("圖片總數:", len(image_files))
print("圖片檔案列表:", image_files[:10])
      

# 隨機洗牌圖片檔案列表
random.shuffle(image_files)

# 計算訓練集和驗證集的分界索引
train_split = int(train_ratio * len(image_files))

# 將圖片檔案分配到訓練集和驗證集資料夾
for i, file_name in enumerate(image_files):
    source_path = os.path.join(data_folder, file_name)
    if i < train_split:
        target_path = os.path.join(train_folder, file_name)
    else:
        target_path = os.path.join(val_folder, file_name)
    shutil.copyfile(source_path, target_path)

print("拆分完成！")
print("訓練集大小:", len(os.listdir(train_folder)))
print("驗證集大小:", len(os.listdir(val_folder)))
