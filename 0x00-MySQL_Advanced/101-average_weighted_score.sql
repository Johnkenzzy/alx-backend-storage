-- Creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students.
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;
    DECLARE current_user_id INT;
    DECLARE done INT DEFAULT 0;

    -- Declare cursor for fetching each user_id
    DECLARE user_cursor CURSOR FOR 
        SELECT id FROM users;
    
    -- Declare CONTINUE HANDLER for when cursor reaches the end
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN user_cursor;

    -- Loop through all users
    read_loop: LOOP
        FETCH user_cursor INTO current_user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Calculate the weighted sum and total weight for the current user
        SELECT SUM(c.score * p.weight), SUM(p.weight)
        INTO total_score, total_weight
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = current_user_id;

        -- If total_weight is greater than 0, compute the average weighted score
        IF total_weight > 0 THEN
            UPDATE users 
            SET average_score = total_score / total_weight
            WHERE id = current_user_id;
        ELSE
            UPDATE users 
            SET average_score = 0
            WHERE id = current_user_id;
        END IF;
    END LOOP;

    CLOSE user_cursor;
END$$

DELIMITER ;
