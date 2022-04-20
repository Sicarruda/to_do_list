CREATE TABLE Tasks (
  id_tasks INT NOT NULL AUTO_INCREMENT,
  user_task varchar(255),
  dead_line DATE,
  date_creation varchar(50),
  PRIMARY KEY (id_tasks)
);