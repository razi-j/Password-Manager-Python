# Password-Manager-Python

### A simple mini project

 <p>
  Hidden Keys Password Manager is based on Python's <a href="https://pypi.org/project/cryptography/"> Cryptography </a> module. It mainly utilizes the    Password Based Key Derive Function to generate a hidden key. This hidden key would be used by Fernet to encrypt the password given by the user.
  </p>

<div>
<h3>How does it work?</h3>
<img width="100%" src="https://github.com/razi-j/Password-Manager-Python/blob/main/Demo.gif"/>
 <br>
  <p>
    <h3>Steps in Using Hidden Keys: </h3>
    <ol type="1">
      <li> Generate A Key and your Main Password for the CLI </li>
      The program will prompt you to give a main password when adding new passwords or accessing your passwords. You may regenerate a key and salt for the program however, passwords that were stored from a key will not be accessible by a different key and will raise errors.
      <li> Add Your Passwords </li>
      <li> View Your Passwords! </li>
  </ol>
 <h3>After doing those steps your Password Manager directory would look something like:</h3>
 <br>
 <img width="80%" src="https://github.com/razi-j/Password-Manager-Python/blob/b8a78ee557f653b176f677669a61f42582773f13/Screenshot%20from%202023-04-11%2000-39-18.png"/>
  </p>
</div>

<h2> This Program is Not 100% Secure </h2>
<p> It still lacks a lot of features that would make it passable as a password manager. The key, salt, and logs used by this program are still stored in files which are accessible by anyone. Kindly proceed with caution if you do decide to use this as a password manager. </p>

---

<p> I plan on making another version of this that utilizes CRUD through a MySQL server. Thank you for checking this out! </p>
