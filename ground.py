import cv2
import numpy as np
# 加载原始照片
img = cv2.imread('dog.jpg')

# 创建一个掩膜，将背景设为红色
mask = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mask[mask > 0] = cv2.GC_PR_FGD  # 将掩膜值设为 GC_PR_FGD

# 从照片中提取前景和背景
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
mask, bgdModel, fgdModel = cv2.grabCut(img, mask, None, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_MASK)

# 将掩膜应用于照片，将背景替换为红色
img[mask == cv2.GC_BGD] = [0, 0, 255]

# 保存处理后的照片
cv2.imwrite('output.jpg', img)