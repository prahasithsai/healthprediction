# Import the required libraries
import pandas as pd
data = pd.read_excel(r"G:\lms\Project_DS\DS_Project_Team_66\DS_66_Dataset\Data.xlsx") 
 
# Label the scores for all the given columns in the dataset
data['Are you still going to school?'] = data['Are you still going to school?'].map({'No, I am at home':4,"Yes, most days of the week":3,"Yes, sometimes":2,'I am in a different school from my own school':1})
data['Are you still going to school?'] = data['Are you still going to school?'].fillna(0)

data['Do you have any other children living in your house with you?'] = data['Do you have any other children living in your house with you?'].map({'Yes':1,"No":0})
data['Do you have any other children living in your house with you?'] = data['Do you have any other children living in your house with you?'].fillna(0)

data['How many people live in your home with you (including adults)?'] = data['How many people live in your home with you (including adults)?'].map({1:1,2:2,3:3,4:4,5:5,"6+":6})
data['How many people live in your home with you (including adults)?'] = data['How many people live in your home with you (including adults)?'].fillna(0)

data['What year are you in now?'] = data['What year are you in now?'].map(lambda x: x.lstrip('Year ').rstrip(''))
data['What year are you in now?'] = data['What year are you in now?'].astype(int)

data['Gender'] = data['Gender'].map({'Girl':0,"Boy":1})

data.rename(columns={'1. What did you eat for breakfast YESTERDAY?': 'breakfast YESTERDAY'}, inplace=True)
data['breakfast YESTERDAY'] = data['breakfast YESTERDAY'].str.split(';').str[0]
data['breakfast YESTERDAY'] = data['breakfast YESTERDAY'].str.split('and').str[0]
data['breakfast YESTERDAY'] = data['breakfast YESTERDAY'].str.split('-').str[0]
data['breakfast YESTERDAY'] = data['breakfast YESTERDAY'].map(lambda x: x.rstrip(' ')).str.lower()
data['breakfast YESTERDAY'] = data['breakfast YESTERDAY'].replace(dict.fromkeys(["crackerbread","pankaces","breadsticks","tostie s","brioch","waffles with chocolate spread","hot cross bun","toast","croissants with cheese","bacon muffins","bacon bap","pancake","pancakes","jam sandwich","croissants","sausage roll","wrap","sausage s","bread roll","waffles","brioche","a toastie","2 x pancakes","egg waffles","beans on toast","snacks","biscuits","homemade pancakes","brioche roll","freshly baked bread","mackrel on toast","bagel"],"Toast Food"))
data['breakfast YESTERDAY'] = data['breakfast YESTERDAY'].replace(dict.fromkeys(["boiled sausages","healthy cereal e.g. porridge, weetabix, readybrek, muesli, branflakes, cornflakes","fruit;toast;yoghurt","boiled eggs","shreddies","marshmallow mates","egg","eggs","sausage & egg s","cheese","sardines"],"Healthy Food"))
data['breakfast YESTERDAY'] = data['breakfast YESTERDAY'].replace(dict.fromkeys(["fruit","fruit;toast;yoghurt","yoghurt","apple, pear, grapes, yogurt, brioche"],"Fruit Food"))
data['breakfast YESTERDAY'] = data['breakfast YESTERDAY'].replace(dict.fromkeys(["danish","waffle","pain au choclat","pan au chocolate","pain au chocolat","sugary cereal e.g. cocopops, frosties, sugar puffs, chocolate cereals","chocolate crepe","chocolate finger","pain au chocolate","crumpets with chocolate spread","croissants","jam s","pancakes with chocolate spread","nutella","pop tarts","chocolate spread on bread","pano chocolate"],"Sugary Food"))
data['breakfast YESTERDAY'] = data['breakfast YESTERDAY'].replace(dict.fromkeys(["nothing"],"No Food"))
data['breakfast YESTERDAY'] = data['breakfast YESTERDAY'].replace(dict.fromkeys(["egg on toast","waffles mum made them","pancakes & strawberries","chesse","healthy shake","tea","cheesey beans","smoothy"],"Other Food"))
data['breakfast YESTERDAY'] = data['breakfast YESTERDAY'].replace(dict.fromkeys(["crumpet","crumpets","cooked breakfast","cheese omlet","crumpets with marmite","homemade pancakes with fruit","homemade pancakes","belgian pancakes (it was my mums birthday)"],"Cooked Food"))
data['breakfast YESTERDAY'] = data['breakfast YESTERDAY'].map({'No Food':0,"Healthy Food":1,"Toast Food":2,"Sugary Food":3,"Fruit Food":4,"Cooked Food":5,"Other Food":6})

