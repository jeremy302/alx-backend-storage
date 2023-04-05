-- creates a view
CREATE OR REPLACE VIEW need_meeting AS
  SELECT name FROM students WHERE score < 80 AND (ISNULL(last_meeting) OR DATE_SUB(CURDATE(), INTERVAL 1 MONTH) > last_meeting);
