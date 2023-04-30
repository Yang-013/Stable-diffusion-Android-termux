# Stable-diffusion-Android-termux
Run SD onnx model on termux(no root)
Download and install Termux from Fdroid https://f-droid.org/repo/com.termux_118.apk
In termux type:
apt update && apt upgrade
then mount internal sdcard with:
termux-setup-storage
Now install ubuntu distro:
pkg install proot-distro
then run:
proot-distro install ubuntu
once download and installation is completed login to ubuntu :
proot-distro install ubuntu
you will root@localhost on screen
now download and install required packages :
apt install python python3 nano git git-lfs wget 
nano is text editor
Now instal SD onnx dependencies
pip install --upgrade diffusers transformers accelerate ftfy xformers onnx onnxruntime torch
Download onnx model from hugging face