data['2. Did you eat any fruit and vegetables YESTERDAY? '] = data['2. Did you eat any fruit and vegetables YESTERDAY? '].map({'2 Or More Fruit and Veg':2,"1 Piece":1,"No":0})

data4 = data.iloc[:,12:14]
data4['4. What time did you fall asleep YESTERDAY (to the nearest half hour)?'] = data4['4. What time did you fall asleep YESTERDAY (to the nearest half hour)?'].map({'10:00pm':2,"9:30pm":2.5,"9:00pm":3,'10:30pm':1.5,'8:30pm':3.5,
      '11:00pm':1,'11:30pm':0.5,'8:00pm':4,'12:00am':0,'12:30am':0.5,'7:30pm':4.5,'2:00am':2,'7:00pm':5,'1:00am':1,'1:30am':1.5})
data4['5. What time did you wake up TODAY (to the nearest half hour)?'] = data4['5. What time did you wake up TODAY (to the nearest half hour)?'].map({'8:00am':8,'7:30am':7,'8:30am':8.5,'9:00am':9,'7:00am':7,'9:30am':9.5,'6:30am':6.5,
      '10:00am':10,'6:00am':6,'10:30am':10.5,'11:30am':11.5,'11:00am':11,'5:30am':5.5,'5:00am':5})
data4 = data4.fillna(0)
data4['sleeping hours'] = data4['4. What time did you fall asleep YESTERDAY (to the nearest half hour)?'] + data4['5. What time did you wake up TODAY (to the nearest half hour)?']

data5 = data.iloc[:,14:21]
data5.columns = ["activities","you watch TV","feel tired","school work","drink","sweets","Chinese takeaway"]
data5["activities"] = data5["activities"].map({'7 days':7,"3-4 days":4,"5-6 days":6,'1-2 days':2,'0 days':0})
data5["you watch TV"] = data5["you watch TV"].map({'7 days':7,"3-4 days":4,"5-6 days":6,'1-2 days':2,'0 days':0})
data5["feel tired"] = data5["feel tired"].map({'7 days':7,"3-4 days":4,"5-6 days":6,'1-2 days':2,'0 days':0})
data5["school work"] = data5["school work"].map({'7 days':7,"3-4 days":4,"5-6 days":6,'1-2 days':2,'0 days':0})
data5["drink"] = data5["drink"].map({'7 days':7,"3-4 days":4,"5-6 days":6,'1-2 days':2,'0 days':0})
data5["sweets"] = data5["sweets"].map({'7 days':7,"3-4 days":4,"5-6 days":6,'1-2 days':2,'0 days':0})
data5["Chinese takeaway"] = data5["Chinese takeaway"].map({'7 days':7,"3-4 days":4,"5-6 days":6,'1-2 days':2,'0 days':0})

data["14. From your house, can you easily walk to a park (for example a field or grassy area)?"] = data["14. From your house, can you easily walk to a park (for example a field or grassy area)?"].map({'Yes':1,"No":0})
data["15. From your house, can you easily walk to somewhere you can play?"] = data["15. From your house, can you easily walk to somewhere you can play?"].map({'Yes':1,"No":0})
data["16. Do you have a garden?"] = data["16. Do you have a garden?"].map({'Yes':1,"No":0})
data['17. How often do you go out to play outside?'] = data['17. How often do you go out to play outside?'].map({'Most days':4,"I don't play":3,"Hardly ever":2,'A few days each week':1})
data['17. How often do you go out to play outside?'] = data['17. How often do you go out to play outside?'].fillna(0)
data['18. Do you have enough time for play?'] = data['18. Do you have enough time for play?'].map({'Yes, I have loads':3,"Yes, it's just about enough":4,"No, I would like to have a bit more":2,'No, I need a lot more':1})
data['18. Do you have enough time for play?'] = data['18. Do you have enough time for play?'].fillna(0)
data['19. What type of places do you play in?'] = data['19. What type of places do you play in?'].str.split(';').str[0]
data['19. What type of places do you play in?'] = data['19. What type of places do you play in?'].map({"In my house":3,"In my garden":2,"In a place with bushes, trees and flowers":1,"On the bike or skate park":5,"On a local grassy area":4,"In the street":6,"Out the front of my house":6,"In the woods near my house":6})
data['20. Can you play in all the places you would like to?'] = data['20. Can you play in all the places you would like to?'].map({'I can play in some of the places I would like to':3,"I can play in all the places I would like to":4,"I can only play in a few places I would like to":2,'I can hardly play in any of the places I would like to':1})
data['21. Do you have somewhere at home where you have space to relax?'] = data['21. Do you have somewhere at home where you have space to relax?'].map({'Yes':2,"Sometimes but not all the time":1,"No":0})

