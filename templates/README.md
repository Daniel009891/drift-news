# Portfolio Project 4 - Full-Stack Toolkit

## Drift News - Keep up to date with everything drifting

The go to site for all things drifting.

![Image mockup of the website in a computer, tablet and phone](https://github.com/Daniel009891/drift-news/blob/main/docs/images/mockup.png?raw=true)

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
<li><a href="#new-comment">New Request</a></li>
<li><a href="#edit-comment">Edit Request</a></li>
<li><a href="#delete-comment">Delete Request</a></li>
</ul>
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

### Front Page

![frontpage](https://github.com/Daniel009891/drift-news/blob/main/docs/images/wireframe-landing.png?raw=true)

### Detail Page

![Detail](https://github.com/Daniel009891/drift-news/blob/main/docs/images/wireframe-detail.png?raw=true)

### Contact Page

![contact](https://github.com/Daniel009891/drift-news/blob/main/docs/images/wireframe-contact.png?raw=true)

---

<h2 id="user-stories">User Stories</h2>

* As a Site User I can comment on news articles I find interesting so that I can interact with like minded users
* As a Site User I can view a list of articles so that I can select one to read
* As a Site User I can click on an article so that I can read the full text
* As a Site User I can register an account so that I can comment on articles
* As a Site Admin I can create, read, update and delete articles so that I can manage my news content
* As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments
* As a Site User I can fill out an enquiry form so that I can find out more about upcoming events.
* As a Site Admin I can read enquiry forms sent in so that I can take on board suggestions and issues

<h2 id="surface-plan">The Surface Plane</h2>

<h3 id="base">Base</h3>

To make the application as dynamic as possible, i want the navbar and footer to be the same in all of the application. Therefore, Django dynamic pages are used so the user always recognizes the default layout they're on.

Navbar
![navbar](https://github.com/Daniel009891/drift-news/blob/main/docs/images/nav-bar.png?raw=true)

Footer
![footer](https://github.com/Daniel009891/drift-news/blob/main/docs/images/footer.png?raw=true)

<h3 id="homepage">Homepage</h3>

A big goal is to highlight the advantages as early as possible so the user gets sold on why they should register and use our application.


![jumbatron](https://github.com/Daniel009891/drift-news/blob/main/docs/images/front-page-jumbatron.png?raw=true)

Articles are displayed in an ordered fashion with big images to catch the users attention.

![articles](https://github.com/Daniel009891/drift-news/blob/main/docs/images/article-list.png?raw=true)


<h3 id="signup">Signup</h3>

The user is can sign up for an account using this page to allow them to comment on articles

![signup](https://github.com/Daniel009891/drift-news/blob/main/docs/images/sign-up.png?raw=true)

<h3 id="login">Login</h3>

Its easy to login for returning user. Just fill in your username and password and you get logged in.

![login](https://github.com/Daniel009891/drift-news/blob/main/docs/images/login.png?raw=true)

<h3 id="new-comment">New Comment</h3>

users can leave comments on articles after registering. it is rendered in a conversation style in descending order.

![new-comment](https://github.com/Daniel009891/drift-news/blob/main/docs/images/comments.png?raw=true)

<h3 id="edit-comment">Edit Comment</h3>

users also have the option to edit comments, through authentication they can only edit comments made by them.

![edit-comment](https://github.com/Daniel009891/drift-news/blob/main/docs/images/edit-comment.png?raw=true)

<h3 id="delete-comment">Delete Comment</h3>

Users can delete comments, but again this is done by authorisation.

![delete-comment](https://github.com/Daniel009891/drift-news/blob/main/docs/images/delete-comment.png?raw=true)

---


### Key Models

### Article

* The comments are related to the article model, this model is used for creating article on the page. It takes several primary keys for it to be able to supply data to the database.
  

### Comment

* The Comment model is related to the Article model and allows the slug from the article to be used as a primary key to enable comments to be set to the correct article.
* user id and date time now fields are displayed along with the comment body.

### Contact

* The contact model takes data from the registered/non registered user and is linked to the comment form, in turn this posts the data to the database.

---

<h2 id="testing">Testing</h2>
Link to the testing document.

[TESTING.md](https://github.com/Daniel009891/drift-news/blob/main/templates/TESTING.md)

---

## **Deployment**

The master branch of this repository is the most current version and has been used for the deployed version of the site.

The Code Institiue student template was used to create this project.

[Code Institute Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)

* Click the *Use This Template* button.
* Give your repository a name, and description if you wish.
* Click the *Create Repository from Template* to create your repository.
* Click the *Gitpod* button to create a gitpod workspace, this can take a few minutes.
* When working on project using Gitpod, please open the workspace from Gitpod, this will open your previous workspace rather than creating a new one.
Use the following commands to commit your work,
* `git add .` - adds all modified files to a staging area.
* `git commit -m "A short message exlaining your commit"` - commits all changes to a local repository.
* `git push` - pushes all your commited changes to your Github repository.

**Requirements**

* [Python 3](https://www.python.org/downloads/)
* [Pip](https://pypi.org/project/pip/)
* [Git](https://git-scm.com/)
* [AWS S3](https://aws.amazon.com/)

**Creating a Clone**

1. From the repository, click *Code*
2. In the *Clone >> HTTPS* section, copy the clone URL for the repository
3. In your local IDE open Git Bash
4. Change the current working directory to the location where you want the cloned directory to be made
5. Type `git clone`, and then paste the URL you copied in Step 2 - ``git clone https://github.com/Harry-Leepz/Nourish-and-Lift.git``
6. Set the following values in a `env.py` file.

```
import os

os.environ.setdefault("SECRET_KEY", "<app secret key of your choice>")
os.environ.setdefault("DEVELOPMENT", "True")
os.environ.setdefault('STRIPE_PUBLIC_KEY', '<key generated by Stripe>')
os.environ.setdefault('STRIPE_SECRET_KEY', '<key generated by Stripe>')
os.environ.setdefault('STRIPE_WH_SECRET', '<key generated by Stripe>')
```

* Stripe keys are generated by Stripe, each individual have their own unique key values.
* *PLEASE MAKE SURE NEVER TO PUBLISH THESE KEYS, ADD THE `env.py` TO A `.gitignore` TO AVOID PUSHING KEYS TO GITHUB.*

7. Install the project requirements - `pip3 install requirements.txt`
8. Apply database migrations - `python manage.py migrate`
9. Create a superuser - `python manage.py createsuperuser`
10. The project can be run with the following - `python manage.py runserver`

**Heroku Deployment**

1. Log into Heroku
2. Create a new app, choose a location closest to you
3. Search for Heroku Postgres from the resources tab and add to your project
4. Make sure to have `dj_database_url` and `psycopg2` installed.

```
pip3 install dj_database_url
pip3 install psycopg2
```

5. Login to the Heroku CLI - `heroku login -i`
6. Run migrations on Heroku Postgres - `heroku run python manage.py migrate`
7. Create a superuser - `python manage.py createsuperuser`
8. Install `gunicorn` - `pip3 install gunicorn`
9. Create a requirements.txt file - `pip3 freeze > requirements.txt`
10. Create a `Procfile` (note the capital P), and add the following,

```
web: gunicorn moose_juice.wsgi:application
```

11. Disable Heroku from collecting static files - `heroku config:set DISABLE_COLLECTSTATIC=1 --app <your-app-name>`
12. Add the hostname to project settings.py file

```
ALLOWED_HOSTS = ['<you-app-name>.herokuapp.com', 'localhost']

```

13. Connect Heroku to you Github, by selecting Github as the deployment method and search for the github repository and pressing `connect`
14. In Heroku, within settings, under config vars select `Reveal config vars`
15. Add the following,

```
AWS_ACCESS_KEY_ID =	<your variable here>
AWS_SECRET_ACCESS_KEY =	<your variable here>
DATABASE_URL =	<added by Heroku when Postgres installed>
DISABLE_COLLECTSTATIC =	1 
EMAIL_HOST_PASS = <your variable here>
EMAIL_HOST_USER = <your variable here>
SECRET_KEY = <your variable here>
STRIPE_PUBLIC_KEY = <your variable here>
STRIPE_SECRET_KEY = <your variable here>
STRIPE_WH_SECRET = <different from env.py>
USE_AWS = True
```

16. Go back to the Deploy tab and under Automatic deploys choose `Enable Automatic Deploys`
17. Back in your CLI add, commit and push your changes and Heroku will automatically deploy your app

```
git add .
git commit -m "Initial commit"
git push
```

18. Your deployed site can be launched by clicking `Open App` from its page within Heroku.

**AWS S3 Bucket setup**

1. Create an Amazon AWS account
2. Search for S3 and create a new bucket
    * Allow public access
3. Under Properties > Static website hosting
    * Enable
    * index.html as index.html
    * save
4. Under Permissions > CORS use the following:

```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```

5. Under Permissions > Bucket Policy:
    * Generate Bucket Policy and take note of Bucket ARN
    * Chose S3 Bucket Policy as Type of Policy
    * For Principal, enter *
    * Enter ARN noted above
    * Add Statement
    * Generate Policy
    * Copy Policy JSON Document
    * Paste policy into Edit Bucket policy on the previous tab
    * Save changes
6. Under Access Control List (ACL):
    * For Everyone (public access), tick List
    * Accept that everyone in the world may access the Bucket
    * Save changes

**AWS IAM (Identity and Access Management) setup**

1. From the IAM dashboard within AWS, select User Groups:
    * Create a new group
    * Click through and Create Group
2. Select Policies:
    * Create policy
    * Under JSON tab, click Import managed policy
    * Choose AmazongS3FullAccess
    * Edit the resource to include the Bucket ARN noted earlier when creating the Bucket Policy
    * Click next step and go to Review policy
    * Give the policy a name and description of your choice
    * Create policy
3. Go back to User Groups and choose the group created earlier
    * Under Permissions > Add permissions, choose Attach Policies and select the one just created
    * Add permissions
4. Under Users:
    * Choose a user name
    * Select Programmatic access as the Access type
    * Click Next
    * Add the user to the Group just created
    * Click Next and Create User
5. Download the `.csv` containing the access key and secret access key.
    * **THE `.csv` FILE IS ONLY AVAILABLE ONCE AND CANNOT BE DOWNLOADED AGAIN.**

**Connecting Heroku to AWS S3**

1. Install boto3 and django-storages

```
pip3 install boto3
pip3 install django-storages
pip3 freeze > requirements.txt
```

2. Add the values from the `.csv` you downloaded to your Heroku Config Vars under Settings:
3. Delete the `DISABLE_COLLECTSTATIC` variable from your Cvars and deploy your Heroku app
4. With your S3 bucket now set up, you can create a new folder called media (at the same level as the newly added static folder) and upload any required media files to it.
    * **PLEASE MAKE SURE `media` AND `static` FILES ARE PUBLICLY ACCESSIBLE UNDER PERMISSIONS**

---

## **Credits**

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
* [Github](https://codeanywhere.com/)
* [codeanywhere](https://www.gitpod.io/)
* [Pexels](https://www.pexels.com)


---

<h2 id="credits">Credits</h2>

#### Code

* To help me get started with the project and understand the basics, i followed [Code Institute](https://codeinstitute.net/se/) and Matt´s Walktrough on "I Think therefore i Blog", big thanks for getting me started.

* Sean Tutor at [Code Institute](https://codeinstitute.net/se/) helped me solve some bugs in my code, big thanks.

#### Bootstrap

* Bootstrap has an amazing library and has helped me focus on the backend and save a lot of time with style, and layout on the frontend.

#### Django

* The generic views from [Django](https://www.djangoproject.com/) made my life much easier, also great documentation.

#### Issues with code

Most of the daily problems were solved thanks to [Stackoverflow](https://stackoverflow.com/)  [W3Schools](https://www.w3schools.com/) and ![slack](https://slack.com/intl/en-gb).

<h2 id="acknowledgements">Acknowledgements</h2>

This website was completed as a Portfolio Project 4 for the Fullstack Diploma at [Code Institute](https://codeinstitute.net/se/). I want to thank my mentor **Harry** for helping me through this tough project.

The project is for educational purposes only and not for public consumption.


