-- ----------------------------
-- Table structure for admin_login_k
-- ----------------------------
DROP TABLE IF EXISTS admin_login_k;
CREATE TABLE admin_login_k (
  admin_id varchar(20) NOT NULL,
  admin_pass varchar(20) DEFAULT NULL,
  PRIMARY KEY (admin_id)
);
 
-- ----------------------------
-- Records of admin_login_k
-- ----------------------------
INSERT INTO admin_login_k VALUES ('admin', 'admin');

-- ----------------------------
-- Table structure for student_k
-- ----------------------------
DROP TABLE IF EXISTS student_k;
CREATE TABLE student_k (
  student_id varchar(20) NOT NULL,
  name varchar(20) DEFAULT NULL,
  gender varchar(5) DEFAULT NULL,
  age int DEFAULT NULL,
	PRIMARY KEY (student_id)
)
;

-- ----------------------------
-- Records of student_k
-- ----------------------------
INSERT INTO "public"."student_k" VALUES ('2023001', 'test1', 'M', 21);
INSERT INTO "public"."student_k" VALUES ('2023002', 'test2', 'M', 21);
INSERT INTO "public"."student_k" VALUES ('2023003', 'test3', 'F', 23);
INSERT INTO "public"."student_k" VALUES ('2023004', 'test4', 'F', 21);
INSERT INTO "public"."student_k" VALUES ('2023005', 'test5', 'F', 24);


-- ----------------------------
-- Table structure for student_login_k
-- ----------------------------
DROP TABLE IF EXISTS student_login_k;
CREATE TABLE student_login_k (
  id int NOT NULL GENERATED ALWAYS AS IDENTITY, 
  student_id varchar(20) NOT NULL,
  student_pass varchar(20) DEFAULT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (student_id) REFERENCES student_k(student_id) ON DELETE CASCADE ON UPDATE CASCADE
)
;

-- ----------------------------
-- Records of student_login_k
-- ----------------------------
INSERT INTO student_login_k(student_id, student_pass) VALUES ('2023001', '123456');
INSERT INTO student_login_k(student_id, student_pass) VALUES ('2023002', '123456');
INSERT INTO student_login_k(student_id, student_pass) VALUES ('2023003', '123456');
INSERT INTO student_login_k(student_id, student_pass) VALUES ('2023004', '123456');
INSERT INTO student_login_k(student_id, student_pass) VALUES ('2023005', '123456');

-- ----------------------------
-- Table structure for course_k
-- ----------------------------
DROP TABLE IF EXISTS course_k;
CREATE TABLE course_k (
  course_id varchar(20) NOT NULL,
  course_name varchar(20) DEFAULT NULL,
  credit float DEFAULT NULL,
	PRIMARY KEY (course_id)
)
;

-- ----------------------------
-- Records of course_k
-- ----------------------------
INSERT INTO course_k VALUES ('C01', 'Python', 4);
INSERT INTO course_k VALUES ('C02', 'Java', 3);
INSERT INTO course_k VALUES ('C03', 'C++', 4);
INSERT INTO course_k VALUES ('C04', 'C', 3);
INSERT INTO course_k VALUES ('C05', 'R', 2);


-- ----------------------------
-- Table structure for student_course_k
-- ----------------------------
DROP TABLE IF EXISTS student_course_k;
CREATE TABLE student_course_k (
	student_id varchar(20)  NOT NULL,
  course_id varchar(20) NOT NULL,
	PRIMARY KEY (student_id, course_id),
	FOREIGN KEY (student_id) REFERENCES student_k(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (course_id) REFERENCES course_k(course_id) ON DELETE CASCADE ON UPDATE CASCADE
)
;

-- ----------------------------
-- Records of student_course_k
-- ----------------------------
INSERT INTO student_course_k(course_id, student_id) VALUES ('C01', '2023001');
INSERT INTO student_course_k(course_id, student_id) VALUES ('C02', '2023001');
INSERT INTO student_course_k(course_id, student_id) VALUES ('C03', '2023001');
INSERT INTO student_course_k(course_id, student_id) VALUES ('C04', '2023001');
INSERT INTO student_course_k(course_id, student_id) VALUES ('C01', '2023002');
INSERT INTO student_course_k(course_id, student_id) VALUES ('C03', '2023002');
INSERT INTO student_course_k(course_id, student_id) VALUES ('C02', '2023003');
INSERT INTO student_course_k(course_id, student_id) VALUES ('C03', '2023003');
INSERT INTO student_course_k(course_id, student_id) VALUES ('C04', '2023003');
INSERT INTO student_course_k(course_id, student_id) VALUES ('C03', '2023004');
INSERT INTO student_course_k(course_id, student_id) VALUES ('C01', '2023004');
INSERT INTO student_course_k(course_id, student_id) VALUES ('C01', '2023005');
INSERT INTO student_course_k(course_id, student_id) VALUES ('C02', '2023005');

-- ----------------------------
-- Table structure for grade_k
-- ----------------------------
DROP TABLE IF EXISTS grade_k;
CREATE TABLE grade_k (
  id int NOT NULL GENERATED ALWAYS AS IDENTITY, 
  student_id varchar(20) NOT NULL,
  course_id varchar(20) NOT NULL,
  score int DEFAULT NULL,
  status varchar(20) DEFAULT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (student_id, course_id) REFERENCES student_course_k(student_id, course_id) ON DELETE CASCADE ON UPDATE CASCADE
)
;

-- ----------------------------
-- Records of grade_k
-- ----------------------------
INSERT INTO grade_k(student_id, course_id, score, status) VALUES ('2023001', 'C01', 90, 'Pass');
INSERT INTO grade_k(student_id, course_id, score, status) VALUES ('2023001', 'C02', 15, 'Not Pass');
INSERT INTO grade_k(student_id, course_id, score, status) VALUES ('2023001', 'C03', NULL, NULL);
INSERT INTO grade_k(student_id, course_id, score, status) VALUES ('2023001', 'C04', NULL, NULL);
INSERT INTO grade_k(student_id, course_id, score, status) VALUES ('2023002', 'C01', NULL, NULL);
INSERT INTO grade_k(student_id, course_id, score, status) VALUES ('2023002', 'C03', NULL, NULL);
INSERT INTO grade_k(student_id, course_id, score, status) VALUES ('2023003', 'C02', NULL, NULL);
INSERT INTO grade_k(student_id, course_id, score, status) VALUES ('2023003', 'C03', NULL, NULL);
INSERT INTO grade_k(student_id, course_id, score, status) VALUES ('2023003', 'C04', NULL, NULL);
INSERT INTO grade_k(student_id, course_id, score, status) VALUES ('2023004', 'C03', NULL, NULL);
INSERT INTO grade_k(student_id, course_id, score, status) VALUES ('2023004', 'C01', NULL, NULL);
INSERT INTO grade_k(student_id, course_id, score, status) VALUES ('2023005', 'C01', NULL, NULL);
INSERT INTO grade_k(student_id, course_id, score, status) VALUES ('2023005', 'C02', NULL, NULL);


