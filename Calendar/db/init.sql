CREATE DATABASE calendar;
use calendar;


CREATE TABLE IF NOT EXISTS  events (
  `id` INT AUTO_INCREMENT,
  `title` VARCHAR (255) NOT NULL,
  `url` VARCHAR( 255) NOT NULL,
  `class` VARCHAR (255) NOT NULL,
  `start_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `end_date` timestamp NOT NULL,
  PRIMARY KEY (`id`)
)

ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

insert  into `events`(`id`,`title`,`class`,`start_date`,`end_date`) values
(1,'Example','event-success','2020-08-10 20:00:00','2020-08-10 20:01:02'),
(2,'Roy Tutorials','event-important','2020-08-15 19:00:00','2020-08-15 19:42:45'),
(3,'Roy Tutorial','event-info','2020-08-23 20:03:05','2020-08-24 08:45:53'),
(4,'Roy Tutorial','event-error','2020-08-24 20:03:05','2020-08-25 08:45:53');