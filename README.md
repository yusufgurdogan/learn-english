# how to install?
1. clone from github and go to directory
```git clone https://github.com/yusufgurdogan/learn-english/ && cd learn-english```
2. install flask
```pip3 install flask```
3. run app
```python3 app.py```
app runs on port 1234. visit http://localhost:1234 from your browser.


4. (from now on, it's optional) install nginx to use it with a domain name.
```apt-get install nginx```
> (Nginx kurulumu için Türkçe anlatım: https://yusufgurdogan.com/nginx-ile-web-sunucusu-kurulumu/)
5. delete default nginx config and create your own config:
```rm /etc/nginx/sites-available/default && nano /etc/nginx/sites-available/default```
6. paste the following config to here:
```
server {
    listen 80;
    server_name example.com; # enter your own domain name
    # if you don't want to enter a domain name:
    # server_name _;
    location / {
        proxy_pass http://localhost:1234;
        proxy_set_header Host $host;
    }
}
```
7. "CTRL+X" and "y" and press enter to save the file.
8. (optional) Get https for the domain
```sudo add-apt-repository ppa:certbot/certbot```
```sudo apt install -y python-certbot-nginx```
```sudo certbot --nginx```
9. Enter your e-mail, enter 1 to accept the agreement, after that, you may enter N to reject getting notifications to your e-mail.
10. Select your domain name, press enter.
If everything is fine, you should be able to browse https://(yourdomainname).com
