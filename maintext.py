import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def visualize_image_histogram(image_path):
 """加载一张图片，计算其颜色直方图，并以可视化的方式呈现."""

 try:
   # 使用 Pillow 加载图片
   img = Image.open(image_path)

   # 必要时转换为 RGB 格式
   if img.mode != "RGB":
     img = img.convert("RGB")

   # 创建像素值的 NumPy 数组
   pixels = np.array(img)

   # 计算每个颜色通道（红、绿、蓝）的颜色直方图
   color_hist = [plt.hist(pixels[:, :, i].flatten(), bins=256, range=(0, 256))[0] for i in range(3)]

   # 为每个颜色通道创建一个子图
   fig, axes = plt.subplots(nrows=3, figsize=(8, 6))
   colors = ["red", "green", "blue"]
   for i, ax in enumerate(axes):
     ax.plot(color_hist[i], color=colors[i])
     ax.set_title(f"{colors[i].title()} 通道直方图")
     ax.set_xlabel("像素强度")
     ax.set_ylabel("频率")

   plt.tight_layout()
   plt.show()

 except FileNotFoundError:
   print("图片文件未找到。")

# 示例用法：
image_path = "path/to/your/image.jpg"  # 替换为实际的图片路径
visualize_image_histogram(image_path)
