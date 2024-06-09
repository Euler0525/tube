from PIL import Image

# 加载图片
image_path = '1.png'
image = Image.open(image_path)

# 将图片转换为RGB模式
image = image.convert('RGB')

# 获取图片数据
pixels = image.load()

# 定义要查找和替换的颜色
color_to_find = (241, 243, 242)  # #F6F6F6
color_to_replace = (255, 255, 255)  # #FFFFFF

# 遍历图片中的每个像素
for y in range(image.size[1]):
    for x in range(image.size[0]):
        # 如果像素颜色匹配要查找的颜色
        if pixels[x, y] == color_to_find:
            # 替换颜色
            pixels[x, y] = color_to_replace

# 保存修改后的图片
image.save('11.png')

print('颜色替换完成，已保存修改后的图片。')
