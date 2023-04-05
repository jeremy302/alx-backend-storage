-- creates a trigger
DROP TRIGGER IF EXISTS after_order_insert;
DELIMITER //
CREATE TRIGGER after_order_insert AFTER INSERT ON orders FOR EACH ROW
BEGIN
UPDATE items SET items.quantity = items.quantity - NEW.number
WHERE items.name = NEW.item_name;
END //
DELIMITER ;
