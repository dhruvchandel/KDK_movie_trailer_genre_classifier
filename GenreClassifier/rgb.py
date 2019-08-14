

def main():

    import numpy as np
    import cv2
    from matplotlib import pyplot as plt
    import os
    import h5py
    from keras.models import load_model
    import shutil

    label_to_genre={0:"action",1:"romance",2:"drama",3:"horror"}

    
    dir_path=os.path.join(os.getcwd(),"movie_extraction")

    count2=0

    # Funtion for finding mean rgb of an image
    def mean_image_color(imgedit) :
        Red=np.mean(imgedit[:,:,0])
        Green=np.mean(imgedit[:,:,1])
        Blue=np.mean(imgedit[:,:,2])
        return (Red,Green,Blue)

    mean_rgb_list = []

    def mean_rgb_extractor(dir_path):
        for internal_dir_path in os.listdir(dir_path):
            if internal_dir_path != ".DS_Store" :
                img = cv2.imread(os.path.join(dir_path, internal_dir_path))
                imgedit = cv2.resize(src=img , dsize = (28,28))
                mean_rgb_list.append(mean_image_color(imgedit))
                # print(mean_rgb_list)
            else : 
                pass

    mean_rgb_extractor(dir_path)

    # dir_path is dictory containing images ;)

    def net_average_rgb(mean_rgb_list=mean_rgb_list) :
        sum_red = 0
        sum_green = 0
        sum_blue = 0

        for x in range(0,len(mean_rgb_list)) :
            for z in range(0,3) :
                if z==0 :
                    sum_blue = sum_blue + mean_rgb_list[x][0]
                if z==1 :
                    sum_green = sum_green + mean_rgb_list[x][1]
                if z==2 :
                    sum_red = sum_red + mean_rgb_list[x][2]
        return (sum_red/len(mean_rgb_list), sum_green/len(mean_rgb_list), sum_blue/len(mean_rgb_list))

    def predict_genre():
        X=np.array([])
        X = np.append(X,net_average_rgb()[0])
        X = np.append(X,net_average_rgb()[1])
        X = np.append(X,net_average_rgb()[2])
        X=np.reshape(X,(-1,X.shape[0]))
        
        path=os.path.join(os.getcwd(),"models")
        model=load_model(os.path.join(path,"model_rgb.h5py"))

        y_pred=model.predict(X)
        y_pred=np.reshape(y_pred,(4,))           

        results_dict={"Action_rgb":[],"Romance_rgb":[],"Drama_rgb":[],"Horror_rgb":[]}
        results_dict["Action_rgb"].append(y_pred[0]*100)
        results_dict["Romance_rgb"].append(y_pred[1]*100)
        results_dict["Drama_rgb"].append(y_pred[2]*100)
        results_dict["Horror_rgb"].append(y_pred[3]*100)

        return results_dict

    d=predict_genre()
    return d