data3 = data.iloc[:,30:34]
data3.rename(columns={"22. Tell us if you agree or disagree with the following: [I am doing well with my school work]": 'well with my school work',
                      "22. Tell us if you agree or disagree with the following: [I feel part of my school community]": 'feel part of my school community',
                      "22. Tell us if you agree or disagree with the following: [I have lots of choice over things that are important to me]" : 'important to me',
                      "22. Tell us if you agree or disagree with the following: [There are lots of things I'm good at]": 'things Iam good at'}, inplace=True)
data3['well with my school work'] = data3['well with my school work'].map({'Agree':2,'Strongly agree':1,"Don't agree or disagree":5,'Disagree':3,'Strongly disagree':4})                                                                                              
data3['feel part of my school community'] = data3['feel part of my school community'].map({'Agree':2,'Strongly agree':1,"Don't agree or disagree":5,'Disagree':3,'Strongly disagree':4})
data3['important to me'] = data3['important to me'].map({'Agree':2,'Strongly agree':1,"Don't agree or disagree":5,'Disagree':3,'Strongly disagree':4})
data3['things Iam good at'] = data3['things Iam good at'].map({'Agree':2,'Strongly agree':1,"Don't agree or disagree":5,'Disagree':3,'Strongly disagree':4})

data1 = data.iloc[:,40:56]
data1.columns =['I feel lonely','I cry a lot','I am unhappy','I feel nobody likes me','I worry a lot','I have problems sleeping','I wake up in the night',
                'I am shy','I feel scared','I worry when I am at school','I get very angry','I lose my temper','I hit out when I am angry','I do things to hurt people',
                'I am calm','I break things on purpose']
data1['I am calm'] = data1['I am calm'].map({'Never':2,'Sometimes':1,'Always':0})
data2 = data1.iloc[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,15]]
data2.replace({'Never':0,'Sometimes':1,'Always':2}, inplace=True)
data1 = pd.concat([data2,data1['I am calm']],axis='columns')
data1["emmotion"] = data1["I feel lonely"] + data1["I cry a lot"] + data1["I am unhappy"] + data1["I feel nobody likes me"] + data1["I worry a lot"] + data1["I have problems sleeping"] + data1["I wake up in the night"] + data1["I am shy"] + data1["I feel scared"] + data1["I worry when I am at school"]
data1["behaviour"] = data1['I get very angry'] + data1["I lose my temper"] + data1["I hit out when I am angry"] + data1["I do things to hurt people"] + data1["I am calm"] + data1["I break things on purpose"]
data1["emmotion_scale"]="<=5"
data1.loc[data1["emmotion"]<=9,"emmotion_scale"]="expected difficulties"
data1.loc[data1["emmotion"]==10,"emmotion_scale"]="borderline difficulties"
data1.loc[data1["emmotion"]==11,"emmotion_scale"]="borderline difficulties"
data1.loc[data1["emmotion"]>=12,"emmotion_scale"]="clinically significant difficulties"
data1["behaviour_scale"]="<=5"
data1.loc[data1["emmotion"]<=5,"behaviour_scale"]="expected difficulties"
data1.loc[data1["emmotion"]==6,"behaviour_scale"]="borderline difficulties"
data1.loc[data1["emmotion"]>=7,"behaviour_scale"]="clinically significant difficulties"
mmf = data1.iloc[:,18:]

data.rename(columns={"25. Are you able to keep in touch with your family that you don't live with? (grand parents, Uncle, Aunt, Cousins, etc)": 'keep in touch with family',"26. Are you able to keep in touch with your friends?":'keep in touch with your friends'}, inplace=True)
data['keep in touch with family'] = data['keep in touch with family'].map({'Yes':1,'No':0})
data['keep in touch with your friends'] = data['keep in touch with your friends'].map({'Yes':1,'No':0})
data.rename(columns={'27. If yes, how are you keeping in touch (tick all you use)?': 'keep in touch by other mode'}, inplace=True)
data['keep in touch by other mode'] = data['keep in touch by other mode'].map({'By phone (texting, calling or video calling)':2,'By phone (texting, calling or video calling);On games consoles':2,
    'I live near them so I can see them (at a social distance);By phone (texting, calling or video calling)':1,
    'By phone (texting, calling or video calling);On social media;On games consoles':2,'By phone (texting, calling or video calling);On social media':2,
    'I live near them so I can see them (at a social distance);By phone (texting, calling or video calling);On social media;On games consoles':1,
    'I live near them so I can see them (at a social distance);By phone (texting, calling or video calling);On games consoles':1,
    'I live near them so I can see them (at a social distance);By phone (texting, calling or video calling);On social media':1,'On games consoles':3,
    'On social media':3,'I live near them so I can see them (at a social distance)':1,'I live near them so I can see them (at a social distance);On games consoles':1,
    'On social media;On games consoles':3,'I live near them so I can see them (at a social distance);On social media':1})                                                                                              

