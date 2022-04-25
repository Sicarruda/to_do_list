CREATE TABLE Tasks (
  id_tasks INT NOT NULL AUTO_INCREMENT,
  user_task varchar(255),
  dead_line DATE,
  date_creation varchar(50),
  FOREIGN KEY (id_user) REFERENCES User (id_user)
)PRIMARY KEY (id_tasks);