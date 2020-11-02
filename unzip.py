import argparse
from zipfile import ZipFile

parser = argparse.ArgumentParser()
parser.add_argument("zip_path")
args = parser.parse_args()


def unzip(zip_path, save_dir='data/'):
    '''
    解压 AKOA 数据，并将左右膝盖分开
    '''
    Z = ZipFile(zip_path)
    # 解压数据
    for path in Z.namelist():
        # 解压 left knee
        if 'left' in path.lower() or 'l_e_f_t' in path.lower():
            Z.extract(path, save_dir+'left')

    for path in Z.namelist():
        # 解压 right knee
        if 'right' in path.lower() or 'r_i_g_h_t' in path.lower():
            Z.extract(path, save_dir+'right')
    Z.close()


if __name__ == "__main__":
    unzip(args.zip_path, save_dir='data/')
