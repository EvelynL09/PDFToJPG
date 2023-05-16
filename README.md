# PDFToJPG
A Python script to convert PDFs to JPG images using pdf2image library.

## Configuring the Environment on Windows

To run the script on Windows, you'll need to install the necessary Python packages and the Poppler utility. Follow these steps to configure your environment:

1. Install the required Python packages by running `pip install -r requirements.txt` in a command prompt or terminal window.

2. Install Poppler:
    - Download the latest version of Poppler for Windows from [Poppler Windows Releases](https://github.com/oschwartz10612/poppler-windows/releases/).
    - Extract the contents of the downloaded `.zip` archive to a directory on your computer, such as `C:\Software\poppler`.
    - Add the path to the `Library\bin` directory within the extracted Poppler directory (e.g., `C:\Software\poppler\Library\bin`) to your system's `PATH` environment variable.
    - Open a new command prompt window and run `pdftoppm -v` to verify that Poppler has been installed correctly and is available in your `PATH`.

After completing these steps, you should be able to run the script on your Windows computer.

## Running the Script

After completing the steps above to configure your environment, you can run the script by opening a command prompt or terminal window, navigating to the directory containing the script, and running the following command:
```cmd
python3 converter.py
```
This will execute the script using Python 3 and convert all the PDF files in the `input` directory to JPG images in the `output` directory.

## 配置使用环境 - 以Windows为例
1. 安装需要的python包`pip install -r requirements.txt`
2. 安装poppler
    - 从[Poppler Windows Releases](https://github.com/oschwartz10612/poppler-windows/releases/)下载安装包，解压到指定文件夹
    - 配置系统环境变量，将解压后的`Libary/bin`所在路径加入`PATH`变量，e.g. `C:\Software\poppler\Library\bin`
    - 新打开一个命令行窗口，执行`pdftoppm -v`确认配置成功

## 执行脚本
```cmd
python3 converter.py
```
这个脚本将会把所有`input`路径下的PDF转为JPG图片到`output`路径下