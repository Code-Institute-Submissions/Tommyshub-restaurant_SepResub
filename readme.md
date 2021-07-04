# The Greenhouse

### User stories

As a customer of the resturant i want,

- to order food to be delivered to my door.

- to be able to create an account.

- to be able to store my default delivery information.

- to be able to change my default delivery information.

- be able to view information about the food.

- be able to contact the resturant to ask about my order.

As a resturant owner I want,

- to have a menu where my customers can view and order food.

- my customers to be able to create a account.

- to be able to view my customers contact information.

- my customers to be able to update their default delivery information.

- my customers to be able to give tips to the delivery people.

- customers to be able to contant us.

- my customers to be able to view their past order.

- my customers to have a good checkout experience.

- the website to look professional so that my customers feel save ordering from us.

## Requirements and Expectations

- The home view should be rendered directly when a customer enters the webpage, it would be very embarrassing if I somehow used the base template for this.

- The responsiveness of the website needs to be good.

- The website needs to be secure and look professional so that the customers feel comfortable using their credit cards on it.

- Navigation should be easy to understand.

- Users should get feedback from their actions, for example by a toast message.

- It should be easy to create accounts, for example by using google to signup.

- It should be easy for the users to retrieve lost passwords.

- It should be easy to contact the site owner in case of problems with orders.

## Design

### Wireframes

I used figma to create the wireframes but sadly my computer broke and I lost the original files so the ones included today has been created after the project was done. I did try to create them similar to how I made them from the start but I added things that I knew was there in the finished project, for example the logo.

