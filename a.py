
import subprocess

# プロジェクトのディレクトリ
project_dir = './'

# プロジェクト名
project_name = 'ProjectName'

# 出力フォーマット
output_format = 'png'

# pyreverseのフルパス
pyreverse_path = 'C:\\Users\\sakaj\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python310\\site-packages\\pylint\\pyreverse\\main.py'  # ここを実際のパスに置き換えてください

# pyreverseを使用してUML図を生成
subprocess.run(['python', pyreverse_path, '-o', output_format, '-p', project_name, project_dir])