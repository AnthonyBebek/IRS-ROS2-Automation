<a name="readme-top"></a>
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]




<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">IRS-ROS2-Automation</h3>

  <p align="center">
    Description of repo
    <br />
    <a href="https://github.com/AnthonyBebek/IRS-ROS2-Automation"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/AnthonyBebek/IRS-ROS2-Automation">View Demo</a>
    ·
    <a href="https://github.com/AnthonyBebek/IRS-ROS2-Automation/issues">Report Bug</a>
    ·
    <a href="https://github.com/AnthonyBebek/IRS-ROS2-Automation/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This project was built with

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)

![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff)

![ROS](https://img.shields.io/badge/ros-2496ED?logo=ros&logoColor=fff)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
### Main Contributior


Anthony Bebek  
* [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/anthony-bebek-52b30a2b7/)
   

<!-- GETTING STARTED -->

## Getting Started

#### Git

#### Install for Windows

1. Visit the official git website: https://git-scm.com/download/win

2. Click on the "Click here to download" button to download git.

3. Once the installer is downloaded, double-click on it to start the installation process.

4. Follow the on-screen instructions to complete the installation.

5. During installation, git might require enabling certain features or restarting your system. Follow the prompts accordingly.

#### Install for linux

1. Run the following command 
``` sudo apt install git-all ```

<!-- Installation -->

### Installation


#### Installing Docker On Linux

This method can also be found on the offical docker website.
<a href = "https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04"> Found here </a>

1. Setup Docker's ```apt``` repository by running the following commands
```
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
apt-cache policy docker-ce
sudo apt install docker-ce
```
2. Install docker with this command
```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
3. Check docker is installed with
```
sudo docker run hello-world
```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE -->
## Usage

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- CONTACT -->
## Contact


Anthony Bebek  
* [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/anthony-bebek-52b30a2b7/)
   

Project Link: [https://github.com/AnthonyBebek/IRS-ROS2-Automation](https://github.com/AnthonyBebek/IRS-ROS2-Automation)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/AnthonyBebek/IRS-ROS2-Automation.svg?style=for-the-badge
[contributors-url]: https://github.com/AnthonyBebek/IRS-ROS2-Automation/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AnthonyBebek/IRS-ROS2-Automation.svg?style=for-the-badge
[forks-url]: https://github.com/AnthonyBebek/IRS-ROS2-Automation/network/members
[stars-shield]: https://img.shields.io/github/stars/AnthonyBebek/IRS-ROS2-Automation.svg?style=for-the-badge
[stars-url]: https://github.com/AnthonyBebek/IRS-ROS2-Automation/stargazers
[issues-shield]: https://img.shields.io/github/issues/AnthonyBebek/IRS-ROS2-Automation.svg?style=for-the-badge
[issues-url]: https://github.com/AnthonyBebek/IRS-ROS2-Automation/issues
[license-shield]: https://img.shields.io/github/license/AnthonyBebek/IRS-ROS2-Automation.svg?style=for-the-badge
[license-url]: https://github.com/AnthonyBebek/IRS-ROS2-Automation/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
