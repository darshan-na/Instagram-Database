--  function to count the number of posts a user has

DELIMITER $$
CREATE FUNCTION no_of_posts(user_id INT)
returns INT
DETERMINISTIC
BEGIN
	Declare number_of_posts INT;
	set number_of_posts = (Select count(*) from posts where Posted_User_ID=user_id);
	return number_of_posts;
END 
$$
DELIMITER ;

--  stored procedure to calculate the number of likes for a given post

DELIMITER $$
CREATE procedure no_of_post_likes(IN post_id INT)
BEGIN
	SELECT count(*) from post_likes where Post_ID=post_id;
END
$$ DELIMITER ;

-- procedure to count the number of friends for all the users
DELIMITER &&
CREATE PROCEDURE `number_of_friends`()
BEGIN
 SELECT User_ID,COUNT(DISTINCT Friend_ID)
 FROM Friends
 GROUP BY User_ID;
END
&& DELIMITER ;