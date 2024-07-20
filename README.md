# Voting_website


## Authors

- Name: [Ankit Ranjan](https://github.com/Viratankit9)
- LinkedIn Profile : [Linkedin](https://www.linkedin.com/in/ankit-ranjan-405199234/).
- I am from Bihar, India.
- Date : 30-04-2024

- ### Certificate Of Merit

<p align="center">
    <img src="evoteSC/Screenshot 2024-04-22 223831.png" width="800" />
</p>

- ### Certificate Of Appreciation

<p align="center">
    <img src="evoteSC/Screenshot 2024-04-22 223652.png" width="800" />
</p>

## Table of Contents

1. [Abstract](#abstract)
2. [Problem Statement](#problem-statement)
3. [Proposed Solution](#proposed-solution)
4. [Technology used](#technology-used)
5. [Installation and Usage](#installation-and-usage)
6. [Results](#results)
7. [Contact](#contact)

---

## Abstract

- This project deals with developing voting web application using Django for conducting exit poll which help to predict outcome of election result.
- Compared to traditional methods, it saves costs by eliminating physical polling process and ensures transparency.
- Homepage features "About" and "Contact" sections in the navigation bar, with separate sections for Election Poll and Public Poll in the body.
- In Election poll and Public poll, authenticated user can cast only one vote to listed political party and created poll respectively, User can also view result in both section.
- This application can serve as a centralized platform for organizations, communities, and individuals to create, manage, and participate in online polls.

## Problem Statement

In today's digital age, there is a growing need for platforms that allow users to easily access and participate in polls. Many existing solutions lack intuitive interfaces and comprehensive features, making it difficult for users to engage effectively. Our goal is to create a solution that provides a seamless and user-friendly experience, empowering users to express their opinions and engage in democratic processes effortlessly.

## Proposed Solution

- To create a user-friendly voting platform, we designed an attractive interface using Bootstrap, HTML, and CSS, allowing users to navigate and vote effortlessly.
- User authentication is handled through login and signup pages, ensuring secure access to features, with backend logic implemented in Django's view files.
- Our Django application includes four key models (Party, Vote, Poll, UserVote) in the `models.py` file to manage data for voting results, poll questions, and political party details.
- Additionally, users can delete outdated polls in the Public Poll section, keeping the platform relevant and up-to-date.

## Technology used

- Bootstrap : (Frontend framework)
- HTML
- CSS
- JavaScript
- Django Framework : (Backend)
- SQLite : (Database)
- Responsive Design Principles

## Installation And Usage

### Installation

1. Clone the repository:

```bash
$ https://github.com/Viratankit9/Voting_website.git
```

2. Navigate to the project directory:

```bash
$ cd Voting_website
```

3. To install the Django, use the following command:

```bash
python --version
```

```bash
pip --version
```

```bash
py -m pip install Django
```

4. Apply Migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the `manage.py` using Python:

```bash
python manage.py runserver
```

6. Starting development server at http://127.0.0.1:8000/

### Usage
- Register and Log In: Create an account and log in.
- Create Polls: Navigate to the admin panel and create new polls.
- Vote: Participate in polls and submit your votes.
- View Results: Check the results of the polls you have voted in.

## Results

1. Home Page ( Landing page )

<p align="center">
    <img src="evoteSC/Screenshot (49).png" width="800" />
</p>

<p align="center">
    <img src="evoteSC/Screenshot (50).png" width="800" />
</p>

3. Login page

<p align="center">
    <img src="evoteSC/Screenshot (54).png" width="800" />
</p>

4. Election Poll page

<p align="center">
    <img src="evoteSC/Screenshot (51).png" width="800" />
</p>

5. Election Result page

<p align="center">
    <img src="evoteSC/Screenshot (53).png" width="800" />
</p>

5. Public Poll page

<p align="center">
    <img src="evoteSC/Screenshot (56).png" width="800" />
</p>

5. Poll Creation page

<p align="center">
    <img src="evoteSC/Screenshot (57).png" width="800" />
</p>

6. Public Poll Cast a Vote page

<p align="center">
    <img src="evoteSC/Screenshot (58).png" width="800" />
</p>

7. About page

<p align="center">
    <img src="evoteSC/Screenshot (55).png" width="800" />
</p>


## Our Mission:
At our online voting website, our mission is to promote democratic participation by making the voting process accessible to everyone, regardless of their location or circumstances. We believe that every voice should be heard, and our platform empowers individuals to express their opinions and make informed decisions.

## Key Features:
- **User-Friendly:** Interface: Our website features an intuitive and user-friendly interface, making it easy for users to navigate and cast their votes efficiently.
- **Security:** We prioritize the security and integrity of the voting process. Our platform utilizes robust encryption and authentication mechanisms to ensure the confidentiality and accuracy of each vote.
- **Accessibility:** Whether you're voting from the comfort of your home, on-the-go, or from a remote location, our website is accessible from any device with an internet connection.
- **Transparency:** We believe in transparency and accountability. Users can verify the status of their votes and track the results of ongoing polls and elections in real-time.


## Get Involved:
Are you ready to make your voice heard? Join our online voting community today and be a part of the democratic process!

## Contact

For any inquiries or support, please contact [Linkedin](https://www.linkedin.com/in/ankit-ranjan-405199234/).

---
