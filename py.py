
import ast
import os
import subprocess

# プロジェクトのディレクトリ
project_dir = './'

# pyreverseを使用してUML図を生成
subprocess.run(['python', '-m', 'pylint.pyreverse', '-o', output_format, '-p', project_name, project_dir])


# 設計書を作成するためのテンプレート
design_doc_template = """
Design Document
===============

"""

# プロジェクト内のすべてのPythonファイルを走査
for root, dirs, files in os.walk(project_dir):
    for file in files:
        if file.endswith('.py'):
            # Pythonファイルのフルパスを取得
            file_path = os.path.join(root, file)

            # ソースコードを読み込む
            with open(file_path, 'r', encoding='utf-8') as f:
                source_code = f.read()

            # ソースコードを抽象構文木に変換
            tree = ast.parse(source_code)

            # 抽象構文木を走査して関数とクラスを見つける
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # 関数の名前、引数、ドキュメンテーション文字列を抽出
                    function_name = node.name
                    arguments = [arg.arg for arg in node.args.args]
                    docstring = ast.get_docstring(node)

                    # 設計書に関数の詳細を追加
                    design_doc_template += f"""
File: {file_path}
Function: {function_name}
Arguments: {arguments}
Docstring: {docstring}
"""
                elif isinstance(node, ast.ClassDef):
                    # クラスの名前とドキュメンテーション文字列を抽出
                    class_name = node.name
                    docstring = ast.get_docstring(node)

                    # 設計書にクラスの詳細を追加
                    design_doc_template += f"""
File: {file_path}
Class: {class_name}
Docstring: {docstring}
"""

# 設計書をファイルに書き出す
with open('design_doc.txt', 'w') as f:
    f.write(design_doc_template)