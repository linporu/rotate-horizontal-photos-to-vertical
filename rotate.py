import os
from PIL import Image


def main():
    # 使用絕對路徑獲取腳本所在目錄
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"腳本目錄: {script_dir}")
    
    # 設定輸入和輸出文件夾的路徑
    input_folder = os.path.join(script_dir, "input_images")
    output_folder = os.path.join(script_dir, "output_images")
    
    print(f"輸入文件夾路徑: {input_folder}")
    print(f"輸出文件夾路徑: {output_folder}")
    
    # 檢查輸入文件夾是否存在
    if not os.path.exists(input_folder):
        print(f"錯誤：輸入文件夾 '{input_folder}' 不存在。")
        return

    # 獲取輸入文件夾中的所有圖片文件
    image_files = get_image_files(input_folder)
    print(f"找到的圖片文件: {image_files}")
    
    # 遍歷每個圖片文件
    for image_file in image_files:
        # 構建完整的圖片路徑
        image_path = os.path.join(input_folder, image_file)
        # 打開圖片
        image = open_image(image_path)
        
        # 檢查圖片是否為橫向
        if is_horizontal(image):
            # 如果是橫向，旋轉圖片
            rotated_image = rotate_image(image)
            # 保存旋轉後的圖片
            save_image(rotated_image, output_folder, image_file)
        else:
            # 如果不是橫向，直接保存原圖
            save_image(image, output_folder, image_file)


def get_image_files(folder):
    print(f"正在搜索文件夾: {folder}")
    files = os.listdir(folder)
    print(f"文件夾中的所有文件: {files}")
    return [f for f in files if f.startswith("IMG_") and f.endswith(".jpg")]


def open_image(image_path):
    # 使用PIL庫打開圖片
    return Image.open(image_path)


def is_horizontal(image):
    # 獲取圖片的寬度和高度
    width, height = image.size
    # 如果寬度大於高度，則為橫向圖片
    return width > height


def rotate_image(image):
    # 將圖片逆時針旋轉270度（相當於順時針旋轉90度）
    # expand=True 確保旋轉後的圖片不會被裁剪
    return image.rotate(270, expand=True)


def save_image(image, output_folder, filename):
    # 如果輸出文件夾不存在，則創建它
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # 構建輸出圖片的完整路徑
    output_path = os.path.join(output_folder, filename)
    # 保存圖片
    image.save(output_path)


if __name__ == "__main__":
    main()
