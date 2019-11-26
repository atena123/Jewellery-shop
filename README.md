[![Build Status](https://travis-ci.org/atena123/Jewellery-shop.svg?branch=master)](https://travis-ci.org/atena123/Jewellery-shop)

# Jewellery shop - website

## UX

This is full stack project. I created website called 'JEWELLERY' that allows user to purchase jewelry products.
The purpose of the website is to successfully sell Jewelry online and drive more sales for the business.
This website lets users/customers shop from anywhere at any time. Jewellery is a great fit for ecommerce as products 
are lightweight and easy to ship, come in many variations, and can be customized.

As a user you can:

* register and login to the page
* reset and change password
* search products by using search bar in the navigation bar
* search products by using categories navigation bar 
* view particular product by clicking on the 'view' link
* add to cart product by choosing quantity first
* amend product by choosing quantity first
* view products added to the cart
* purchase product by going to the checkout page, complete the form and submit the payment
* when register and logged in, view other users post by clicking on the blog in navbar
* write your own post by clicking on 'write your review here' link
* contact the shop by sending email through the contact form by clicking on the 'contact' link on the bottom of any page
* view information about the shop by clicking on any link on the bottom of any page

## WIREFRAMES

## FEATURES

### Existing features

* **register page** - allow new user to register to the website
* **login page** - allow user to login to the website to ba able to purchase products and access to the blog
* **'Jewellery logo'** - when clicked it will always bring the user to the home page
* **navbar** - created to navigate to particular page: *login*, *register*, *profile*, *Cart*, *blog* - when logged in.
  For smaller devices the navbar collapse into burger icon.
* **category navbar** - allow user to search products by categories
* **search bar** - allow user to search product by typing first letter/letters of the product
* **product** - each product contain: *image*, *description*, *price*, and *view link*
* **view link** - when clicked will bring to 'product detail' page
* **add to cart button** - allows add product to the cart by choosing quantity first
* **amend product** - allows user to amend product by choosing quantity first
* **cart page** - allow user to view products added to the cart
* **checkout button** - when clicked will bring to 'checkout page'
* **checkout page** - allows to complete the payment details form
* **submit payment button** - when clicked will submit the payment
* **contact page** - allows contact the shop by sending email by clicking on the 'contact' link at the bottom of any page
* **blog** - allows user to view other users post - when logged in, and also write its own post by clicking on the 'write your reviw here' link
* **footer links** - allows view information about the shop by clicking on: *about*, *return*, *shipping* links
* **social links** - allows user to view shop's social media (not existing yet)
* **back to top button** - when clicked will bring to the top of the page

### Features left to implement

* search product by different categories like: (price, color, for men, for women and more)
* be able to remove product from the cart
* add star rating system of each product
* add review system of each product
* add tracking order system
* create discount label for products on sales

## TECHNOLOGIES USED

* **Git** - used command line to for regular commits and to push my project to github
* **Github** - used to remotely store project code and allow public to see my website
* **Bootstrap 3.3.7** - https://getbootstrap.com/docs/3.3/ bootstrap 3.3.7 used for responsive navbar, grid layout and forms;
* **JQuery** - to assist the bootsrap
* **Bootswatch** - https://bootswatch.com/journal/ used to add theme to the website
* **Fontawesome4** - https://fontawesome.com/v4.7.0/ used to add icons to links: *register*, *login*, *profile*, *blog*, *logo*,
  and to some *contact* and *blog* headings
* **google fonts** - https://fonts.google.com/ used to add different font to the logo
* **Travis CI** - to easily sync this project & to test the code in minutes 
* **Heroku** - this application is hosted via heroku

### Frond-End Technologies

* **HTML** - to create basic structure
* **CSS** - to add styles to the websites

### Back-End Technologies

* **Django 1.11.24** - an open-source python web framework used for rapid development, maintainable, clean design, and to secure the website 
* **Python 3** - used as the backend programming language
* **Email.js** - to allow user send email and contact the shop
* **Jinja** - to display back-end data to the front-end
* **Stripe** - used for online payment processing for the business 
* **Pillow** - library to support opening, manipulating, and saving many different image file formats
* **gunicorn** - to run Python web application, required to connect to heroku
* **django-storages** - used in order to use s3
* **boto3** - allows to connect Django to s3
* **S3** - allows to store media and static files
* **Procfile** - it tells heroku what kind of app its getting

## TESTING

This website had been tested on different devices such as: Desktop, Tablet, Mobile.
I used Chrome DevTools to make sure it works on: Samsung Galaxy S5, iPhone 5/6/7/8, iPad, PC Desktop;

## DEPLOYMENT

### GITHUB

I deploy my project by going to GitHub, navigate to my github pages site's repository. Under my repository name I clicked Settings.
Then I used the Select drop-down menu to select master branch and then save it. Now my project is deployed to github pages and accessible to anyone via URL.

Link to my github repository: https://github.com/atena123/Jewellery-shop

### HEROKU

In the terminal, I created a requirements.txt file using this command: pip freeze > requirements.txt. 
In the terminal, I created a Procfile by running: echo web: python app.py > Procfile command. I push these files to my GitHub repository.
I created a new app on Heroku dashboard, I named it 'Jewellery-shop' and then I set the region. I linked Github repository to Heroku.

My app can be found at:

To run this project you need to do the following:

* Go to Github repository and click on the 'clone or download' and copy the link https://github.com/atena123/Jewellery-shop
* Create virtual environment that helps to keep dependencies required by this project separate from other projects by creating virtual environments.
* Install all required modules by creating requirements.txt file.
* Create a .env file with the connection to s3, stripe and a secret key.
* You can run this application by following command: python3 manage.py runserver $IP:$PORT

## CREDIT

### content

all products images and description are from this website: https://www.jewelrypoint.com/?gclid=EAIaIQobChMIwtnNtaSB5gIVzLTtCh14bwCUEAAYASAAEgI7BvD_BwE

### aknowlegment

1. my mentor: Ignatius Ukwuoma - my help throughout the project
1. Code Institute - using tutors support




