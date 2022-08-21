from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

model = pickle.load(open(r'model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def result():
    Yesterdays_breakfast = request.form.get("Yesterdays_breakfast")
    No_of_times_brushing_teeth = request.form.get('No_of_times_brushing_teeth')
    Is_it_safe_playing_in_your_area = request.form.get('Is_it_safe_playing_in_your_area')
    Do_you_go_to_playoutside = request.form.get('Do_you_go_to_playoutside')
    Can_you_play_in_all_places = request.form.get('Can_you_play_in_all_places')
    Your_health = request.form.get('Your_health')
    Your_school = request.form.get('Your_school')
    Your_family = request.form.get('Your_family')
    Your_friends = request.form.get('Your_friends')
    Your_appearance = request.form.get('Your_appearance')
    Your_life = request.form.get("Your_life")
    Activities = request.form.get("Activities")
    Do_you_get_tired = request.form.get("Do_you_get_tired")
    Do_you_finish_you_home_work = request.form.get("Do_you_finish_you_home_work")
    Do_you_have_drinks = request.form.get("Do_you_have_drinks")
    Are_you_doing_well_your_homework = request.form.get("Are_you_doing_well_your_homework")
    Are_you_part_of_school_community = request.form.get("Are_you_part_of_school_community")
    Important_things = request.form.get("Important_things")
    Im_good_at = request.form.get("Im_good_at")

    result = model.predict([[Yesterdays_breakfast,No_of_times_brushing_teeth,Is_it_safe_playing_in_your_area,Do_you_go_to_playoutside,
                             Can_you_play_in_all_places,Your_health,Your_school,Your_family,Your_friends,Your_appearance,Your_life,
                             Activities,Do_you_get_tired,Do_you_finish_you_home_work,Do_you_have_drinks,Are_you_doing_well_your_homework,
                             Are_you_part_of_school_community,Important_things,Im_good_at]])[0]

    if result==0:
        # return 'Expected difficulties'
        return render_template('index.html',label=0)
        
    elif result==1:
        # return 'Border line difficulties'
        return render_template('index.html',label=1)
    else:
        # return 'clinically significant difficulties'
        return render_template('index.html',label=2)

if __name__=='__main__':
    app.run(debug=False)
