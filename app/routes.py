from app import app
from flask import render_template, request, redirect, url_for, flash
from .forms import UserCreationForm, WorkoutsearchForm, LoginForm
from .models import User, Workout, My_Workout
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
import requests as r
import random
from config import headers
import os



@app.route('/', methods=['GET', 'POST'])
def findworkout():
    form = WorkoutsearchForm()
    workout_dict = {}
    print("above if")

    if request.method == "POST":
        print("inside post")
        url = "https://workout-planner1.p.rapidapi.com/"
        ftime= request.form.get('time')
        fmuscle= request.form.get('muscle')
        flocation= request.form.get('location')
        fequipment= request.form.get('equipment')

        querystring = {"time":f"{ftime}","muscle":f"{fmuscle}","location":f"{flocation}","equipment":f"{fequipment}"}

        headers = {
            "X-RapidAPI-Key": os.environ.get('API-KEY'),
            "X-RapidAPI-Host": "workout-planner1.p.rapidapi.com"
}

        response = r.get(url, headers=headers, params=querystring)

        print(response.json())
          
       
       
        if response.ok:
            my_dict = response.json()
            workout_dict = {}
            workout_dict["ID"] = my_dict["_id"]
            workout_dict["Workout_name"] = my_dict["key"]
            workout= Workout.query.get(workout_dict["ID"])
            if workout:
                pass
            else:
                workout = Workout(id=workout_dict["ID"], Time=ftime, Muscle=fmuscle, Location=flocation, Equipment=fequipment,key=workout_dict["Workout_name"])
                workout.saveToDB()

            workout_dict["Warm up"] = [] 
            workout_dict["Warm up"].append({"Exercise": my_dict["Warm Up"][0]["Exercise"],"Time":my_dict["Warm Up"][0]["Time"]})
            workout_dict["Warm up"].append({"Exercise": my_dict["Warm Up"][1]["Exercise"],"Time":my_dict["Warm Up"][1]["Time"]})
            workout_dict["Exercises1"] ={"Exercise":my_dict["Exercises"][0]["Exercise"], "Sets":my_dict["Exercises"][0]["Sets"],"Reps":my_dict["Exercises"][0]["Reps"]}
            workout_dict["Exercises2"] = {"Exercise":my_dict["Exercises"][1]["Exercise"], "Sets":my_dict["Exercises"][1]["Sets"],"Reps":my_dict["Exercises"][1]["Reps"]}
            workout_dict["Exercises3"] = {"Exercise":my_dict["Exercises"][2]["Exercise"], "Sets":my_dict["Exercises"][2]["Sets"],"Reps":my_dict["Exercises"][2]["Reps"]}
            workout_dict["Exercises4"] = {"Exercise":my_dict["Exercises"][3]["Exercise"], "Sets":my_dict["Exercises"][3]["Sets"],"Reps":my_dict["Exercises"][3]["Reps"]}
            workout_dict["cool-down"] = []
            ["cool-down"].append({"Exercise": my_dict["Cool Down"][0]["Exercise"],"Time":my_dict["Cool Down"][0]["Time"]})
            ["cool-down"].append({"Exercise": my_dict["Cool Down"][1]["Exercise"],"Time":my_dict["Cool Down"][1]["Time"]})
            

            print(workout_dict)

        else:
            flash("The workout you're looking for does not exist. Try again", category='warning')
            return redirect(url_for('findworkout'))

        return render_template('index.html', form = form, workout_dict = workout_dict)
    
    return render_template('index.html', form = form, workout_dict = workout_dict)
           

@app.route('/save/<workout_id>', methods=['GET', 'POST'])
@login_required
def Save_Workout(workout_id):
    workout= Workout.query.get(workout_id)
    if workout:
        my_workouts = My_Workout.query.filter_by(user_id = current_user.id).all()
        if len(my_workouts)>=15:
            flash(f"Your list is full.  To add {workout.key}, delete unused workouts.", category='warning')
        for my_workout in my_workouts:
            if my_workout.Workout_name == workout.key:
                flash(f"{my_workout.Workout_name} has already been selected.", category='warning')
    
        my_workout = My_Workout( current_user.id, workout.key)

        my_workout.saveToDB()

        flash(f"{workout.key} has been added to your list!", category='success')


    else:
        flash("The Workout you're looking for does not exist.", category='warning')
    return redirect(url_for('findworkout'))



 

@app.route('/remove/<int:workout_id>', methods=["GET", "POST"])
@login_required
def removeWorkout(workout_id):
    
    my_workout = My_Workout.query.get(workout_id)

    if current_user.id == my_workout.user_id:
        my_workout.deleteFromDB()
        flash(f"{my_workout.Workout_name} has been removed from your list.", category='warning')
        return redirect(url_for('myProgram'))

    else:
        flash("Login to update team.", category='warning')
        return redirect(url_for('myProgram'))

@app.route('/program', methods=["GET"])
@login_required
def myProgram():

    
    my_workouts = current_user.My_Workout

   

    return render_template('program.html', my_workouts = my_workouts)

@app.route('/signup', methods=["GET", "POST"])
def signUpPage():
    form = UserCreationForm()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            name = form.name.data
            email = form.email.data
            password = form.password.data

            user = User(username, name, email, password)

            user.saveToDB()

            return redirect(url_for('findworkout'))

    return render_template('signup.html', form = form)


@app.route('/login', methods=['GET', 'POST'])
def loginPage():
    form = LoginForm()

    if request.method == "POST":
        if form.validate():
            username = form.username.data
            password = form.password.data

            user = User.query.filter_by(username=username).first()
            if user: 
                if check_password_hash(user.password, password):
                    login_user(user)
                else:
                    flash('WRONG PASSWORD', category='warning')
            else:
                flash('User doesn\'t exist', category='warning')
            
        return redirect(url_for('myProgram'))


    return render_template('login.html', form = form)

@app.route('/logout', methods=["GET"])
def logOutRoute():
    form = logout_user()

    return redirect(url_for('findworkout'))



