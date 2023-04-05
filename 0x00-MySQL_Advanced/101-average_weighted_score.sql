-- creates a procedure

DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers//

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  DECLARE average FLOAT;
  DECLARE user_id INT;
  DECLARE done INT;
  DECLARE cur CURSOR FOR select id from users;
  DECLARE CONTINUE HANDLER FOR NOT FOUND
   BEGIN
    SET done = 1;
   END;

  SET done = 0;
  OPEN cur;
  FETCH cur into user_id;
  WHILE (done = 0) DO
   SELECT IF(s.w_sum = 0, 0, s.s_sum/s.w_sum) INTO average FROM
    (SELECT SUM(t.score * t.weight) as s_sum, SUM(t.weight) AS w_sum
     FROM (SELECT score, (SELECT weight FROM projects
      WHERE projects.id=project_id LIMIT 1) AS weight
      FROM corrections WHERE corrections.user_id=user_id) AS t) AS s;
   UPDATE users SET average_score=average WHERE id=user_id;
   FETCH cur into user_id;
  END WHILE;
  CLOSE cur;
END //
DELIMITER ;
