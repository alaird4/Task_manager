<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


  <p align="center">
    <p>Project Name:Task_manager </p>
    <p>Purpose: This Task manager project is a management system that can be used by small businesses to assign tasks to staff. It can also allow staff to track tasks and mark them as       complete. The system will also allow management teams to look at the statistics and add new members to the system.</p>
    <p>I hope you enjoy following the management system through on python.</p>
    <br />
    <a href="https://github.com/alaird4/Task_manager"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/alaird4/Task_manager">View Demo</a>
    ·
    <a href="https://github.com/alaird4/Task_manager/issues">Report Bug</a>
    ·
    <a href="https://github.com/alaird4/Task_manager/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>




### Built With

Python 

![image](https://github.com/alaird4/Task_manager/assets/116030750/10b1064d-6be5-466c-a954-d57074d6a593)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started



### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python
  ```sh
  pip install python
  ```
* Check python version
  ```sh
  python --version
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/alaird4/Task_manager
   ```
2. Install python packages
   ```sh
   https://www.python.org/downloads/ 
   ```
3. 
   ```sh
   pip install python
   ```
   ```sh
 4.  More information here: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/ 
   ```
   
   
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The management system begins with asking you to login and therefore you need to enter a username and password:
<img width="381" alt="image" src="https://github.com/alaird4/Task_manager/assets/116030750/d86e097c-77eb-4a2b-aa4d-c1dbd0244297">

If the username and password does not appear on the 'user.txt' file, then you can't login to the system and will need to be set up as a user by an admin user. 

Once you are logged in, you are presented with a menu:
<img width="580" alt="image" src="https://github.com/alaird4/Task_manager/assets/116030750/43d1d603-2648-4405-a25a-7aee24fa37b4">

Select which option you would like by typing in the letter that is next to your desired option. For example, if you would like to register a new user, type in 'r' and then click enter on your keyboard. 

<img width="320" alt="image" src="https://github.com/alaird4/Task_manager/assets/116030750/7b4249a5-2dfe-413e-a20f-3c8cd4a0a024">

Each section will as series of questions to allow you to achieve what you would like it to do. 

Let's start with **'Registering a User'**. 
You will be asked to enter the new username and password, then confirm the password you have entered. If the username and password, does not exist, they are both added to the user.txt file.
<img width="427" alt="image" src="https://github.com/alaird4/Task_manager/assets/116030750/4cb5f7a9-d44e-4f21-8fda-f87d9abf05db">

However, if they have been added, the user is informed.
<img width="532" alt="image" src="https://github.com/alaird4/Task_manager/assets/116030750/7835355c-8ec1-4330-8399-4234a9d635e6">

**Adding a task**
Put in the letter 'a'when the menu is presented.
You will then be asked to fill in some information including; 
the username of the assignee
the title of the task
A description of the task
The due date of the task

<img width="589" alt="image" src="https://github.com/alaird4/Task_manager/assets/116030750/31977989-ba21-47ef-8e30-6c0b9e99fb7b">
The task is then added to the tasks.txt file and the user is informed:

<img width="221" alt="image" src="https://github.com/alaird4/Task_manager/assets/116030750/6ba147e6-82ad-44ee-8bf2-ccafc7e25b72">

**View all Tasks**
To view all your tasks, put in the letters 'va' when presented with the menu.
Python then reads all the tasks on the tasks.txt file and you are presented with all the tasks in an easy to read format:
![image](https://github.com/alaird4/Task_manager/assets/116030750/c1fd6939-1609-4fbb-a92e-8372e1857eb1)

The tasks are also numbered and you will see tasks 3 and 4 in the screenshot above. 

**View my Tasks**
To view all the tasks that have been assigned to you, type in the letters 'vm' when presented with the menu. 
You will then be presented with all the tasks that are assigned to you. The systems looks at the name you are logged in as: 

<img width="466" alt="image" src="https://github.com/alaird4/Task_manager/assets/116030750/8b23acfd-f4a0-403a-a184-aac2767830d3">

If there are no tasks assigned to you, the system let's you know:

<img width="639" alt="image" src="https://github.com/alaird4/Task_manager/assets/116030750/e68faa3a-8092-449b-b6b4-9f414ba6b891">

**Generate Reports**
To generate any reports, type in the letters 'gr'.

The system will then create a new txt file called 'task_overview.txt' and all the reports are stored in there:
<img width="397" alt="image" src="https://github.com/alaird4/Task_manager/assets/116030750/67f688a3-599e-4181-a978-cecfb067be3f">

The reports will give you an overview of how many tasks there are, how many are complete and overdue, along with the percentages. 

**Display Statistics**

To display the statistics, type the letters 'ds' from the menu. 

The system again, created another txt file called 'user_overview.txt' and the statistics are displayed in there:
<img width="410" alt="image" src="https://github.com/alaird4/Task_manager/assets/116030750/42f6f57b-2677-47e6-a11c-1def3ee4f1a3">

The statistics will give you an overview of how many users are registered and a user breakdown of many tasks are complete and overdue

**Exit**
To exit, just simply type in the letter 'e' when presented with the menu. 



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated** so please do pass these on.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Ashley Laird - [LinkedIn](https://uk.linkedin.com/in/ashley-laird-39415ab7) - ashley.laird93@yahoo.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [HyperionDev](https://coding-bootcamps.ed.ac.uk/uoe-courses/)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
