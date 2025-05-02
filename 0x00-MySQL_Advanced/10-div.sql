-- Creates a function SafeDiv that divides (and returns) the first by 
-- the second number or returns 0 if the second number is equal to 0.
DELIMITER $$

-- Create the SafeDiv function
CREATE FUNCTION SafeDiv(a INT, b INT) 
RETURNS FLOAT
DETERMINISTIC
BEGIN
    -- If b is 0, return 0, otherwise return a / b
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END $$

DELIMITER ;
