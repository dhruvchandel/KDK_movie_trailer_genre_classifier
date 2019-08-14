import librosa
import os
import numpy as np
import pandas as pd
from keras.models import load_model
import moviepy.editor as mp

label_dict={"action":0,"romance":1,"drama":2,"horror":3} 
label_to_genre={0:"action",1:"romance",2:"drama",3:"horror"}


def time_differ(onset_frames,x,sr,onset_envelope) :
    N = len(x)
    T = N/float(sr)
    t = np.linspace(0, T, len(onset_envelope))
    td=t[onset_frames]
    time_difference = []
    if td.shape[0] ==1:
        time_difference.append(td[0])
    else:
        for i in range(1,td.shape[0]):
            z=td[i]-td[i-1]
            time_difference.append(z)
    time_difference=np.array(time_difference)
    avg_time=time_difference.mean()
    return avg_time


def get_mfcc(data,sr,n_mfcc=13):
    mfcc=librosa.feature.mfcc(data,sr,n_mfcc=n_mfcc)
    mfcc_mean=np.zeros((n_mfcc,))
    for i in range(mfcc.shape[0]):
        mfcc_mean[i]=(mfcc[i].mean())
    return mfcc_mean
    


    
def predict_genre(path):
    
    current_path = os.getcwd() 
    audio_path_dir=os.path.join(current_path,"Extracted_Audios")
    name="sample"
    clip=mp.AudioFileClip(path)
    if os.path.exists(os.path.join(current_path, "Extracted_Audios")) == False:
        os.makedirs(os.path.join(current_path,"Extracted_Audios"))
    clip.write_audiofile(audio_path_dir+'/'+name+".mp3")
             
        
    audio_path=audio_path_dir+'/'+name+".mp3"
    data1,sr1=librosa.load(audio_path)
    data2,sr2=librosa.load(audio_path,sr=1000)

    # feature extraction
    if(data1.shape[0]==0 or data2.shape[0]==0):
        print("Audio Inappropriate")
        exit()
    else:
        X=np.array([])
        mfcc=get_mfcc(data1,sr1)
        rms=librosa.feature.rms(y=data1).mean()
        onset_envelope = librosa.onset.onset_strength(data2 , sr = sr2)
        onset_frames = librosa.util.peak_pick(onset_envelope, 4, 4, 4, 4, 0.5, 5)
        avg_time=time_differ(onset_frames,data2,sr2,onset_envelope)
        X=np.append(X,mfcc)
        X=np.append(X,rms)
        X=np.append(X,onset_frames.shape[0])
        X=np.append(X,avg_time)
        X=np.reshape(X,(-1,X.shape[0]))
        model_path = os.path.join(current_path, 'models')
        model=load_model(os.path.join(model_path, "model_classweights.h5py"))

        y_pred=model.predict(X)
        y_pred=np.reshape(y_pred,(4,))
                
        name=name+".mp3"       
        os.remove(os.path.join(audio_path_dir,name))
        os.rmdir("Extracted_Audios")
        results_dict={"Action_audio":[],"Romance_audio":[],"Drama_audio":[],"Horror_audio":[]}
        if y_pred[0]=="nan":
            results_dict={"Action_audio":[0],"Romance_audio":[0],"Drama_audio":[0],"Horror_audio":[0]}       
        else:        
            results_dict["Action_audio"].append(y_pred[0]*100)
            results_dict["Romance_audio"].append(y_pred[1]*100)
            results_dict["Drama_audio"].append(y_pred[2]*100)
            results_dict["Horror_audio"].append(y_pred[3]*100)
        
        return results_dict



