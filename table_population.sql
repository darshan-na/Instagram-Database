-- populating the users table

insert into users (Email_ID,Phone_Number,Pass_word,First_name,Last_name,City,PinCode,DOB,Gender) values ('darshan@yahoo.com','7852323352','admin','Darshan','NA','Bengaluru',560070,DATE '2002-05-12','M');
insert into users (Email_ID,Phone_Number,Pass_word,First_name,Last_name,City,PinCode,DOB,Gender) values ('ankit@gmail.com','9561443640','xyz','ankith','nadgir','Nizampet',789563,DATE '1992-04-25','M');
insert into users (Email_ID,Phone_Number,Pass_word,First_name,Last_name,City,PinCode,DOB,Gender) values ('akash@gmail.com','9522115365','abc','Akash','Kiran','Hydrabad',750050,DATE '2002-09-23','M');
insert into users (Email_ID,Phone_Number,Pass_word,First_name,Last_name,City,PinCode,DOB,Gender) values ('amruth@gmail.com','9523663259','xyz','Amruth','S','Dharwad',45620,DATE '2005-02-28','M');
insert into users (Email_ID,Phone_Number,Pass_word,First_name,Last_name,City,PinCode,DOB,Gender) values ('ankur@gmail.com','9456355879','uvw','Ankur','D','Mysore',562305,DATE '1999-10-14','M');
insert into users (Email_ID,Phone_Number,Pass_word,First_name,Last_name,City,PinCode,DOB,Gender) values ('arna@gmail.com','9874563210','ijk','Angle','Arna','Vizag',23640,DATE '1999-10-14','F');

-- populating friends table

insert into friends values(1,6);
insert into friends values(1,2);
insert into friends values(1,5);
insert into friends values(1,4);
insert into friends values(2,3);
insert into friends values(4,3);
insert into friends values(6,3);
insert into friends values(6,5);

-- populating the page table

insert into pages(Page_user_id,Page_bio,Page_Content_no_followers_n_following) values(1,"Never_settle","360_400");
insert into pages(Page_user_id,Page_bio,Page_Content_no_followers_n_following) values(2,"wish me on 04/25","200_900");
insert into pages(Page_user_id,Page_bio,Page_Content_no_followers_n_following) values(3,"great_things_take_time","700_800");
insert into pages(Page_user_id,Page_bio,Page_Content_no_followers_n_following) values(4,"work in shuuussshh let ur success make noise","850_1");
insert into pages(Page_user_id,Page_bio,Page_Content_no_followers_n_following) values(5,"Nerd","100_50");
insert into pages(Page_user_id,Page_bio,Page_Content_no_followers_n_following) values(1,"glitter","2050_450");

-- populating posts table

insert into posts(Posted_User_ID,Post_Date,Post_Content) values(1,DATE '2020-10-20','SOME scenary image');
insert into posts(Posted_User_ID,Post_Date,Post_Content) values(3,DATE '2021-01-19','my first image');
insert into posts(Posted_User_ID,Post_Date,Post_Content) values(4,DATE '2022-04-06','image');
insert into posts(Posted_User_ID,Post_Date,Post_Content) values(5,DATE '2017-06-22','blank_image');
insert into posts(Posted_User_ID,Post_Date,Post_Content) values(6,DATE '2016-05-23','ethnic_day image');
insert into posts(Posted_User_ID,Post_Date,Post_Content) values(3,DATE '2015-04-24','meme');
insert into posts(Posted_User_ID,Post_Date,Post_Content) values(5,DATE '2014-03-25','image');
insert into posts(Posted_User_ID,Post_Date,Post_Content) values(2,DATE '2020-02-26','news/facts image');

-- populating post_like table

insert into post_likes values(1,3);
insert into post_likes values(2,6);
insert into post_likes values(3,2);
insert into post_likes values(4,1);
insert into post_likes values(5,4);
insert into post_likes values(6,1);
insert into post_likes values(1,4);
insert into post_likes values(2,5);

-- populating post_shares table

insert into shared_posts values(1,4);
insert into shared_posts values(5,1);
insert into shared_posts values(4,2);
insert into shared_posts values(4,3);
insert into shared_posts values(5,2);
insert into shared_posts values(5,6);
insert into shared_posts values(6,3);
insert into shared_posts values(6,4);

-- populating post_comments table

insert into post_comments(Post_id,Commented_Date,Comment_Content,Commented_User_ID) values(1,DATE '2020-11-14','Beautiful ',3); 
insert into post_comments(Post_id,Commented_Date,Comment_Content,Commented_User_ID) values(3,DATE '2022-06-23','heroooo ',4); 
insert into post_comments(Post_id,Commented_Date,Comment_Content,Commented_User_ID) values(2,DATE '2021-01-19','nice .. ',5); 
insert into post_comments(Post_id,Commented_Date,Comment_Content,Commented_User_ID) values(4,DATE '2017-08-11','wahhh .. ',2);
insert into post_comments(Post_id,Commented_Date,Comment_Content,Commented_User_ID) values(5,DATE '2017-06-15','superrrr .. ',3);
insert into post_comments(Post_id,Commented_Date,Comment_Content,Commented_User_ID) values(3,DATE '2022-07-21','studd boi .. ',1);
insert into post_comments(Post_id,Commented_Date,Comment_Content,Commented_User_ID) values(6,DATE '2020-02-26','informative..',1);
insert into post_comments(Post_id,Commented_Date,Comment_Content,Commented_User_ID) values(8,DATE '2020-02-28','its fake .. ',4);

-- populating comments_like table

insert into comment_likes values(1,2);
insert into comment_likes values(4,3);
insert into comment_likes values(5,1);
insert into comment_likes values(7,2);
insert into comment_likes values(1,6);
insert into comment_likes values(8,5);
insert into comment_likes values(5,6);
insert into comment_likes values(2,3);
insert into comment_likes values(3,2);