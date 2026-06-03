1) Pomodoro basic, timer and the usual features
2) Rock vs Mine prediction used linear regression to find if the object is a rock or a mine from the given data.
3) Doc-Intelligence, useds claude API to give a summary, key points and answer questions based on the .docx or whatever content you've pasted.
4) Prob1 is a QR code decoder, it decodes QR codes assigned in the Images folder and stores in a .csv file.
5) Qrscanner2 is upgraded version of the previous QR scanner/decoder. It can now use CV to read real time QR codes and decode them, since camera not available added a mock camera to test it (also has code incase a real camera is invovled). It also has a dashboard which displays crucial information along with the QR its decoding and stores in a csv.

note: commands to run node.js 
npm create vite@latest my-project-name -- --template react
cd my-project-name
npm install
npm run dev
