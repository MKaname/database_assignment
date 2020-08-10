database assignment  
**server build**  
(@sakura-server)
1. mkdir webapp
2. git clone @ webapp
3. install gcc,python3-devel
4. install httpd httpd-tools httpd-devel httpd-manual
5. install pyenv
6. install django mod-wsgi mod-wsgi-httpd
7. cd <project directory>
8. sudo ../bin/mod_wsgi-express start-server --port=80 --user=djangowebserver mysite/wsgi.py

