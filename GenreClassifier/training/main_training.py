import os
import call
import numpy as np
from pathlib import Path
import pandas as pd
final_dict={"Name":[],"Action_rgb":[],"Romance_rgb":[],"Drama_rgb":[],"Horror_rgb":[],"Action":[],"Drama":[],"Horror":[],"Romance":[],"Action_audio":[],"Romance_audio":[],"Drama_audio":[],"Horror_audio":[]}

path_dir = input("enter the path of the video folder\n")
path = Path(path_dir)
for video_path in os.listdir(path_dir):
    if video_path[0]!='.':
        new_path=os.path.join(path_dir,video_path)
        print(new_path)
        name=video_path.split(".")[0]
        result_dict=call.call(new_path)
        for key in final_dict.keys():
            if(key=="Name"):
                final_dict[key].append(name)
            else:
                final_dict[key].append(result_dict[key][0])
    
df=pd.DataFrame(final_dict)
df.to_csv(os.path.join(os.getcwd(),"final_results.csv"),index=False)