# Django-Poll-App

### **Overview**
<hr/>

Django poll app is a full-featured polling app. Users can have to register in this app to show the polls and to vote. If users already voted then they can not vote again. The only owner of the poll can add a poll, edit a poll, update a poll, delete a poll, add choice, edit choice, update choice, delete choice. If a poll is ended it can not be voted. The ended poll only shows the user the final result of the poll.Users can not delete poll options that have lesser than two options, poll must have more than two options to delete other option


### **Prerequisites**

Basic knowledge of python.
Understanding of MVT structure.

### **Installation**
<hr />

The Code is written in Python 3.7. If you don't have Python installed you can find it <a href="https://www.python.org/downloads/">here</a>. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after <a href="https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository">cloning</a> the repository:
    
  - To run this project you have follow below steps.
  
  1] Open the terminal and go inside the project directory where the project is located.
  
  - Migrate the database.
  
  2] python manage.py makemigrationn
  3] python manage.py migrate
  
  - To access admin panel you have hit blow command.
  
  4] python manage.py createsuperuser
  
  - To run the program in local server you have to use below command.
  
  5] python manage.py runserver
      - After hiting this command it will give link. click to link http://127.0.0.1:8000/ or Paste the link in your browser.
    
### **Screeshots**

### **Registration Page**

![Screenshot (115)](https://user-images.githubusercontent.com/51736427/102342295-0e878d00-3fbf-11eb-9316-170c76fdba38.png)

### **Login Page**

![Screenshot (116)](https://user-images.githubusercontent.com/51736427/102342506-54dcec00-3fbf-11eb-8d39-a326f5fa031a.png)

### **Home Page**

![Screenshot (117)](https://user-images.githubusercontent.com/51736427/102342600-7b028c00-3fbf-11eb-94d4-2eb3e36a73d9.png)

### **Logged In User Dashboard**

![Screenshot (118)](https://user-images.githubusercontent.com/51736427/102342661-9372a680-3fbf-11eb-8041-6abfe793b5d1.png)

### **Edit Poll**

![Screenshot (120)](https://user-images.githubusercontent.com/51736427/102342803-c2891800-3fbf-11eb-960a-d31828514fe9.png)

  <br/>
  Here, poll have two options so user can't delete any options. If user want to delete any options they need to add one more option to delete other options.
 
 ### **Add Choice**
 
 ![Screenshot (121)](https://user-images.githubusercontent.com/51736427/102343051-15fb6600-3fc0-11eb-9f32-f46842209ac0.png)

### **Edit Poll(After adding one more options)**
  
![Screenshot (122)](https://user-images.githubusercontent.com/51736427/102343431-8e622700-3fc0-11eb-97c5-606c232894dd.png)

### **Voting Poll**

![Screenshot (123)](https://user-images.githubusercontent.com/51736427/102343702-dbde9400-3fc0-11eb-9dac-402a6d825a90.png)

### **Ended Poll**

  - After ending the poll page will be redirect to the result page and show the result of the poll
  
![Screenshot (124)](https://user-images.githubusercontent.com/51736427/102343737-e8fb8300-3fc0-11eb-933d-855137fa4e5b.png)


### Thank You!
  




