-- creates a procedure
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER //
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score FLOAT)
BEGIN
  DECLARE project_id INT;
  
  IF (SELECT COUNT(*) FROM projects WHERE projects.name = project_name) = 0 THEN
     INSERT INTO projects (name) VALUES (project_name);
  END IF;
  SELECT id INTO project_id FROM projects WHERE projects.name = project_name LIMIT 1;
  INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END //
DELIMITER ;
