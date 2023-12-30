[Back to README]()

---

## Testing Catalouge

<li><a href="#user-stories">User Stories Testing</a></li>
<ul>

<li><a href="#admin-testing">Admin Stories Testing</a></li>
</ul>
<li><a href="#manual-testing">Manual Testing</a></li>
<ul>
<li><a href="#navigation-bar">Navigation Bar</a></li>
<li><a href="#footer">Footer</a></li>
<li><a href="#homepage">Homepage</a></li>
<li><a href="#signup">Signup Page</a></li>
<li><a href="#login">Login Page</a></li>

<li><a href="#logout">Log out</a></li>
<li><a href="#adminpanel">Admin panel</a></li>
<li><a href="#authorization">Authorization</a></li>
<li><a href="#responsivness">Responsivness</a></li>
<li><a href="#browser-testing">Browser Testing</a></li>
</ul>
<li><a href="#validation">Validation</a></li>
<ul>
<li><a href="#validation">W3C HTML Validator</a></li>
<li><a href="#validation">W3C CSS Validator</a></li>
<li><a href="#validation">JSHint Javascript Validator</a></li>
<li><a href="#validation">PEP8 Python Validator</a></li>
</ul>
<li><a href="#lighthouse">Lighthouse Testing</a></li>
<li><a href="#bugs">Bugs</a></li>
<ul>
<li><a href="#solved-bugs">Solved Bugs</a></li>
</ul>

---

<h2 id="user-stories">User Stories Testing</h2>

<h3 id="site-user-stories">Site User Stories Testing</h3>
<ul>
<li><a href="#one">As a Site User I can comment on news articles I find interesting so that I can interact with like minded users</a></li>
<li><a href="#two">As a Site User I can view a list of articles so that I can select one to read</a></li>
<li><a href="#three">As a Site User I can click on an article so that I can read the full text</a></li>
<li><a href="#five">As a Site User I can register an account so that I can comment on articles</a></li>
<li><a href="#eight">As a Site User I can fill out an enquiry form so that I can find out more about upcoming events.</a></li>
</ul>

<h3 id="#admin-testing">Admin Testing</h3>
<ul>
<li><a href="#six">As a Site Admin I can create, read, update and delete articles so that I can manage my news content</a></li>
<li><a href="#seven">As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments</a></li>
<li><a href="#nine">As a Site Admin I can read enquiry forms sent in so that I can take on board suggestions and issues</a></li>

</ul>


## User Stories Testing
<h3 id="one">As a Site User I can comment on news articles I find interesting so that I can interact with like minded users</h3>
Acceptance Criteria 1: I can leave a comment on the article and see it displayed once approved.

Acceptance Criteria 2: I can edit or delete the comment if I choose to.

