
# Librac University

Librac University introduces opportunity to Universities around the world which gives their students to select courses for their students before a semester starts,drop courses and see the assignments of their course.The teachers can schedule and drop assignments for their courses they are assigned in.The VC of the University is the admin who can append new courses and assign teachers to any particular courses.It makes the life of students and teachers easier.

## Tech Stack

**Backend Technology used:**  Python, Django, Django Rest Framework

**Database:**  PostgreSQL



## Live Link

[Librac University](https://librac-backend.vercel.app/) is currently deployed on vercel.Click on the blue link to go to the live website.


## Authors

- [Asifmahmud436](https://github.com/Asifmahmud436)



## Installation
Actually ,you can just run the requirements.txt file and run the project.But to be 100% sure ,just install the packages below to smoothly run the project on local server. 

Install djangorestframework:

```bash
  pip install djangorestframework
```
Install djangorestframework-authtoken:

```bash
  pip install djangorestframework-authtoken
```
Install dj-rest-auth:

```bash
  pip install dj-rest-auth
```
Install django-cors-headers:

```bash
  pip install django-cors-headers
```
Install pillow:

```bash
  pip install pillow
```
Install requests:

```bash
  pip install requests
```
    
## API Reference

#### Get all teachers

```http
  GET /api/teachers/list/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | get all the teachers |

#### Get all students

```http
  GET /api/students/list/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | get all the students |

#### Get all courses

```http
  GET /api/courses/list/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | get all the courses of the organization |

#### Get all dashboards

```http
  Get /api/dashboards/list/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | get the dashboard of everyone |

#### Get assignments of a student
```http
  Get /api/assignments/list/?student_username=${userInfo.username}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | get all the assignments of a particular student by their username |

#### Get dashboard of a student
```http
  Get /api/dashboards/list/?student_name=${data.username}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | get dashboard of a particular student by their username |

#### Get assignments of a teacher
```http
  Get /api/assignments/list/?teacher_username=${userInfo.username}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | get all the assignments of a particular teacher by their username |

#### Get dashboard of a teacher
```http
  Get /api/courses/list/?teacher_name=${data.username}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | get all the courses of a particular teacher by their username |


#### Get user details

```http
  GET /api/accounts/user/?user_id=${user_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | get any user details by user_id |

#### Append a course as a VC
```http
  POST /api/courses/list/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | append a course  as a VC/Admin |


#### Logout

```http
  POST /api/accounts/logout/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | logout as any user |

#### Login

```http
  POST /api/accounts/login/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | login as any user |

#### Register as a student

```http
  POST /api/students/register/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | register as a student |

#### Register as a teacher

```http
  POST /api/teachers/register/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | register as teacher |




#### Edit teacher details

```http
  PATCH /api/teachers/list/${id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | edit teacher details by id |

#### Edit student details

```http
  PATCH /api/student/list/${id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | edit student details by id |


#### Drop Course

```http
  PATCH /api/dashboards/list/${courseId}/drop/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | drop a course by a student |





## Run Locally

Clone the project

```bash
  git clone https://github.com/Asifmahmud436/librac-backend
```

Go to the project directory

```bash
  cd librac-backend
```

Install dependencies

```bash
  pip install django
```

Start the server

```bash
  python manage.py runserver
```



## Features

- Live previews
- Fullscreen mode
- Cross platform

## Lessons Learned

After completing this project, I can: 
- Use multiple role base user 
- Deploy Projects on Vercel 
- Use supabase as a site for deploying my PostgreSQL


## Contribution

Contributions are always welcome!

Fork and clone the Project to your own repository.Then create a branch,update the code and send a pull request.

Please adhere to this project's `code of conduct`.


## Support

For support, email safaandsafa4@gmail.com or join our discord: https://discord.gg/DaU4QuNM






## 🔗 Connect with me:
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/asif-mahmud-3bb1a627a/)

## Feedback

If you have any feedback, please reach out to us at safaandsafa4@gmail.com

