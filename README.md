1) Pomodoro basic, timer and the usual features.
2) Rock vs Mine prediction used linear regression to find if the object is a rock or a mine from the given data.
3) Doc-Intelligence, useds claude API to give a summary, key points and answer questions based on the .docx or whatever content you've pasted.
4) Prob1 is a QR code decoder, it decodes QR codes assigned in the Images folder and stores in a .csv file.
5) Qrscanner2 is upgraded version of the previous QR scanner/decoder. It can now use CV to read real time QR codes and decode them, since camera not available added a mock camera to test it (also has code incase a real camera is invovled). It also has a dashboard which displays crucial information along with the QR its decoding and stores in a csv.
6) ALPR_Project - Automatic License Plate Recognition, recoginises license plates. Has image processing using OpenCV, plate and character detection using YOLOV11. Uses mock camera, similar to previous project. Needs python version 11 to run it. Used roboflow to train the model, also to run the model use roboflow api.
7) Image Processing Toolkit is a desktop application built using Python, OpenCV, Tkinter, Pillow, and NumPy that allows users to load images from a local data folder, apply various image processing operations through a graphical user interface, preview results instantly, and save processed images. The toolkit supports operations such as grayscale conversion, color conversion, blurring, sharpening, edge detection, thresholding, brightness and contrast adjustment, denoising, image transformations, and more.
Tkinter for GUI. Pillow for image format conversion and rendering inside Tkinter, without it Tkinter cannot render open CV images. Numpy for storing images.
8) OpenCV Image Studio is a desktop image-editing application built using Python, OpenCV, and CustomTkinter. It allows users to load images, apply image-processing operations through a plugin system, create reusable processing pipelines, perform batch processing on entire folders, compare original and edited images side-by-side, view image statistics, and manage editing history through undo/redo functionality.




note: commands to run node.js 
npm create vite@latest my-project-name -- --template react
cd my-project-name
npm install
npm run dev
