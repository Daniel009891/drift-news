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
<li><a href="#register">Register Page</a></li>
<li><a href="#login">Login Page</a></li>
<li><a href="#article-detail">Article detail page</a></li>
<li><a href="#comment-edit">Comment edit page</a></li>
<li><a href="#comment-delete">Comment delete page</a></li>
<li><a href="#contact-page">Contact page</a></li>
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
![admin comment list ](https://github.com/Daniel009891/drift-news/blob/main/docs/images/admin-comments-list.png?raw=true)
The admin can view a list of comments approved/awaiting approval
![admin Delete comment](https://github.com/Daniel009891/drift-news/blob/main/docs/images/admin-comments-list-delete.png?raw=true)
Delete any comment they see fit
![admin approve comment](https://github.com/Daniel009891/drift-news/blob/main/docs/images/admin-comments-approve.png?raw=true)
and also approve suitable comments.
![admin approve comment success](https://github.com/Daniel009891/drift-news/blob/main/docs/images/admin-comments-approve-success.png?raw=true)
Once a comment is approved a success message is displayed.

<h3 id="nine">As a Site Admin I can read enquiry forms sent in so that I can take on board suggestions and issues</h3>
Acceptance Criteria
Acceptance Criteria 1: I can view contact form in the admin panel and mark it as complete.

Acceptance Criteria 2: I have the relevant information needed if an email reply is necessary.

![admin contact list ](https://github.com/Daniel009891/drift-news/blob/main/docs/images/admin-contact-list.png?raw=true)
The admin user can view a list of contact requests
![admin contact form information](https://github.com/Daniel009891/drift-news/blob/main/docs/images/admin-contact-review.png?raw=true)
open them to view the individual contact enquiries to view the information
![admin contact complete](https://github.com/Daniel009891/drift-news/blob/main/docs/images/admin-contact-complete.png?raw=true)
and mark them as complete once to enquiry is satisfied.

<hr>

<h2 id="manual-testing">Manual Testing</h2>

<h3 id="navigation">Navigation Bar</h3>

* All links correctly redirect to the correct pages for visitors.
* Navbar is fully responsive on small/medium/large devices.
* User sees correct link "logout" when logged in.
* user sees correct links "register", "log in" when not logeed in.
* Navbar collapse works on smaller devices.
* contact us dropdown available for registered and non registered users.


<h3 id="footer">Footer</h3>

* All icon links work correctly.
* All links open in a new page.
* The footer appears at the end of the page using bootsrap.

<h3 id="homepage">Homepage</h3>

* All buttons work and link correctly.
* Icons are being displayed correctly, however a favicon error is displayed in dev tools.
* Images are displayed correctly.
* Good contrast between text/images/buttons.


<h3 id="register">Register page</h3>

* Username, and password are required as expected.
* Email address is optional.
* login link works and redirects existing users to log in page.
* User get redirected to the home page after successfully signing up, a success message appears to the user.
* Messages to user disappear after 2.5 seconds as expected.

<h3 id="login">Login page</h3>

* Form works as expected with username and password.
* User gets redirected to the right page after login.
* Message of login confirmation being displayed and disappear as expected.

<h3 id="article-detail">Article detail page</h3>

* Comment form works as expected, success message displayed.
* Users cannot submit an empty comment.
* Images, text and subheadings displaying as expected.
* Edit and delete buttons available to logged in users who origionally commented only.
* message displays to non logged in users informing them log in to leave a comment as expected.

<h3 id="comment-edit">Comment edit page</h3>

* Form works as expected and submits correctly.
* message displayed to user when updated.
* back to homepage button works as expected.
* user is redirected correctly when comment is updated.

<h3 id="comment-delete">Comment delete page</h3>

* all buttons work as expected.
* on delete user is redirected as expected.
* unable to get success message to show, unresolved bug.

<h3 id="contact-page">Contact page</h3>

* form validation works as expected.
* back to homepage button works as expected.
* form submits correctly and displays message to user.
* user is not redirected, this is a design choice to allow users to submit a different enquiry without having to click back to the form.

<h3 id="logout">Log out</h3>

* sign out button works as expected.
* users are directed to an are you sure page as expected.
* sing out button works fine and a message is displaying correctly.

<h3 id="adminpanel">Admin panel</h3>

* Admin can see a list of all articles.
* Admin has access to all approved and pending comments.
* Admin has access to all Users with details.
* Admin can see all contact requests.

<h3 id="authorization">Authorization</h3>

* onnly origional commenters can edit or delete their comments.
* django all auth handles signing in, out and registering of new users.
* users must sign in to comment on articles, logic prevents not authorised users from doing so.


<h3 id="responsivness">Responsivness</h3>



<h3 id="browser-testing">Browser Testing</h3>

Chrome dev tools were used throughout the development of the project to test responsiveness. Responsiveness was tested using Dev Tools to emulate the following devices.

* Iphone 5
* Iphone 6/7/8
* Iphone 6/7/8 Plus
* Iphone X
* Ipad
* Ipad Pro


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
