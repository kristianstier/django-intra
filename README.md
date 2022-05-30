# django-intra
## Lightweight intranet application for organisations to share announcements and contact information with their members or employees, based on django

### Features
- Comfortable backend to manage users, groups and roles
- Fully responsive design
- Users can search other users and see contact details
- Authors (usergroup) can publish announcements that all users can see
- Dashboard showing the latest announcements
- Announcements can be pinned on the dashboard to be permanently visible

---

### Setup
Important! This tutorial shows how to set up the app locally for testing. What to consider when deploying the app to a production site and how the deployment of Django apps works can be read at https://docs.djangoproject.com/en/4.0/howto/deployment/.  <br><br>


#### 1. Clone the repository. I would recommended to only clone the main branch and not the whole repository. 

```bash
git clone -b main --single-branch https://github.com/kristianstier/django-intra
```

#### 2. Install the requirements using pip

```bash
pip install -r django-intra/requirements.txt
```

#### 3. Setup the database
```bash
python3 django-intra/manage.py makemigrations
python3 django-intra/manage.py migrate
```

#### 4. Create a superuser as the admin account
```bash
python3 django-intra/manage.py createsuperuser
```

#### 5. Start the server and login as the superuser
```bash
python3 django-intra/manage.py runserver
```

---

### Images
![image0](https://github.com/kristianstier/django-intra/blob/assets/dashboard.png)  
Dashboard

![image1](https://github.com/kristianstier/django-intra/blob/assets/intra_admin.png)  
User management in the backend

![image2](https://github.com/kristianstier/django-intra/blob/assets/login_mobile.png)  
Mobile login screen

![image3](https://github.com/kristianstier/django-intra/blob/assets/mobile_menu.png)  
Mobile menu

![image4](https://github.com/kristianstier/django-intra/blob/assets/user_detail.png)  
User details in the frontend

![image5](https://github.com/kristianstier/django-intra/blob/assets/users_list.png)  
List of users in the frontend

![image6](https://github.com/kristianstier/django-intra/blob/assets/announcements_list.png)  
List of announcements in the frontend

![image7](https://github.com/kristianstier/django-intra/blob/assets/announcements_list_mobile.png)  
List of announcements in the frontend on mobile device

![image8](https://github.com/kristianstier/django-intra/blob/assets/authors_group.png)  
Group management showing the author group