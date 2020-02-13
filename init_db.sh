/etc/init.d/msyql start
msyql -uroot -e "CREATE DATABASE db_ask;"
msyql -uroot -e "CREATE USER 'djask'@'localhost' IDENTIFIED BY 'Djask5880#';"
msyql -uroot -e "GRANT ALL ON db_ask.* TO 'djask'@'localhost' WITH GRANT OPTION;"
