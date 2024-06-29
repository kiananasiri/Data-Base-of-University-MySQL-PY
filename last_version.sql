-- MySQL Script generated by MySQL Workbench
-- Sat Jun 29 13:54:06 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`DEPARTMENT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`DEPARTMENT` (
  `DEP_ID` INT NOT NULL,
  `DEP_NAME` VARCHAR(30) NOT NULL,
  `DEP_ADDR` VARCHAR(45) NULL,
  PRIMARY KEY (`DEP_ID`),
  UNIQUE INDEX `DEP_ID_UNIQUE` (`DEP_ID` ASC) VISIBLE,
  UNIQUE INDEX `DEP_NAME_UNIQUE` (`DEP_NAME` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`FACULTY_EMPLOYEE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`FACULTY_EMPLOYEE` (
  `EMID` INT NOT NULL,
  `NAME` VARCHAR(60) NOT NULL,
  `DEPARTMENT_DEP_ID` INT NOT NULL,
  PRIMARY KEY (`EMID`),
  UNIQUE INDEX `EMID_UNIQUE` (`EMID` ASC) VISIBLE,
  INDEX `fk_FACULTY_EMPLOYEE_DEPARTMENT1_idx` (`DEPARTMENT_DEP_ID` ASC) VISIBLE,
  CONSTRAINT `fk_FACULTY_EMPLOYEE_DEPARTMENT1`
    FOREIGN KEY (`DEPARTMENT_DEP_ID`)
    REFERENCES `mydb`.`DEPARTMENT` (`DEP_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`PERSON 2`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`PERSON 2` (
  `NAME` VARCHAR(60) NOT NULL,
  `NSI` INT NOT NULL,
  `SEX` VARCHAR(6) NOT NULL,
  `DOB` DATE NOT NULL,
  `POB` VARCHAR(60) NOT NULL,
  `NOF` VARCHAR(45) NOT NULL,
  `GREGION` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`NSI`),
  UNIQUE INDEX `NSI_UNIQUE` (`NSI` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`PERSON`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`PERSON` (
  `APP_ID` INT NOT NULL,
  `ADDR.` VARCHAR(80) NOT NULL,
  `PHONE` INT NOT NULL,
  `EMAIL` VARCHAR(320) NOT NULL,
  `PERSON 2_NSI` INT NOT NULL,
  PRIMARY KEY (`APP_ID`),
  UNIQUE INDEX `APP_ID_UNIQUE` (`APP_ID` ASC) VISIBLE,
  INDEX `fk_PERSON_PERSON 21_idx` (`PERSON 2_NSI` ASC) VISIBLE,
  CONSTRAINT `fk_PERSON_PERSON 21`
    FOREIGN KEY (`PERSON 2_NSI`)
    REFERENCES `mydb`.`PERSON 2` (`NSI`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ENROLLMENT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ENROLLMENT` (
  `STID` INT NOT NULL,
  `DEPARTMENT_DEP_ID` INT NOT NULL,
  `FACULTY_EMPLOYEE_EMID` INT NOT NULL,
  `DATE` DATE NOT NULL,
  `PERSON_APP_ID` INT NOT NULL,
  PRIMARY KEY (`STID`, `DEPARTMENT_DEP_ID`, `FACULTY_EMPLOYEE_EMID`, `PERSON_APP_ID`),
  INDEX `fk_ENROLLMENT_DEPARTMENT1_idx` (`DEPARTMENT_DEP_ID` ASC) VISIBLE,
  INDEX `fk_ENROLLMENT_FACULTY_EMPLOYEE1_idx` (`FACULTY_EMPLOYEE_EMID` ASC) VISIBLE,
  UNIQUE INDEX `STID_UNIQUE` (`STID` ASC) VISIBLE,
  INDEX `fk_ENROLLMENT_PERSON1_idx` (`PERSON_APP_ID` ASC) VISIBLE,
  CONSTRAINT `fk_ENROLLMENT_DEPARTMENT1`
    FOREIGN KEY (`DEPARTMENT_DEP_ID`)
    REFERENCES `mydb`.`DEPARTMENT` (`DEP_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ENROLLMENT_FACULTY_EMPLOYEE1`
    FOREIGN KEY (`FACULTY_EMPLOYEE_EMID`)
    REFERENCES `mydb`.`FACULTY_EMPLOYEE` (`EMID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ENROLLMENT_PERSON1`
    FOREIGN KEY (`PERSON_APP_ID`)
    REFERENCES `mydb`.`PERSON` (`APP_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`STUDENT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`STUDENT` (
  `ENROLLMENT_STID` INT NOT NULL,
  `NAME` VARCHAR(60) NOT NULL,
  `MAJOR` VARCHAR(25) NOT NULL,
  `TOT_CRED` INT NOT NULL,
  `LEVEL` VARCHAR(4) NOT NULL,
  PRIMARY KEY (`ENROLLMENT_STID`),
  INDEX `fk_STUDENT_ENROLLMENT1_idx` (`ENROLLMENT_STID` ASC) VISIBLE,
  UNIQUE INDEX `ENROLLMENT_STID_UNIQUE` (`ENROLLMENT_STID` ASC) VISIBLE,
  CONSTRAINT `fk_STUDENT_ENROLLMENT1`
    FOREIGN KEY (`ENROLLMENT_STID`)
    REFERENCES `mydb`.`ENROLLMENT` (`STID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`PROFESSOR`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`PROFESSOR` (
  `PROF_ID` INT NOT NULL,
  `NAME` VARCHAR(60) NOT NULL,
  `SALARY` INT NOT NULL,
  `DEPARTMENT_DEP_ID` INT NOT NULL,
  `PHONE_NO` INT NOT NULL,
  `BA'S` VARCHAR(45) NULL,
  `MA'S` VARCHAR(45) NULL,
  `PHD` VARCHAR(45) NULL,
  PRIMARY KEY (`PROF_ID`),
  UNIQUE INDEX `PROF_ID_UNIQUE` (`PROF_ID` ASC) VISIBLE,
  INDEX `fk_PROFESSOR_DEPARTMENT1_idx` (`DEPARTMENT_DEP_ID` ASC) VISIBLE,
  CONSTRAINT `fk_PROFESSOR_DEPARTMENT1`
    FOREIGN KEY (`DEPARTMENT_DEP_ID`)
    REFERENCES `mydb`.`DEPARTMENT` (`DEP_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`COURSE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`COURSE` (
  `COID` INT NOT NULL,
  `TITLE` VARCHAR(45) NOT NULL,
  `CREDIT` TINYINT NOT NULL,
  `DEPARTMENT_DEP_ID` INT NOT NULL,
  UNIQUE INDEX `COID_UNIQUE` (`COID` ASC) VISIBLE,
  PRIMARY KEY (`COID`),
  INDEX `fk_COURSE_DEPARTMENT1_idx` (`DEPARTMENT_DEP_ID` ASC) VISIBLE,
  CONSTRAINT `fk_COURSE_DEPARTMENT1`
    FOREIGN KEY (`DEPARTMENT_DEP_ID`)
    REFERENCES `mydb`.`DEPARTMENT` (`DEP_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`PREREQUISITE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`PREREQUISITE` (
  `COID` INT NOT NULL,
  `PRECO_ID` INT NOT NULL,
  `PREREQUISITE_STAT` BINARY(1) NOT NULL,
  PRIMARY KEY (`COID`, `PRECO_ID`),
  INDEX `fk_COURSE_has_COURSE_COURSE2_idx` (`PRECO_ID` ASC) VISIBLE,
  INDEX `fk_COURSE_has_COURSE_COURSE1_idx` (`COID` ASC) VISIBLE,
  CONSTRAINT `fk_COURSE_has_COURSE_COURSE1`
    FOREIGN KEY (`COID`)
    REFERENCES `mydb`.`COURSE` (`COID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_COURSE_has_COURSE_COURSE2`
    FOREIGN KEY (`PRECO_ID`)
    REFERENCES `mydb`.`COURSE` (`COID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`LIBRARY`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`LIBRARY` (
  `LIBID` INT NOT NULL,
  `NAME` VARCHAR(45) NOT NULL,
  `DEPARTMENT_DEP_ID` INT NOT NULL,
  PRIMARY KEY (`LIBID`),
  UNIQUE INDEX `LIBID_UNIQUE` (`LIBID` ASC) VISIBLE,
  INDEX `fk_LIBRARY_DEPARTMENT1_idx` (`DEPARTMENT_DEP_ID` ASC) VISIBLE,
  CONSTRAINT `fk_LIBRARY_DEPARTMENT1`
    FOREIGN KEY (`DEPARTMENT_DEP_ID`)
    REFERENCES `mydb`.`DEPARTMENT` (`DEP_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`BOOK`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`BOOK` (
  `ISBN` INT NOT NULL,
  `NAME` VARCHAR(45) NOT NULL,
  `AUTHOR` VARCHAR(100) NOT NULL,
  `PUBLICATION` VARCHAR(45) NULL,
  `EDITION` TINYINT NULL,
  PRIMARY KEY (`ISBN`),
  UNIQUE INDEX `ISBN_UNIQUE` (`ISBN` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`SECTION`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`SECTION` (
  `SECID` INT NOT NULL,
  `PROFESSOR_PROF_ID` INT NOT NULL,
  `COURSE_COID` INT NOT NULL,
  `YEAR` YEAR NOT NULL,
  `SEMESTER` INT NOT NULL,
  `SCHEDULE` VARCHAR(45) NOT NULL,
  `EXAM_DATE` DATETIME NOT NULL,
  PRIMARY KEY (`SECID`),
  INDEX `fk_SECTION_PROFESSOR1_idx` (`PROFESSOR_PROF_ID` ASC) VISIBLE,
  INDEX `fk_SECTION_COURSE1_idx` (`COURSE_COID` ASC) VISIBLE,
  UNIQUE INDEX `SECID_UNIQUE` (`SECID` ASC) VISIBLE,
  CONSTRAINT `fk_SECTION_PROFESSOR1`
    FOREIGN KEY (`PROFESSOR_PROF_ID`)
    REFERENCES `mydb`.`PROFESSOR` (`PROF_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_SECTION_COURSE1`
    FOREIGN KEY (`COURSE_COID`)
    REFERENCES `mydb`.`COURSE` (`COID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`STSEC`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`STSEC` (
  `SECTION_SECID` INT NOT NULL,
  `STUDENT_ENROLLMENT_STID` INT NOT NULL,
  `DELETE_STAT` BINARY(1) NOT NULL DEFAULT 0,
  `GRADE` DECIMAL(2,2) NULL,
  PRIMARY KEY (`SECTION_SECID`, `STUDENT_ENROLLMENT_STID`),
  INDEX `fk_SECTION_has_STUDENT_STUDENT1_idx` (`STUDENT_ENROLLMENT_STID` ASC) VISIBLE,
  INDEX `fk_SECTION_has_STUDENT_SECTION1_idx` (`SECTION_SECID` ASC) VISIBLE,
  CONSTRAINT `fk_SECTION_has_STUDENT_SECTION1`
    FOREIGN KEY (`SECTION_SECID`)
    REFERENCES `mydb`.`SECTION` (`SECID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_SECTION_has_STUDENT_STUDENT1`
    FOREIGN KEY (`STUDENT_ENROLLMENT_STID`)
    REFERENCES `mydb`.`STUDENT` (`ENROLLMENT_STID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ATTENDANCE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ATTENDANCE` (
  `STSEC_SECTION_SECID` INT NOT NULL,
  `STSEC_STUDENT_ENROLLMENT_STID` INT NOT NULL,
  `DATE` DATE NOT NULL,
  `ATT` BINARY(1) NULL,
  PRIMARY KEY (`STSEC_SECTION_SECID`, `STSEC_STUDENT_ENROLLMENT_STID`, `DATE`),
  CONSTRAINT `fk_ATTENDANCE_STSEC1`
    FOREIGN KEY (`STSEC_SECTION_SECID` , `STSEC_STUDENT_ENROLLMENT_STID`)
    REFERENCES `mydb`.`STSEC` (`SECTION_SECID` , `STUDENT_ENROLLMENT_STID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`LIBRARY_has_BOOK`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`LIBRARY_has_BOOK` (
  `LIBRARY_LIBID` INT NOT NULL,
  `BOOK_ISBN` INT NOT NULL,
  `BOOKID` INT NOT NULL,
  PRIMARY KEY (`LIBRARY_LIBID`, `BOOK_ISBN`, `BOOKID`),
  INDEX `fk_LIBRARY_has_BOOK_BOOK1_idx` (`BOOK_ISBN` ASC) VISIBLE,
  INDEX `fk_LIBRARY_has_BOOK_LIBRARY1_idx` (`LIBRARY_LIBID` ASC) VISIBLE,
  UNIQUE INDEX `BOOKID_UNIQUE` (`BOOKID` ASC) VISIBLE,
  CONSTRAINT `fk_LIBRARY_has_BOOK_LIBRARY1`
    FOREIGN KEY (`LIBRARY_LIBID`)
    REFERENCES `mydb`.`LIBRARY` (`LIBID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_LIBRARY_has_BOOK_BOOK1`
    FOREIGN KEY (`BOOK_ISBN`)
    REFERENCES `mydb`.`BOOK` (`ISBN`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`BORROWS`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`BORROWS` (
  `STUDENT_ENROLLMENT_STID` INT NOT NULL,
  `LIBRARY_has_BOOK_BOOKID` INT NOT NULL,
  `TAKE_DATE` DATETIME NOT NULL,
  `RETURN_DATE` DATETIME NULL,
  PRIMARY KEY (`STUDENT_ENROLLMENT_STID`, `LIBRARY_has_BOOK_BOOKID`, `TAKE_DATE`),
  INDEX `fk_STUDENT_has_LIBRARY_has_BOOK_LIBRARY_has_BOOK1_idx` (`LIBRARY_has_BOOK_BOOKID` ASC) VISIBLE,
  INDEX `fk_STUDENT_has_LIBRARY_has_BOOK_STUDENT1_idx` (`STUDENT_ENROLLMENT_STID` ASC) VISIBLE,
  UNIQUE INDEX `STUDENT_ENROLLMENT_STID_UNIQUE` (`STUDENT_ENROLLMENT_STID` ASC) VISIBLE,
  UNIQUE INDEX `LIBRARY_has_BOOK_BOOKID_UNIQUE` (`LIBRARY_has_BOOK_BOOKID` ASC) VISIBLE,
  UNIQUE INDEX `TAKE_DATE_UNIQUE` (`TAKE_DATE` ASC) VISIBLE,
  CONSTRAINT `fk_STUDENT_has_LIBRARY_has_BOOK_STUDENT1`
    FOREIGN KEY (`STUDENT_ENROLLMENT_STID`)
    REFERENCES `mydb`.`STUDENT` (`ENROLLMENT_STID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_STUDENT_has_LIBRARY_has_BOOK_LIBRARY_has_BOOK1`
    FOREIGN KEY (`LIBRARY_has_BOOK_BOOKID`)
    REFERENCES `mydb`.`LIBRARY_has_BOOK` (`BOOKID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`P_BORROWS`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`P_BORROWS` (
  `PROFESSOR_PROF_ID` INT NOT NULL,
  `LIBRARY_has_BOOK_BOOKID` INT NOT NULL,
  `TAKE_DATE` DATETIME NOT NULL,
  `RETURN_DATE` DATETIME NULL,
  PRIMARY KEY (`PROFESSOR_PROF_ID`, `LIBRARY_has_BOOK_BOOKID`, `TAKE_DATE`),
  INDEX `fk_PROFESSOR_has_LIBRARY_has_BOOK_LIBRARY_has_BOOK1_idx` (`LIBRARY_has_BOOK_BOOKID` ASC) VISIBLE,
  INDEX `fk_PROFESSOR_has_LIBRARY_has_BOOK_PROFESSOR1_idx` (`PROFESSOR_PROF_ID` ASC) VISIBLE,
  CONSTRAINT `fk_PROFESSOR_has_LIBRARY_has_BOOK_PROFESSOR1`
    FOREIGN KEY (`PROFESSOR_PROF_ID`)
    REFERENCES `mydb`.`PROFESSOR` (`PROF_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_PROFESSOR_has_LIBRARY_has_BOOK_LIBRARY_has_BOOK1`
    FOREIGN KEY (`LIBRARY_has_BOOK_BOOKID`)
    REFERENCES `mydb`.`LIBRARY_has_BOOK` (`BOOKID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`SUGGESTS`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`SUGGESTS` (
  `SECTION_SECID` INT NOT NULL,
  `BOOK_ISBN` INT NOT NULL,
  PRIMARY KEY (`SECTION_SECID`, `BOOK_ISBN`),
  INDEX `fk_SECTION_has_BOOK_BOOK1_idx` (`BOOK_ISBN` ASC) VISIBLE,
  INDEX `fk_SECTION_has_BOOK_SECTION1_idx` (`SECTION_SECID` ASC) VISIBLE,
  CONSTRAINT `fk_SECTION_has_BOOK_SECTION1`
    FOREIGN KEY (`SECTION_SECID`)
    REFERENCES `mydb`.`SECTION` (`SECID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_SECTION_has_BOOK_BOOK1`
    FOREIGN KEY (`BOOK_ISBN`)
    REFERENCES `mydb`.`BOOK` (`ISBN`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`MANAGEMENT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`MANAGEMENT` (
  `DEPARTMENT_DEP_ID` INT NOT NULL,
  `PROFESSOR_PROF_ID` INT NOT NULL,
  `STARTING_DATE` DATE NOT NULL,
  `ENDING_DATE` DATE NULL,
  PRIMARY KEY (`DEPARTMENT_DEP_ID`, `PROFESSOR_PROF_ID`, `STARTING_DATE`),
  INDEX `fk_DEPARTMENT_has_PROFESSOR_PROFESSOR1_idx` (`PROFESSOR_PROF_ID` ASC) VISIBLE,
  INDEX `fk_DEPARTMENT_has_PROFESSOR_DEPARTMENT1_idx` (`DEPARTMENT_DEP_ID` ASC) VISIBLE,
  CONSTRAINT `fk_DEPARTMENT_has_PROFESSOR_DEPARTMENT1`
    FOREIGN KEY (`DEPARTMENT_DEP_ID`)
    REFERENCES `mydb`.`DEPARTMENT` (`DEP_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_DEPARTMENT_has_PROFESSOR_PROFESSOR1`
    FOREIGN KEY (`PROFESSOR_PROF_ID`)
    REFERENCES `mydb`.`PROFESSOR` (`PROF_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
