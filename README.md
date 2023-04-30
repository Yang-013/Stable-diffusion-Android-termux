# Stable-diffusion-Android-termux 
Run SD onnx model (cpu)

Device: Redmi note 8 pro(Android 11)


CPU: Mediatek Helio G90T (12nm)


RAM: 6GB


Storage: Need 20GB free space

It takes around 5 minutes to generate 256*512 image with 8 steps

int8 quantized model take 2 minutes for the same

# Install termux from Fdroid
https://f-droid.org/repo/com.termux_117.apk


In termux type
> apt update && apt upgrade

then mount internal sdcard
>termux-setup-storage

Give required permission

# Install ubuntu distro
>pkg install proot-distro

once above proot distro is installed run

>proot-distro install ubuntu

login to proot distro

>proot-distro login ubuntu

>apt update && apt upgrade

Install python git and nano text editor

>apt install python3 python3-pip git git-lfs wget nano

once above packages are installed then install dependencies

>pip3 install --upgrade diffusers transformers accelerate ftfy xformers onnx onnxruntime torch

clone stable diffusion 1.5 onnx model from huggingface

>git clone -b onnx https://huggingface.co/runwayml/stable-diffusion-v1-5

it will take a while as more than 10GB data will be downloaded

you can also download SD 1.4 from huggingface if you want to use 1.4

>git clone -b onnx https://huggingface.co/CompVis/stable-diffusion-v1-4

int8 quantized model can be run using same script for faster generation but quality will take the hit

>git clone https://huggingface.co/ClashSAN/miniSD-quantized-onnx

clone this git to download txt2img script and lpw pipeline 

run script with command

>python3 sd.py

you can move generated image to sdcard with below command as sdcard is mounted

>mv test.png /sdcard

you can view the image from usual file manager or gallery

you can edit script to change model path and prompt using nano text editor as needed

> nano sd.py

once required changes are done press ctrl+o then enter key then ctrl+x to exit

# Face restoration using gfpgan on android

Tested on same device, Face restoration works perfectly fine but termux crashes when bg upscaler realesrgan is used due to limited RAM

Follow the step on below git once you are logged in as root@localhost in termux ubuntu

https://github.com/TencentARC/GFPGAN


# Image upscale using ESRGAN on android(uses android gpu)

Tumuyan has android app for easy upscaling, works amazing

visit

https://github.com/tumuyan/RealSR-NCNN-Android
