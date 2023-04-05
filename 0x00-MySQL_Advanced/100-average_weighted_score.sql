-- creates a procedure

DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser//

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
  DECLARE average FLOAT;

  SELECT IF(s.w_sum = 0, 0, s.s_sum/s.w_sum) INTO average FROM
   (SELECT SUM(t.score * t.weight) as s_sum, SUM(t.weight) AS w_sum
    FROM (SELECT score, (SELECT weight FROM projects
     WHERE projects.id=project_id LIMIT 1) AS weight
     FROM corrections WHERE corrections.user_id=user_id) AS t) AS s;
  UPDATE users SET average_score=average WHERE id=user_id;
END //
DELIMITER ;
