import os
import call
import numpy as np
import finalANNworking
from pathlib import Path
import pandas as pd
ans_dict={"Name":[],"Genre":[]}
path_dir = input("enter the path of the video folder\n")
path = Path(path_dir)
for video_path in os.listdir(path_dir):
    if video_path[0]!='.':
        new_path=os.path.join(path_dir,video_path)
        print(new_path)
        name=video_path.split(".")[0]
        result_dict=call.call(new_path)
        final_dict={"Name":[],"Action_rgb":[],"Romance_rgb":[],"Drama_rgb":[],"Horror_rgb":[],"Action":[],"Drama":[],"Horror":[],"Romance":[],"Action_audio":[],"Romance_audio":[],"Drama_audio":[],"Horror_audio":[]}
        for key in final_dict.keys():
            if(key=="Name"):
                final_dict[key].append(name)
            else:
                final_dict[key].append(result_dict[key][0])

        ans=finalANNworking.final_model(final_dict)
        ans_dict["Name"].append(ans["Name"][0])
        ans_dict["Genre"].append(ans["Genre"])
        print("\nFinal Predicted Genre :{} \n".format(ans["Genre"]))

    
df=pd.DataFrame(ans_dict)
p=os.path.join(os.getcwd(),"test_results")
df.to_csv(os.path.join(p,"results.csv"),index=False)
