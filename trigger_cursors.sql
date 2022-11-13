-- Creating a trigger to calculate age of a user whenever a new record/row is added

CREATE trigger user_age
before insert
on users
for each row
set NEW.age = DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), NEW.DOB)), '%Y') + 0;

-- creating a cursor to count the number of friends for a user in the user table

$$ DELIMITER
CREATE PROCEDURE for_cursors() 
BEGIN
DECLARE user_ INT; 
DECLARE no_of_friends INT; 
DECLARE done INT DEFAULT 0; 
DECLARE friends_cursor CURSOR FOR SELECT User_ID FROM users; 
DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1; 
OPEN friends_cursor; 
myloop: LOOP 
FETCH friends_cursor into user_; 
IF done = 1 THEN LEAVE myloop; 
END IF; 
Set no_of_friends = ( Select Count(*) From friends WHERE User_ID = user_ ); 
UPDATE users SET number_of_friends = no_of_friends WHERE User_ID = user_; 
END LOOP; 
CLOSE friends_cursor; 
END;
$$ DELIMITER ;

