# Dice rolling web interface

<b>Python 3.x</b> is used for implementation of dice rolling programe<br />
Packages: <b>Django</b>

In order to run program sucessfully, firstly create a separated env, for example:<br />
<b>conda create -n dice_roller python=3.6</b> <br />
Then activate created environment:</br>
<b>conda activate dice_roller</b></br>
Then install all needed modules using:<br />
<b>pip install -r requirements.txt</b>

Running program from command line:<br />
CD yourself to the root directory of this repo and run the folowing command to startup the Django server:<br />
<b>python manage.py runserver 0.0.0.0:8000</b><br/>
Then visit this url: http://localhost:8000/ and enjoy playing!</br>

This repo is equipped with unittests as well. Just navigate to the dice folder and run the following command:</br>
<b>python -m unittest test_helper_functions</b>
