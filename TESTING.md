# Testing :

At various stages of the project development I have been using extensive testing of the website.Main tools used to test the website are Google Dev Tools,Firefox Dev Tools . To validate the code  I have been using W3C Markup Validator, W3C CSS Validator - PEP8 Online to ensure proper indentetion and full PEP8 compliance. During development The [Built-In Flask's Debugger](https://flask.palletsprojects.com/en/2.0.x/debugging/) was set to `True` so the code has been refactored on multiple occassions should any errors occured.

One of the major issues that occured during development stage was instaling Flask-login. Even though authentication was already implemented , I attempted to increase control of who will have access to ceatain website pages by instaling `pip3 flask-login`. Upon pushing all changes to deployed website I noticed that an app would no longer run. 
After trouboleshooting I found the error in Heroku's Latest activity dashbord, the latest build failed.
<details>
<summary><summary>
<br>
 2021-08-15T23:02:11.021890+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=ms3-project-ci.herokuapp.com request_id=865be830-4f18-4cd8-8c9c-fbea5a995aee fwd="37.228.200.107" dyno= connect= service= status=503 bytes= protocol=https
2021-08-15T23:02:11.204746+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=ms3-project-ci.herokuapp.com request_id=d6a6ba76-421f-4bd3-855c-73499f456bfb fwd="37.228.200.107" dyno= connect= service= status=503 bytes= protocol=https
2021-08-15T23:02:14.381538+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=ms3-project-ci.herokuapp.com request_id=6cdef621-21f9-41a9-bb97-f1b020119ce6 fwd="37.228.200.107" dyno= connect= service= status=503 bytes= protocol=https
2021-08-15T23:02:14.519507+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=ms3-project-ci.herokuapp.com request_id=b66d8eb8-9feb-4ffc-bd18-fd7d1c08a1e9 fwd="37.228.200.107" dyno= connect= service= status=503 bytes= protocol=https
2021-08-15T23:07:18.182266+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=ms3-project-ci.herokuapp.com request_id=b10ae681-2474-4e58-9c5e-1370576af4b2 fwd="37.228.200.107" dyno= connect= service= status=503 bytes= protocol=https
2021-08-15T23:07:18.372198+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=ms3-project-ci.herokuapp.com request_id=8a3b89cc-25d7-43cf-861e-8cf3fe6ac0ff fwd="37.228.200.107" dyno= connect= service= status=503 bytes= protocol=https
2021-08-15T23:07:33.079336+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/home" host=ms3-project-ci.herokuapp.com request_id=8616acab-b98a-4626-8970-8b55e3f4d468 fwd="37.228.200.107" dyno= connect= service= status=503 bytes= protocol=https
2021-08-15T23:07:33.394536+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=ms3-project-ci.herokuapp.com request_id=ba1ea718-0c9d-453e-8109-389691e453b8 fwd="37.228.200.107" dyno= connect= service= status=503 bytes= protocol=https
2021-08-15T23:09:29.837859+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=ms3-project-ci.herokuapp.com request_id=8fc78017-dce9-4b94-bb4c-b584cee7be8f fwd="37.228.200.107" dyno= connect= service= status=503 bytes= protocol=https
2021-08-15T23:09:29.989406+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=ms3-project-ci.herokuapp.com request_id=4ba60ae2-5cf2-4e35-ba49-b80697cf6e4a fwd="37.228.200.107" dyno= connect= service= status=503 bytes= protocol=https
</details>

After resarching Google for error code H10 I tryed to restart all dynos. As it failed to restart I tried uninstaling flask-login as it was not used in my project, which eventualy solved the issue.
Another issue a ran into was wrongly positioned Jinja's `{% endfor %}` loop. I tried repositioning ``for`` and ``if`` statements but it would every new dataset added to the database render as it was not expected. I reached out to #backend-dev channel on Slack and assked for assisttance. The channel lead Amy pointed me in the right direction and later I found what the issue was.

### Image of rendered page:

<details>
<summary><summary>
<br>
 <p><img src="static/docs/scrshot 2.PNG" style="min-width:80%" height="400" alt="HTML Temlpate"></p>
</details>

### Image of HTML Template:

<details>
<summary><summary>
<br>
  <p><img src="static/docs/html.scrshot.PNG" style="min-width:60%" height="600" alt="HTML Temlpate"></p>
</details>