[Mobile Wireframe](https://github.com/Tommyshub/restaurant/blob/main/static/wireframes/thegreenhouse-mobile-wireframe.fig.fig)

[Desktop Wireframe](https://github.com/Tommyshub/restaurant/blob/main/static/wireframes/thegreenhouse-desktop-wireframe.fig)

### Choice of project and design

I decided to create a project that I thought was a bit easier to create and I took something that was a bit similar to the Boutique Ado project.
I did this because I knew I would not have too much time to create this and I wanted to make sure I had time enought to finish what I started.

I did not like how the navbar from the materialize css framework looks or functions so I decided to create one from scratch, I think it worked out pretty well but it did take longer then I originally expected.

I also decided to keep the rest of the design fairly simple because I often question my taste and spend a lot of time obsessing over small things.

I think that the it worked out prettty well with the gray navbar and a white background but with a little bit of color added in terms of the logo and buttons.

## Languages

- [HTML](https://en.wikipedia.org/wiki/HTML)

- [CSS](https://en.wikipedia.org/wiki/CSS)

- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>)

## Tools & frameworks

- [Django](<https://en.wikipedia.org/wiki/Django_(web_framework)>)

- [Materialize CSS](https://materializecss.com/)

- [Git](https://git-scm.com/)

- [Google Fonts](https://fonts.google.com/)

## Testing

### Bandit -a tool designed to find common security issues in Python code.

[You can find out more about bandit here](https://github.com/PyCQA/bandit)

I used this automated tool to check if there were any security issues in my code. It scanned 1491 lines of code and found no security issues.

### Django Testing

I tested some of my code with the built-in django testing framework. I focused on the checkout app when I wrote my tests but I intend to add more in the future.

- I tested the forms by making sure that the form cannot be submitted without the required fields.

- I tested so that the urls resolves as expected.

### Migrating to PostgreSQL from Sqlite3

This part was a real headache for me and I spent more than a week trying to figure out what was wrong, even asking people for help without avail.

I tried everyting I could think of and at the end it was something really simple that I feel I should have figured out sooner.

PostgreSQL did not understand my query when I wrote in lowercase letters and Sqlite3 did, so all I needed to do to fix this was to change how I query the databse.

### Forms

- Default delivery information form

The first form I tested was the change default delivery information form, and I realized that this form can be submitted when it is empty and therefore set the default delivery information to an empty string.

I fixed this by setting blank to false on all fields except the street address 2 field.

I also checked that everything was updated as expected when submitting a valid form by going to the checkout form and looking at the delivery information.

I also had an issue with the form not being prefilled and it warned about missing fields without any actions. To fix this I looked at my view and noticed that I was requsting post where I should not so I removed that.

- Contact form

First thing I checked was to submit a blank form and that does not work.

I tried to submit the form without a valid email address and this did not work either.

I also tried to submit a valid form and I checked my email adress to confirm that I the received the email and that it was formatted as expected.

- Bag forms

The first thing I tested here was to update and remove items and that worked as expected.

One problem I noticed is that the input field for the form for giving tips does not show until the button is pressed and it warns that the form needs to be filled out. I have no idea how to fix this and I cannot find any information about it online so that is something I intend to ask my mentor about before submitting this project.

- Register and login forms

I manually tested these forms and both of them works as expected and it is not possible to submit forms without the right information.

- Register with social account

It is possible to register on the website with a google social account and this also works as expected.

- Forgot password

I tried to reset my password and I got a link sent to my email adress where I could reset my password.

### Coupon codes

I checked so that it's not possible to enter invalid codes and I checked so that it's not possible to enter the same code twice.

### Buttons and links

I manually looked at every button and link on the page and I could not find any the did not work as expected.

The keep shopping and secure checkout buttons in the shopping bag had the old teal color so I changed these to light green so they match the rest of the page.

### Developer console

While looking in the console I visited every page in my app and I clicked all the buttons.

One issue I noticed was a warning about missing favicon, I solved this by making a copy of my vegan logo and using that as a favicon and linking to it in the base template.

It still warnes me about the favicon when I look at past orders and go back to the accounts page and I have no idea why or how to fix this. I assume this is a bug and I think it should be fine as it is.

I found no other warnings.

### Responsiveness

- Navbar

One problem with my navbar is that the popout menu is not perfectly aligned in height on some screen sizes. I solved this by setting media queries for the height and changing the viewport settings in my css.

The navbar also starts to look a bit funky on sizes under 300pixels width but after doing some research I decided that it is not necessary to support screen sizes below 300 pixels in width so I left this as it is.

- Menu

I found no real issues with the responsiveness here but I did not like how the category names looked at smaller screen sizes and it also looked a bit wierd when the categories had icons.

I fixed this by changing the headings to small text and put it under the icons instead.

- Contact

No issues.

- Account

No issue.

- Bag

In the bag I found that the keep shopping and secure checkout buttons where too close on small screen sizes and I fixed this by adding a class with margin-top on both of them. I needed to do that on both so that the height of the buttons matched on large screen sizes.

- Checkout

I had the same issues as in the bag but with the complete order and adjust bag buttons, and I fixed them in the same way.

## Formatting and Validation

### Prettier

I used the prettier extension for vscode to format the html, this worked great but one issue I had was that it did not format the jinja code. I googled how to best solve this and I could chose between either adding a comment saying prettier ignore to make the formatter ignore the jinja code, or just add normal comments. I did a mix between both but I mainly used normal comments.

### Pep8

For python I used the cornflakes-linter which is a wrapper for flake8. This also worked really good and it did most of the formatting for me, but I did notice a few issues when I checked my python files online. It seems that the cornflakes-linter missed a few lines that were too long and it also missed whitespace in some places.

[This tool](http://pep8online.com/) is what I used to double check if I had missed any pep8 issues and I fixed all that I could find.

### HTML

Validating the html was a bit problematic because the tool warned alot about the jinja code and it was a bit hard to see the real issues but this should be right now as far as I can tell.

One example of this problem is that it warned me about a stray doctype declaration in the base template, but as far as I can tell this is just because the jinja code is on the line before.

## Visualization of my database

[database diagram](https://github.com/Tommyshub/restaurant/blob/main/static/images/database_diagram.png)

## Deployment

I performed the following steps in deploying my site:

### GitHub

- Pushed my commits from git to github.

- Logged in to my github account.

- Selected my repositories.

- Navigated to shopping-list.

- Clicked on settings.

- Scrolled down to where I can do the github pages settings.

- Selected the mastench from the dropdown menu.

- Clicked on save.

### Heroku

- Created a repository for this application

- Connected GitHub to Heroku under the "deploy" tab

- Clicked on deploy

- Added my config variables in the settings / reveal config vars tab.

- Added a postgres database and changed my settings file to include it.

- Migrated my database using the python manage.py migrate command.

- setup static files hosting.

First I used amazon s3 bucket to host my static files but after just a few days I got an email warning me that the free tier was almost used up, so I decided to change this to use whitenoise so that my static files can be served by the webapp directly.

I realize that this is not ideal when it comes to performance but I think it will be okay for this application.

You can [go here](https://the-greenhouse-1.herokuapp.com/) if you are interested in checking out my website.

## Acknowledgments and Credits

I would like to make it clear that I referenced and used a lot of what we learned during the Boutique Ado project when creating this, especially when it came to connecting to the stripe payments system.

I got a little bit help from the tutor support and an acquaintance when creating the coupon codes. I had problems figuring out how to subtract the discount from the total in the context processor, so I got advised to add the discount to the settings.py file and I also got adviced how to best check for used coupons.

### Images

I got all the images from and I would like to thank these people for making them available for the public to use.

- Deryn Macey
- Taylor Kiser
- Jordan Nix
- Irene Kredenets
- Fabio Alves
- Luis Gonzalez
- Adalia Botha

## Coupon Codes for Testing

I considered adding the coupon codes to the confirmation email but I decided not to because I felt that it was less of a risk
that they would be missed if I added them here instead.

Here are two codes that can be used for testing:

Code20 and Institute21

## Changes made after the 14th of July 2016

### Coupon codes

Here I had a problem with the users not being given the right feedback after applying coupon codes, to fix this I added the discount to the
checkout model and made sure the discount and new total will be displayed correctly everywhere. I also made sure to set the discount back to zero after it was applied so that the users can't use the coupon code twice before the session is emptied.

When testing the new changes I encountered a problem, both the discount and the total could be set to zero if the user tried to refresh the checkout success page so to fix this I am now redirecting the users to the order history page instead.

This made the message that the users are viewing a past order when clicking on the order history link a bit awkward so I decided to remove that message. I figured that it should be clear to the user that it is a past order either way, because of the date in the order information but also because of the navigation actions.

To test so that this works as expected I made several orders with different items and I appplied the discount codes to check that it worked correctly. I also made a few orders without discount directly after to insure that the discount was gone from the session.
