CREATE TABLE User (
  id_user INT NOT NULL AUTO_INCREMENT,
  email varchar(50),
  password varchar(50),
  PRIMARY KEY (id_user)
);


CREATE TABLE Tasks (
  id_tasks INT NOT NULL AUTO_INCREMENT,
  user_task varchar(255),
  dead_line DATE,
  date_creation varchar(50),
  id_user INT(11), 
  PRIMARY KEY (id_tasks),
  FOREIGN KEY(id_user) REFERENCES User(id_user)
);