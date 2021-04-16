@ECHO OFF 
cmd
Echo Merk
dir
cd aagayam
dir
uvicorn src.server:app --reload
cd ..
cd kaatru
npm run serve
PAUSE