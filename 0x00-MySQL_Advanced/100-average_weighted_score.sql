-- Creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;
    
    -- Calculate the weighted sum and the total weight
    SELECT SUM(c.score * p.weight), SUM(p.weight)
    INTO total_score, total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;
    
    -- Calculate and update the average weighted score for the user
    IF total_weight > 0 THEN
        UPDATE users 
        SET average_score = total_score / total_weight
        WHERE id = user_id;
    ELSE
        UPDATE users 
        SET average_score = 0
        WHERE id = user_id;
    END IF;
END$$

DELIMITER ;
