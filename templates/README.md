# Portfolio Project 4 - Full-Stack Toolkit

## Drift News - Keep up to date with everything drifting

The go to site for all things drifting.

![Image mockup of the website in a computer, tablet and phone]()

## Live Site

[Go to application](https://walltap-229162c12b90.herokuapp.com/)

## Repository

[View repository](https://github.com/Daniel009891/drift-news)

---

## Catalouge

<li><a href="#target-group">Target Group</a></li>
<li><a href="#user-experince">UXD - User Experince Design</a></li>
<ul><li><a href="#storytelling">Storytelling</a></li>
<li><a href="#wireframe">Wireframe</a></li>
<li><a href="#flowchart">Flowchart</a></li>
</ul>
<li><a href="#user-stories">User Stories</a></li>
<li><a href="#surface-plan">The Surface Plan</a></li>
<ul>
<li><a href="#base">Base</a></li>
<li><a href="#homepage">Homepage</a></li>
<li><a href="#signup">Signup</a></li>
<li><a href="#login">Login</a></li>
<li><a href="#customer-overview">Customer Overview</a></li>
<li><a href="#new-request">New Request</a></li>
<li><a href="#edit-request">Edit Request</a></li>
<li><a href="#delete-request">Delete Request</a></li>
<li><a href="#send-candidates">Send Candidates</a></ul>
<li><a href="#see-candidates">See Candidates</a></li>
<li><a href="#partner-overview">Partner Overview</a></li>
</ul>
<li><a href="#database-design">Database Design</a></ul>
<li><a href="#testing">Testing</a></li>
<li><a href="#deployment">Deployment</a></li>
<li><a href="#technologies-used">Technologies</a></li>
<li><a href="#credits">Credits</a></li>
<li><a href="#acknowledgements">Acknowledgements</a></li></ul>

---

<h2 id="target-group">Target Group</h2>

Drift news targets anyone interested in the sport or motorsports in general, it is a good source of information for the community.


---

<h2 id="user-experince">UXD - User Experince Design</h2>

<h3 id="wireframe">Wireframes</h3>

![frontpage]()
![frontpage#2]()

![register account]()
![login](

### User loged in

![user overview]()
![user request details]()
![user presented candidates]()

### Partner loged in

![partner overview]()
![partner request details]()


---

<h2 id="user-stories">User Stories</h2>



---

<h2 id="surface-plan">The Surface Plane</h2>

<h3 id="base">Base</h3>


Navbar
![navbar]()

Footer
![footer]()

<h3 id="homepage">Homepage</h3>


![hero]()



![mockup and cta]()



![partner cta]()



![step-by-step]()



![quote]()



<h3 id="signup">Signup</h3>


![signup]()

<h3 id="login">Login</h3>
Its easy to login for returning user. Just fill in your username and password and you get logged in.

![login]()



<h3 id="new-request"></h3>


![new-request]()

<h3 id="edit-request">Edit Request</h3>


![buttons]()

![edit-request]()

<h3 id="delete-request">Delete Request</h3>


![buttons]()

![delete-request]()

---

<h2 id="database-design">Database Design</h2>
On this project postgresql is used with ElephantSQL

[Database Diagram](https://res.cloudinary.com/dpliee0fu/image/upload/v1669761371/Database_Planning_gzhnzg.pdf)

### Key Models

### User

* The user profile is connected to the User model created by Allauth on registration.
* The model is extended with AbstractUser to be able to save different user types with different permissions.
* Primary Key is the id which is genereated automatically when a user is created.

### Order

* The order model is related to the user model to see who is responsible for the order.
* If the user is deleted, the order also gets deleted so no orders are active for users that don´t exist.

### Candidate

* Candidates are related to their managers (Users) who "create" the candidate.
* Candidates are also related to the order in which managers present the candidate and link them together.
* Being linked to the order, the user can also get access to the Candidate information via the template.

---

<h2 id="testing">Testing</h2>
Link to the testing document.

[TESTING.md]()

---

<h2 id="deployment">Deployment</h2>

The Code Institute student template was used to create this project.

[Code Institute Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)

* Click the "Use This Template" button.
* Give your repository a name, and description if you wish.
* Click the Create Repository from Template to create your repository.
* Click the Gitpod button to create a gitpod workspace, this can take a few minutes.
* When working on project using Gitpod, please open the workspace from Gitpod, this will open your previous workspace rather than creating a new one.
* Use the following commands to commit your work,
git add . - adds all modified files to a staging area.

git commit -m "A short message exlaining your commit" - commits all changes to a local repository.

git push - pushes all your commited changes to your Github repository.

* Before making the first commit:
PLEASE MAKE SURE NEVER TO PUBLISH SECRET KEYS, ADD THE env.py TO A .gitignore TO AVOID PUSHING KEYS TO GITHUB.

### Heroku Deployment

1. Log into Heroku
2. Create a new app, choose a location closest to you
3. Search for Heroku Postgres from the resources tab and add to your project
4. Make sure to have dj_database_url and psycopg2 installed.

pip3 install dj_database_url
pip3 install psycopg2

5. Login to the Heroku CLI - heroku login -i
6. Run migrations on Heroku Postgres - heroku run python manage.py migrate
7. Create a superuser - python manage.py createsuperuser
8. Install gunicorn - pip3 install gunicorn
9. Create a requirements.txt file - pip3 freeze > requirements.txt
10. Create a Procfile (note the capital P), and add the following,

web: gunicorn jobin.wsgi

11. Disable Heroku from collecting static files

heroku config:set DISABLE_COLLECTSTATIC=1 --app jobin-compare-consultants

12. Add the hostname to project settings.py file

ALLOWED_HOSTS = ['jobin-compare-consultants.herokuapp.com', 'localhost']

13. Connect Heroku to you Github, by selecting Github as the deployment method and search for the github repository and pressing

connect

14. In Heroku, within settings, under config vars select

Reveal config vars

15. Add the following

DATABASE_URL = URL to the database
CLOUDINARY_URL = URL to cloudinary
SECRET_KEY = The secret key

16. Commit and push in your CLI

git add .
git commit -m "Initial commit"
git push

17. Go back to the Deploy tab and press

Deploy Branch

18. Your deployed site can be launched by clicking Open App from its page within Heroku.

*During production Heroku Postgresql was no longer availible and therefore DATABASE_URL in Heroku Config Vars was changed to the ElephantSQL Postgres url.*

---

<h2 id="technologies-used">Technologies Used</h2>

* [HTML](https://sv.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/CSS)
* [Javascript](https://www.javascript.com/)
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [ElephantSQL](https://www.elephantsql.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Heroku](https://id.heroku.com/login)
* [Cloudinary](https://cloudinary.com/)
* [Github](https://github.com/)
* [Gitpod](https://www.gitpod.io/)
* [Balsamiq](https://balsamiq.com/)
* [SimpleImageResizer](https://www.simpleimageresizer.com/)
* [Pagespeed](https://pagespeed.web.dev/)
* [Miniwebtool](https://miniwebtool.com/django-secret-key-generator/)
* [Techsini](https://techsini.com/multi-mockup/index.php)
* [Pexels](https://www.pexels.com)
* [Writer](https://writer.com/grammar-checker/)

---

<h2 id="credits">Credits</h2>

#### Code

* To help me get started with the project and understand the basics, i followed [Code Institute](https://codeinstitute.net/se/) and Matt´s Walktrough on "I Think therefore i Blog", big thanks for getting me started.

* Ed, Ger and Oisin, Tutors at [Code Institute](https://codeinstitute.net/se/) helped me solve some bugs in my code, big thanks.

#### Bootstrap

* Bootstrap has an amazing library and has helped me focus on the backend and save a lot of time with style, and layout on the frontend.

#### Django

* The generic views from [Django](https://www.djangoproject.com/) made my life much easier, also great documentation.

#### Issues with code

Most of the daily problems were solved thanks to [Stackoverflow](https://stackoverflow.com/) and [W3Schools](https://www.w3schools.com/).

<h2 id="acknowledgements">Acknowledgements</h2>

This website was completed as a Portfolio Project 4 for the Fullstack Diploma at [Code Institute](https://codeinstitute.net/se/). I want to thank my friend **Manne** for helping me understand some javascript functions.

The project is for educational purposes only and not for public consumption.

William Tynér, November 2022.
[LinkedIn](https://www.linkedin.com/in/williamtyner/)
