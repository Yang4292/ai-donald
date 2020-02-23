         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


Introduction: 
    This a text generator that tries to generate Donald's new Twitter based on his pervious speech material.
    
Author:
    This project is done by Jared Robbins, Tanner Marshall and Taoqi Yang.
    
Description:
    We first collected big set of data of the Donald's past speeches and then built a machine learning model in tensorflow which is trained by 
the data set. Based on the model, we predict the next words using current and previous words. 
    In practice, we need to the user to feed a heading to start the model. After the execution of model, the generated text will be post to
twitter with id "Ai Donald" 

Possible improvement:
    Modify the algorithm and logic in the model to let it has a better prediction of the next word.
    
    
reference:
    The process in model building refers techniques shown on this website: https://www.tensorflow.org/tutorials/text/text_generation
    The picture of background refers to picture: https://assets.donaldjtrump.com/2017/web/hero_images/hero_marine_one.jpg
    