![comments](https://github.com/Daniel009891/drift-news/blob/main/docs/images/comments.png?raw=true)
Once logged in users can leave a comment on the articles they wish. Once approved these comments will be available to edit or delete, but only by the origional commenter.

<h3 id="two">As a Site User I can view a list of articles so that I can select one to read</h3>
Acceptance Criteria 1: I can see a list of articles on the main page.
Acceptance Criteria 2: I can click on the articles to find out more.

![article list](https://github.com/Daniel009891/drift-news/blob/main/docs/images/article-list.png?raw=true)
Users can scroll the homepage to see the list of articles, there is a read more button to view the entire article.

As a Site User I can click on an article so that I can read the full text

<h3 id="three">As a Site User I can click on an article so that I can read the full text</h3>
Acceptance Criteria 1: I can click a button to read read the full article.

Acceptance Criteria 2: I can easily read the information that i am interested in.

![article detail top](https://github.com/Daniel009891/drift-news/blob/main/docs/images/article-detail-top.png?raw=true)
![article detail top](https://github.com/Daniel009891/drift-news/blob/main/docs/images/article-detail-bottom.png?raw=true)
Once the user has clicked read more, they will be redirected to the article detail page where they can read the full article.

<h3 id="five">As a Site User I can register an account so that I can comment on articles</h3>
Acceptance Criteria 1: I can choose my own username.

Acceptance Criteria 2: I can fill in the details of my company as company name and vat number.

![signup](https://github.com/Daniel009891/drift-news/blob/main/docs/images/sign-up.png)
On the signup page, the user can sign up and add their own unique email , user name and password.

<h3 id="eight">As a Site User I can fill out an enquiry form so that I can find out more about upcoming events.</h3>
Acceptance Criteria 1:  I can fill out the form with my enquiry.

Acceptance Criteria 2: I can submit my enquiry to the admins and have confirmation it has been sent.

![contact nav](https://github.com/Daniel009891/drift-news/blob/main/docs/images/contact-nav.png?raw=true)
![contact nav dropdown](https://github.com/Daniel009891/drift-news/blob/main/docs/images/contact-nav-dropdown.png?raw=true)
The user can click the dropdown menu on the navbar to allow them to find the contact form.
![contact form](https://github.com/Daniel009891/drift-news/blob/main/docs/images/contact-form.png?raw=true)
![contact form message](https://github.com/Daniel009891/drift-news/blob/main/docs/images/contact-form-message.png?raw=true)
The user will be greeted with a form that is required to be complete before allowing them to submit. Once the form is submitted a message is displayed to the user.

<h2 id="admin-testing">Admin Stories Testing</h2>

<h3 id="six">As a Site Admin I can create, read, update and delete articles so that I can manage my news content</h3>
Acceptance Criteria 1: I can easily create articles with a form in the admin panel.

Acceptance Criteria 2: I can update or delete the articles through the admin panel.

![admin create](https://github.com/Daniel009891/drift-news/blob/main/docs/images/admin-create.png?raw=true)
Admins will have the ability to update the articles
![admin Delete](https://github.com/Daniel009891/drift-news/blob/main/docs/images/admin-delete.png?raw=true)
delete the articles
![admin list](https://github.com/Daniel009891/drift-news/blob/main/docs/images/admin-list.png?raw=true)
view a list of articles awaiting publishing or published
![admin update](https://github.com/Daniel009891/drift-news/blob/main/docs/images/admin-update.png?raw=true)
and update existing articles. All through the built in django admin panel.

<h3 id="seven">As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments</h3>
Acceptance Criteria
Acceptance Criteria 1: I can view all comments awaiting approval.

Acceptance Criteria 2: I can approve comments if suitable or deny comments if they are not.
![admin create]()
Admins will have the ability to update the articles
![admin Delete]()
delete the articles
![admin list]()
view a list of articles awaiting publishing or published
![admin update]()

<h3 id="ten">





---

<h2 id="manual-testing">Manual Testing</h2>

<h3 id="navigation">Navigation Bar</h3>



<h3 id="footer">Footer</h3>



<h3 id="homepage">Homepage</h3>



<h3 id="signup">Signup page</h3>



<h3 id="login">Login page</h3>



<h3 id="new-request">New Request Customer</h3>



<h3 id="request-overview">Request Overview</h3>



<h3 id="edit-request-customer">Edit Request Customer</h3>




<h3 id="logout">Log out</h3>

.

<h3 id="adminpanel">Admin panel</h3>



<h3 id="authorization">Authorization</h3>



<h3 id="responsivness">Responsivness</h3>



<h3 id="browser-testing">Browser Testing</h3>



---

<h2 id="validation">Validation</h2>

### [W3C HTML Validator](https://validator.w3.org/)



### [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)



### [JSHint Javascript Validator](https://jshint.com/)



### PEP8 Python Validator



<h3 id="lighthouse">Lighthouse Testing</h3>

#### On desktop for homepage

![lighthouse1]()

#### On mobile for homepage

![lighthouse1]()

---

<h2 id="bugs">Bugs</h2>



<h3 id="solved-bugs">Solved Bugs</h3>


---
