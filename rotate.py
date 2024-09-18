import os
from PIL import Image


def main():
    """
    主函式，負責協調整個圖片處理過程。
    包括獲取文件夾路徑、讀取圖片文件、處理圖片旋轉，以及保存處理後的圖片。
    """
    # 建立路徑
    input_folder, output_folder = get_folders()
    
    # 獲取輸入文件夾中的所有圖片文件
    image_files = get_image_files(input_folder)
    
    # 遍歷每個圖片文件
    for image_file in image_files:
        # 構建完整的圖片路徑
        image_path = os.path.join(input_folder, image_file)
        # 打開圖片
        with Image.open(image_path) as image:
            # 檢查圖片是否為橫向
            if is_horizontal(image):
                # 如果是橫向，旋轉圖片
                # 將圖片逆時針旋轉270度（相當於順時針旋轉90度）
                # expand=True 確保旋轉後的圖片不會被裁剪
                rotated_image = image.rotate(270, expand=True)
                # 保存旋轉後的圖片
                save_image(rotated_image, output_folder, image_file)
            else:
                # 如果不是橫向，直接保存原圖
                save_image(image, output_folder, image_file)


def get_folders():
    """
    獲取輸入和輸出文件夾的路徑。
    檢查輸入文件夾是否存在，如果輸出文件夾不存在則創建它。
    返回輸入和輸出文件夾的路徑。
    """
    # 使用絕對路徑獲取腳本所在目錄
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 設定輸入和輸出文件夾的路徑
    input_folder = os.path.join(script_dir, "input_images")
    output_folder = os.path.join(script_dir, "output_images")

    # 檢查輸入文件夾是否存在
    if not os.path.exists(input_folder):
        print(f"錯誤：輸入文件夾 '{input_folder}' 不存在。")
        return
    
    # 如果輸出文件夾不存在，則創建它
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    print(f"輸入文件夾路徑: {input_folder}")
    print(f"輸出文件夾路徑: {output_folder}")
    
    return input_folder, output_folder


def get_image_files(folder):
    """
    獲取指定文件夾中所有以"IMG_"開頭且以".jpg"結尾的圖片文件。
    返回符合條件的文件名列表。
    """
    files = os.listdir(folder)
    return [f for f in files if f.startswith("IMG_") and f.endswith(".jpg")]


def is_horizontal(image):
    """
    檢查給定的圖片是否為橫向。
    如果圖片的寬度大於高度，則返回True，否則返回False。
    """
    # 獲取圖片的寬度和高度
    width, height = image.size
    # 如果寬度大於高度，則為橫向圖片
    return width > height


def save_image(image, output_folder, filename):
    """
    將給定的圖片保存到指定的輸出文件夾中。
    使用原始文件名作為保存的文件名。
    """
    # 構建輸出圖片的完整路徑
    output_path = os.path.join(output_folder, filename)
    # 保存圖片
    image.save(output_path)


if __name__ == "__main__":
    main()
