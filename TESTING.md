# Testing :

At various stages of the project development I have been using extensive testing of the website.Main tools used to test the website are Google Dev Tools,Firefox Dev Tools . To validate the code  I have been using W3C Markup Validator, W3C CSS Validator - PEP8 Online to ensure proper indentetion and full PEP8 compliance. During development The [Built-In Flask's Debugger](https://flask.palletsprojects.com/en/2.0.x/debugging/) was set to `True` so the code has been refactored on multiple occassions should any errors occured.

One of the major issues that occured during development stage was instaling Flask-login. Even though authentication was already implemented , I attempted to increase control of who will have access to ceatain website pages by instaling `pip3 flask-login`. Upon pushing all changes to deployed website I noticed that an app would no longer run. 
After trouboleshooting I found the error in Heroku's Latest activity dashbord, the latest build failed.
<details>

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
<br>
 <p><img src="static/docs/scrshot 2.PNG" style="min-width:80%" height="400" alt="HTML Temlpate"></p>
</details>

### Image of HTML Template:

<details>
<br>
  <p><img src="static/docs/html.scrshot.PNG" style="min-width:60%" height="600" alt="HTML Temlpate"></p>
</details>

Another bug spotted during  project review on Slack's #peer-code-review channel was brought to my attention by the Code Institute student Yigit. This was fixed by adding classes to @media query for mobile screen size devices.
> Yigit  3 days ago
Hey @Goran, nice project! Couple things caught my eye tho; Some of the images look a bit stretched on iphone XS,  and you may want to reduce the font-size for the flash messages. Good luck!

<details>
<br>
 <p><img src="static/docs/yigittest.png" style="min-width:100%" height="800" alt="Mobile screenshot"></p>
</details>

<details>
<br>
 <p><img src="static/docs/yigitIOS.png" style="min-width:100%" height="800" alt="Mobile screenshot"></p>
</details>

## Code Validation

- Results of CSS code validation:
      - Code shows no errors.Note: Warnings are due to prefixes added using Autoprefixer to ensure cross-browser compatibility.     

   <a href="static/docs/W3C CSS Validator.pdf" target="_blank" >Link to CSS Validation PDF Document</a>

- Results of HTML code validation:
      - Document checking completed. No errors or warnings to show.

     [The W3C Markup Validatior](https://validator.w3.org/nu/?doc=https%3A%2F%2Fms3-project-ci.herokuapp.com%2F)


  <a href="static/docs/Nu Html Checker.pdf" target="_blank" >Link to HTML Validation PDF Document</a>


- Results of Python PEP8 code validation:
<details>
<br>
 <p><img src="static/docs/pep8.PNG" style="min-width:100%" height="800" alt="Mobile screenshot"></p>
</details>

### Lighthouse reports of deployed website:

Lighthouse mobile report:

<details>
<br>
 <p><img src="static/docs/mobile-lighthouse.PNG" style="min-width:100%" height="800" alt="Mobile screenshot"></p>
</details>

Lighthouse desktop report:

<details>
<br>
 <p><img src="static/docs/lighthouse-desktop.PNG" style="min-width:100%" height="800" alt="Mobile screenshot"></p>
</details>

### User stories testing :

- User 1 : As a user I want to find a source of ideas of how to keep my kids entertained.
    - I registerd as a user to Growapps and was able to see a collection of diffrent activities for kids.

<details>
<br>
<p><img src="static/docs/activities.PNG" style="min-width:60%" height="400" alt="Activities"></p>
</details>

<details>
<br>
<p><img src="static/docs/activities2.PNG" style="min-width:60%" height="400" alt="Activities"></p>
</details>

- User 2 : As a user I want to share my ideas with others.
    - I logged in to Growapps and was able to share the idea of how to Color treasure hunt play with other users.


<details>
<br>
<p><img src="static/docs/add_activity.PNG" style="min-width:60%" height="400" alt="Activities"></p>
</details>

<details>
<br>
<p><img src="static/docs/add_activity2.PNG" style="min-width:60%" height="400" alt="Activities"></p>
</details>

<details>
<br>
<p><img src="static/docs/add_activity3.PNG" style="min-width:60%" height="400" alt="Activities"></p>
</details>

- User 3 : As a user I want to be able to edit my activities should I need to.
    - I logged in to Growapps and was able to edit activity I posted previously but noticed a typo.

<details>
<br>
<p><img src="static/docs/edit.PNG" style="min-width:60%" height="400" alt="Activities"></p>
</details>

<details>
<br>
<p><img src="static/docs/edit2.PNG" style="min-width:60%" height="400" alt="Activities"></p>
</details>

- User 4 : As a user I want to be able to delete activities should I need to.
- I logged in to Growapps and was able to delete activity. When I clicked remove button a modall popup appeared asked to confirm wheter or not I wanted to delete my post.
 When I clicked delete, a message appeared notifing me it was deleted.

 <details>
<br>
<p><img src="static/docs/delete.PNG" style="min-width:60%" height="400" alt="Activities"></p>
</details>

<details>
<br>
<p><img src="static/docs/delete2.PNG" style="min-width:60%" height="400" alt="Activities"></p>
</details>

<details>
<br>
<p><img src="static/docs/delete3.PNG" style="min-width:60%" height="200" alt="Activities"></p>
</details>

- User 5 : As a user I want to have convenient access to the data provided by all other members.
     - I registerd as a user to Growapps and was able to see a collection of diffrent activities for kids posted by other users.

<details>
<br>
<p><img src="static/docs/activities.PNG" style="min-width:60%" height="400" alt="Activities"></p>
</details>

- User 6 : As a user I want to be able to register as a regular user.
      - I was able to easily navigate to convinient registration page and to register as a user.

<details>
<br>
<p><img src="static/docs/register.PNG" style="min-width:60%" height="400" alt="Activities"></p>
</details> 

- User 7 : As a user I want to be able to login to my account as a registered user.
    - I was able to create a strong password and to login into Groapps securly every time after registration.

<details>
<br>
<p><img src="static/docs/login.PNG" style="min-width:60%" height="400" alt="Activities"></p>
</details>   


### Functionality testing :