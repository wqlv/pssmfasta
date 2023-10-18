import os
import subprocess

def generate_pssm(fasta_file, output_dir):
    # 检查输出目录是否存在，如果不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 设置 BLAST 路径和数据库路径
    blast_path = r"D:\blast-2.14.0+\bin\psiblast"  # 根据你的实际路径进行修改
    db_path = r"D:\blast-2.14.0+\db\swissprot"  # 根据你的实际路径进行修改

    # 获取文件名（不带扩展名）
    filename = os.path.splitext(os.path.basename(fasta_file))[0]

    # 构建 PSSM 输出文件路径
    pssm_file = os.path.join(output_dir, f"{filename}.pssm")

    # 构建 BLAST 命令行参数
    cmd = [
        blast_path,
        "-query", fasta_file,
        "-db", db_path,
        "-num_iterations", "16",
        "-out_ascii_pssm", pssm_file
    ]

    # 调用 BLAST 执行命令
    subprocess.run(cmd)

    # 检查 PSSM 文件是否生成成功
    if os.path.isfile(pssm_file):
        print(f"PSSM 文件生成成功！({pssm_file})")
    else:
        print("PSSM 文件生成失败。")

# 主程序入口
if __name__ == "__main__":
    input_dir = r"D:\blast-2.14.0+\input"  # 根据你的实际路径进行修改
    output_dir = r"D:\blast-2.14.0+\output"  # 根据你的实际路径进行修改

    # 遍历输入目录中的所有 FASTA 文件
    for filename in os.listdir(input_dir):
        if filename.endswith(".fasta"):
            fasta_file = os.path.join(input_dir, filename)
            generate_pssm(fasta_file, output_dir)


