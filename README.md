![image](https://github.com/user-attachments/assets/de46f57e-06bf-466e-9f88-446c5ef452fb)# MyBand Webapp (Listen With Pvle_TheEngineer)

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Description
This project is a web application built using the Django framework. It includes two main components: `myband`, a web application for managing band information with an embedded music player from Spotify, and `user_auth`, a user authentication module. This project demonstrates the use of Django for building robust web applications with user management features.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/GWMolekoa/myBand.git
   cd myband

  This command copies the repository from GitHub to your local machine.
  
  ## Usage
  1. **Create and activate a virtual environment** using the following code in your cmd:

       python3 -m venv venv

       To activate the virtual environment, type the following into your cmd: 
         **On macOS and Linux:** source venv/bin/activate  
         **On Windows:** venv\Scripts\activate

       After activation, your terminal prompt should change to indicate that the virtual environment is active.

    
  2. **Install dependencies**:
       With the virtual environment activated, you need to install the necessary dependencies for the project.
       These dependencies are typically listed in a requirements.txt file.

       Run the following code in your cmd:

       pip install -r requirements.txt

       This command reads the requirements.txt file and installs all the packages listed there.

     
  3. **Apply migrations**:
        Django uses migrations to propagate changes you make to your models (adding a field,
        deleting a model, etc.) into your database schema.

        Apply migrations by running the following command:
     
        python manage.py migrate

       This command applies all the migrations needed to set up your database schema.

     
  4. **Run the development server**:
        Finally, you need to run the Django development server to start the application.

        Run the development server by running the following command:

        python manage.py runserver

        This command starts the development server, and you should see output indicating that the server is running.
  

  5.   After running the development server, navigate to http://127.0.0.1:8000 in your web browser. 
       You'll arrive at the home page of "Listen With Pvle_TheEngineer". To access and navigate the
       contents my webapp you must be authenticated. Register as a new user or log in (if you're an
       existing user) and you'll be able to read my band's information and toggle through the embedded
       Spotify playlist to hear some of your favourite songs by each band.

       Below are some screenshots of the project in action:


       **Home Page (Listen With Pvle_TheEngineer) - Content Disabled:**

       After navigating to the URL, you'll be directed to the home page. Notice the content is disabled and you will not
       be able to navigate the rest of the webapp without user authentication. Click on register or login below or above the
       screen to get started to enjoy a historical musical experience.
       ![image](https://github.com/user-attachments/assets/cb883f8e-1823-47b8-91c9-c97b0c3a6eaf)


       **Registration Page:**

       Here you will create a new username and password and fill out your credentials in order to use the webapp as
       shown in the imaage below. When done, click on register and you will be redirected to the login page.
       ![image](https://github.com/user-attachments/assets/f1a6e094-5189-4d03-a7db-43bddb7f129c)


       **Login Page:**

       Following registration, you'll be redirected to the login page below where you'll insert your username and password.
       When done, click on the login button and you will redirected back to the home page with all content enabled.  
       ![image](https://github.com/user-attachments/assets/0add4f54-785e-42ed-b42b-45ded52c7b3b)


       **Home Page (Listen With Pvle_TheEngineer) - Content Enabled:**
     
       You'll now be able to read more about my favourite artists and learn about their history on the next page.
       ![image](https://github.com/user-attachments/assets/c97b641e-8b6e-4614-ba2c-789ee9d76e1d)

       ![image](https://github.com/user-attachments/assets/06b8fdbf-61e7-4d52-b09d-e0b50aa6def9)


  6.   When you're all done, be sure to logout, by clicking on the **'Logout'** button at the top-left of the page. Enjoy!

       

  ## Credits
  Developed by **Gaopalelwe Wilson Molekoa - Software Engineer**


     

     

