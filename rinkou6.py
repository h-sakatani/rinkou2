import os
import sys
import argparse
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="make figure of testdir")
    parser.add_argument("dirname", help="first file path", type=str)
    parser.add_argument("-n","--newdir", help="new output dir", type=str, default="output")

    args = parser.parse_args()

    dpath = args.dirname
    files_name = os.listdir(dpath)

    new_dir = args.newdir
    os.makedirs(new_dir, exist_ok=True)

    for file in files_name:
        file_path = dpath + file
        df = pd.read_csv(file_path, sep='\t', skiprows=6, index_col='Strand shift')
        
        plt.figure(figsize=(4,4))
        plt.plot(df.iloc[:,3], color="red")
        plt.xlim(0,500)
        plt.xlabel("index") 
        plt.ylabel("per control")

        newfigure = file.split(".", 1)[0]

        plt.savefig(new_dir + "/" + newfigure + ".pdf") 
        plt.close()      
    