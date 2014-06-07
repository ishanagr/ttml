PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users (
	id INTEGER NOT NULL, 
	name VARCHAR, 
	facebook_id INTEGER, 
	profile_pic VARCHAR, 
	PRIMARY KEY (id)
);
INSERT INTO "users" VALUES(1,'Neerav Kumar',591446731,'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xpf1/t1.0-1/c13.13.168.168/s50x50/23538_365574856731_312082_n.jpg');
INSERT INTO "users" VALUES(2,'Ishan Agrawal',1313695165,'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfp1/t1.0-1/c0.0.50.50/p50x50/1978616_10203758246819337_91578058_t.jpg');
CREATE TABLE attends (
	id INTEGER NOT NULL, 
	event_id INTEGER, 
	user_id INTEGER, 
	PRIMARY KEY (id)
);
INSERT INTO "attends" VALUES(1,1,2);
INSERT INTO "attends" VALUES(2,1,2);
CREATE TABLE categories (
	id INTEGER NOT NULL, 
	title VARCHAR, 
	image VARCHAR, 
	PRIMARY KEY (id)
);
INSERT INTO "categories" VALUES(1,'Games','https://lh6.googleusercontent.com/RFJYAGRgOZ6oWOPNz0dBlwh1SfUJvE7U_RxYqYxEy-37sXjjDfXqRXKlyknKUXRWcjOcUQ=w2336-h900');
INSERT INTO "categories" VALUES(2,'Dessert','https://lh3.googleusercontent.com/hPPHoqeGmvhTGYSBwzVwPjFhZ1hxwK94yZN8W8xGlmKrRCEpgHrc1yBW0KNTdXPtAS-C3g=w2336-h900');
INSERT INTO "categories" VALUES(3,'Learning','https://lh4.googleusercontent.com/mCbuCKjYppLXmcTmvAdbzUfxjpbhcl44czuJCmgUhiPCVQ79lU5QmUxcbUyS8dIzSLYoQGNgk20');
CREATE TABLE events (
	id INTEGER NOT NULL, 
	activity VARCHAR, 
	start_time DATETIME, 
	end_time DATETIME, 
	latitude FLOAT, 
	longitude FLOAT, 
	description VARCHAR, 
	category_id INTEGER, 
	address VARCHAR, 
	privacy VARCHAR, 
	n_people INTEGER, 
	host_name INTEGER, 
	tags VARCHAR, 
	PRIMARY KEY (id)
);
INSERT INTO "events" VALUES(1,'Chess Roulette!','2014-06-19 14:25:16.000000','2014-06-17 17:25:16.000000',1.2931,103.8558,'Beat me at Chess or die trying!',1,'59, Mohamed Sultan Road','Public',2,1,'chess, game, challenge');
COMMIT;
