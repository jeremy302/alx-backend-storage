-- creates a trigger
DROP TRIGGER IF EXISTS before_user_update;
DELIMITER //
CREATE TRIGGER before_user_update BEFORE UPDATE ON users FOR EACH ROW
BEGIN
  IF OLD.email != NEW.email THEN
     SET NEW.valid_email = 0;
  END IF;
END //
DELIMITER ;
