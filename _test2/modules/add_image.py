from tkinter import filedialog
from PIL import Image, ImageTk

# 이미지 선택 함수
def choose_image(label, size=(90, 90)):
    """
    이미지 파일 선택 후 지정된 라벨에 표시합니다.
    
    :param label : 이미지가 표시될 tkinter.Label 객체
    :param size  : 이미지 리사이즈시 크기 (기본값 (90, 90))
    :return      : 이미지 객체 (필요시 외부에서 참조 가능)
    """

    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png;*jpg;*jpeg;*.gif")]
    )

    if file_path:

        # 이미지 열고 리사이즈
        img = Image.open(file_path)
        img = img.resize((80, 80))
        tk_img = ImageTk.PhotoImage(img)

        # 이미지 표시
        label.config(image=tk_img)
        label.img = tk_img

        # 외부에서 참조 가능하게 반환
        return tk_img
    
    return None

