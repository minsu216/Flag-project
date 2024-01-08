# import io
# from IPython.display import display
# import cv2
# from flask import Flask, render_template, request,send_from_directory
# from PIL import Image
# import os
# import base64

# import torch
# from ultralytics import YOLO

# app = Flask(__name__)

# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Ensure 'uploads' folder exists
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# @app.route("/")
# def hello_world():
#     return render_template('indexs.html')

# @app.route('/detect', methods=['GET', 'POST'])
# def predict_img():
#     if 'file' not in request.files:
#         return render_template('indexs.html', error='No file part')

#     file = request.files['file']
#     if file.filename == '':
#         return render_template('indexs.html', error='No selected file')

#     if file:
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(filepath)

#         file_extension = file.filename.rsplit('.', 1)[1].lower()

#         if file_extension == 'jpg':
#             image = Image.open(filepath)
#             yolo = YOLO('best_20_80_576.pt')
#             detections = yolo.predict(image, save=True)

#             # 결과를 HTML 페이지에 표시할 수 있는 형식으로 변환
#             results_html = ""
#             for detection in detections:
#                 results_html += f"<p>{detection}</p>"

#             # 이미지를 base64로 인코딩하여 HTML 페이지에 삽입
#             img_str = image_to_base64(image)

#             return render_template('result.html', image=img_str, results=results_html)




# def image_to_base64(image):
#     buffered = io.BytesIO()
#     image.save(buffered, format="JPEG")
#     img_str = "data:image/jpeg;base64," + base64.b64encode(buffered.getvalue()).decode()
#     return img_str
# def display(filename):
#     folder_path ='runs/detect'
#     subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path,f))]
#     latest_subfolder = max(subfolders,key=lambda x: os.path.getctime(os.path.join(folder_path,x)))
#     directory = folder_path +'/'+latest_subfolder
#     print('printing directory:',directory)
#     files=os.listdir(directory)
#     latest_file=files[0]

#     filename = os.path.join(folder_path,latest_subfolder,latest_file)
#     file_extension =filename.rsplit('.',1)[1].lower()
#     environ =request.environ
#     if file_extension =='jpg':
#         return send_from_directory(directory,latest_file,environ)
#     else:
#         return "invalid file format"

# if __name__ == '__main__':
#     app.run(debug=True)