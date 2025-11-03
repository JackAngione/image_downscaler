# image_downscaler
Completely Lossless FFMPEG-based Image Downscaler!   
*Made this because most image downscalers do not preserve HDR*  
  
**Must install FFMPEG first**  
Windows: `winget install ffmpeg`  
MacOS: `brew install ffmpeg`  
(Debian) Linux: `sudo apt install ffmpeg`  

- Supports HDR images! (tested on AVIF)
- Batch processes images in a folder
- Controlable quality parameter
- Use Nearest Neighbor filter for fine detail preservation and perfect scaling clarity.
- Use Lanzcos if you encounter moire or similar artifacts

