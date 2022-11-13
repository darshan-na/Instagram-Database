--  creating users table
--  auto_increment is a fetaure which generates a unique integer which is often used a primary key
CREATE TABLE users(
  User_ID INT NOT NULL auto_increment,
  Email_ID VARCHAR(25) NOT NULL,
  Phone_Number CHAR(10) NOT NULL,
  Pass_word VARCHAR(20) NOT NULL,
  First_name VARCHAR(20) NOT NULL,
  Last_name VARCHAR(20),
  City VARCHAR(20),
  PinCode INT,
  DOB DATE NOT NULL,
  Gender CHAR(10),
  PRIMARY KEY(User_ID)
);s

-- creating posts table 

CREATE TABLE posts(
   Post_ID INT NOT NULL auto_increment,
   Posted_User_ID INT NOT NULL,
   Post_Date DATE NOT NULL,
   Post_Content VARCHAR(50) NOT NULL,
   CONSTRAINT user_posted_refcons FOREIGN KEY (Posted_User_ID) references users(User_ID) on delete cascade,
   PRIMARY KEY(Post_ID)
);

-- creating table shared_posts table

CREATE TABLE shared_posts(
  Post_ID INT NOT NULL,
  Shared_User_ID INT NOT NULL,
  PRIMARY KEY(Post_ID,Shared_User_ID),
  CONSTRAINT Shared_Post_ID_refcons FOREIGN KEY (Post_ID) references posts(Post_ID) on delete cascade,  -- if the user deletes the post then all the users who have shared the posts should also be notified in other words the post shd be made unavailable
  CONSTRAINT Shared_User_ID_refcons FOREIGN KEY (Shared_User_ID) references users(User_ID) on delete cascade -- if the user itself is deleted then all his posts get deleted then all the users who have those posts shd be notified
);

-- creating liked_posts table 

CREATE TABLE post_likes(
  Post_ID INT NOT NULL,
  Liked_User_ID INT NOT NULL,
  PRIMARY KEY(Post_ID,Liked_User_ID),
  CONSTRAINT Liked_Post_ID_refcons FOREIGN KEY (Post_ID) references posts(Post_ID) on delete cascade,
  CONSTRAINT liked_User_ID_refcons FOREIGN KEY (Liked_User_ID) references users(User_ID) on delete cascade
);

-- creating Posts_comments table

CREATE TABLE post_comments(
  Comment_ID INT NOT NULL auto_increment,
  Post_ID INT NOT NULL,
  Commented_Date DATE,
  Comment_Content VARCHAR(50),
  Commented_User_ID INT NOT NULL,
  PRIMARY KEY(Comment_ID),
  CONSTRAINT Commented_Post_ID_refcons FOREIGN KEY (Post_ID) references posts(Post_ID) on delete cascade,
  CONSTRAINT Commented_User_ID_refcons FOREIGN KEY (Commented_User_ID) references users(User_ID) on delete cascade
);

-- creating liked_comments table

CREATE TABLE comment_likes(
  Comment_ID INT NOT NULL,
  Comment_liked_User_ID INT NOT NULL,
  PRIMARY KEY (Comment_ID,Comment_liked_User_ID),
  CONSTRAINT Comment_ID_refcons FOREIGN KEY (Comment_ID) references post_comments(Comment_ID) on delete cascade,
  CONSTRAINT Comment_liked_user_ID_refcons FOREIGN KEY (Comment_liked_User_ID) references users(User_ID) on delete cascade
);

-- creating page table

CREATE TABLE pages(
   Page_ID INT NOT NULL auto_increment,
   Page_user_id INT NOT NULL,
   Page_bio VARCHAR(20) NOT NULL,
   Page_Content_no_followers_n_following VARCHAR(50) NOT NULL,
   PRIMARY KEY(Page_ID),
   CONSTRAINT Page_user_id_refcons FOREIGN KEY(Page_user_id) references users(User_ID) on delete cascade
);

-- creating friend or followers table

CREATE TABLE friends(
   User_ID INT NOT NULL,
   Friend_ID INT NOT NULL,
   PRIMARY KEY(User_ID,Friend_ID),
   CONSTRAINT User_ID_refcons FOREIGN KEY (User_ID) references users(User_ID) on delete cascade on update cascade,
   CONSTRAINT Friend_ID_refcons FOREIGN KEY (Friend_ID) references users(User_ID) on delete cascade
);


