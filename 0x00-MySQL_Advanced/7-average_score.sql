-- Creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_projects INT;
    
    -- Calculate the total score and the total number of projects for the user
    SELECT SUM(score), COUNT(*) 
    INTO total_score, total_projects
    FROM corrections
    WHERE user_id = user_id;
    
    -- If the user has completed any projects, compute the average score
    IF total_projects > 0 THEN
        UPDATE users 
        SET average_score = total_score / total_projects
        WHERE id = user_id;
    ELSE
        -- If no projects, set average score to 0
        UPDATE users 
        SET average_score = 0
        WHERE id = user_id;
    END IF;
END$$

DELIMITER ;
