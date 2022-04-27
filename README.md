## Opening a server using XAMPP for Windows


Install XAMPP from [Official Website](https://www.apachefriends.org/index.html). Then Follow the steps below:

1. Start `Apache` server and press `Admin` to check everything is working correctly.

2. By default, the `localhost` shows demo page from directory:

   ```shell
   # Usually :
   C:\xampp\htdocs\
   # In general :
   <installation folder>\htdocs\
   ```

3. In the installation folder, there is a file (`\apache\conf\extra`) named `httpd-vhosts.conf`.
   This is the configuration file that contains information of which page to show in the server.

4. Add these lines at the end of the file:

   ``` shell
   <VirtualHost *:80>
          DocumentRoot "document-root-folder"
          ServerName localhost
   </VirtualHost>
   ```

5. XAMPP always looks for the `index.html` or `index.php`.  So, either one of the file needs to be in the root folder.

6. If the server fails to run, this is probably the XAMPP does not have access to that directory.
   This can be solved by adding these lines at the top of `<Virtualhost *:80>`:

   ```shell
   <Directory "document-path">
           Options Indexes FollowSymLinks MultiViews
           AllowOverride all
           Order Deny,Allow
           Allow from all
           Require all granted
   </Directory>
   ```

7. At this point you are good to go. All the devices connected in the same network can access the server by typing the IP address in the browser.

