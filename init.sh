pip3 install --force-reinstall django==2.0.13
pip3 install pymysql
pip install pymysql
ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
unlink /etc/nginx/sites-enabled/default
/etc/init.d/nginx restart
/etc/init.d/msyql start
mysql -uroot -e "CREATE DATABASE db_ask;"
mysql -uroot -e "CREATE USER 'djask'@'localhost' IDENTIFIED BY 'Djask5880#';"
mysql -uroot -e "GRANT ALL ON db_ask.* TO 'djask'@'localhost' WITH GRANT OPTION;"