# Drop the irrevelant columns
data.drop(data.columns[[0,6,7,8,12,13,14,15,16,17,18,19,20,30,31,32,33,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55]], axis = 1, inplace = True)

# Prepare the final data with output as emmotional column
model_bhv = pd.concat([data,data4['sleeping hours'],data5,data3,mmf['behaviour_scale']],axis='columns')
model_bhv.columns = ['Are you still going to school','Any children with you','No of people with you','Age','Gender',"Yesterdays breakfast",'Did you ate fruits,veggies','No of times brushing teeth',
                     "Is it safe playing in your area",'Can you walk to park','Can you walk where you play','Do you have garden','Do you go to play outside','Do you have time to play','Where you will play',
                     'Can you play_in_all_places','Do you have place to relax','Your health','Your school','Your family','Your friends','Your appearance','Your life','keep in touch with family', 'keep in touch with your friends',
                     'keep in touch by other mode','Sleeping hours','Activities','Do you watch TV','Do you get tired','Do you finish you home work','Do you have drinks','Do you have sweets','Do you have chineese takeaway','Are you doing well your homework',
                     'Are you part of school community','Important things',"Im_good_at",'behaviour_scale']
model_bhv['behaviour_scale'] = model_bhv['behaviour_scale'].map({'expected difficulties':0,"borderline difficulties":1,"clinically significant difficulties":2})
 
# Handling Missing values:
model_bhv.isna().sum() # NaN values are found
from sklearn.impute import SimpleImputer
import numpy as np
s_imputer=SimpleImputer(missing_values=np.nan,strategy='most_frequent',verbose=0)
s_imputer=s_imputer.fit(model_bhv.iloc[:,:])
model_bhv.iloc[:,:]=s_imputer.transform(model_bhv.iloc[:,:])
model_bhv.isna().sum().sum()

# Feature Selection: Using "K-Best & Chi2" Algorithm 
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
X_bhv = model_bhv.iloc[:,:-1];Y_bhv = model_bhv.iloc[:,-1]
best_ftr = SelectKBest(score_func=chi2,k='all')
allftr_scores = best_ftr.fit(X_bhv,Y_bhv)
allftr_scores = pd.DataFrame(allftr_scores.scores_,columns=['Score'])
allftr_names = pd.DataFrame(X_bhv.columns,columns=['Features'])
bst_ftrs = pd.concat([allftr_names,allftr_scores],axis=1).sort_values(by='Score',ascending = False)
bst_ftrs
model_bhvf =model_bhv.drop(['Do you have sweets','Do you have place to relax','Gender','No of people with you','keep in touch with your friends','Do you watch TV','Did you ate fruits,veggies',
                            'Do you have time to play','keep in touch by other mode','Any children with you','Do you have chineese takeaway','Can you walk to park','Sleeping hours',
                            'Age','Can you walk where you play','keep in touch with family','Do you have garden','Where you will play','Are you still going to school'],axis=1)
top_bst_ftrs = bst_ftrs.nlargest(19,'Score')

model_bhvf.columns = ['Yesterdays_breakfast', 'No_of_times_brushing_teeth','Is_it_safe_playing_in_your_area','Do_you_go_to_playoutside',
                      'Can_you_play_in_all_places','Your_health','Your_school','Your_family','Your_friends','Your_appearance','Your_life',
                      'Activities', 'Do_you_get_tired','Do_you_finish_you_home_work','Do_you_have_drinks','Are_you_doing_well_your_homework',
                      'Are_you_part_of_school_community','Important_things','Im_good_at','behaviour_scale']
# Model Building:
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.model_selection import train_test_split
X_bhvf = model_bhvf.iloc[:,:-1];Y_bhv
x_train, x_test, y_train, y_test = train_test_split(X_bhvf, Y_bhv, test_size = 0.2,random_state=42)
model = LogisticRegression(multi_class = "ovr", solver = "newton-cg")
model.fit(x_train,y_train)
prediction_test = model.predict(x_test) 

# Evaluation on Test Data
print(confusion_matrix(y_test,prediction_test))
print(classification_report(y_test,prediction_test))

# Evaluation on Train Data
prediction_train = model.predict(x_train)
print(confusion_matrix(y_train,prediction_train))
print(classification_report(y_train,prediction_train))

# Saving the model
import pickle
pickle.dump(model,open(r'model.pkl','wb'))

# Load the model from disk
model = pickle.load(open(r'model.pkl','rb'))

# Predicting the output for the test data points
predicted_values = pd.DataFrame(model_bhvf.iloc[0:1,:-1])
output = [model.predict(predicted_values)]
output


  









































    


    
    
    
    
    
    
    

