try:
    import os
    import video_extractor
    import delete_images
    import CNNworking
    import final_working
    current_path = os.getcwd()
    movie_extraction_path = os.path.join(current_path, 'movie_extraction')
    try:
        if os.path.exists(os.path.join(os.getcwd(), 'movie_extraction')) == False:
            os.makedirs(os.path.join(os.getcwd(), 'movie_extraction'))
            print('!!!!  DO NOT DARE TO TOUCH MY DIRECTORIES AGAIN!!!')
        else:
            print('all good to go')
    
        try:
            video_extractor.extractframes(movie_extraction_path)
            try:
                final_dic = CNNworking.model()
                print('\n\n\nHere comes your result\n')
                for key,value in final_dic.items():
                    print(key + '-->%2.2f percent'%(value))
                input('press enter to continue')
                try:
                    delete_images.empty_folder(movie_extraction_path)
                except:
                    print('deleting images failure')
                    input('press enter to exit')
            except:
                print('model failure')
                input('press enter to exit')
        except:
            print('can\'t find video, u forgot the path')
            input('press enter to exit')

    except:
        print('error')
        input('press enter to exit')    
except:
    print("files not found")
    input('press enter to exit')

