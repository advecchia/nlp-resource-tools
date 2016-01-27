SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

DROP SCHEMA IF EXISTS `mestrado` ;
CREATE SCHEMA IF NOT EXISTS `mestrado` DEFAULT CHARACTER SET utf8 ;
USE `mestrado` ;

-- -----------------------------------------------------
-- Table `mestrado`.`languages`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mestrado`.`languages` ;

CREATE TABLE IF NOT EXISTS `mestrado`.`languages` (
  `id` INT UNSIGNED NOT NULL,
  `acronym` VARCHAR(10) NOT NULL,
  `title` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
COMMENT = 'Keep the list of supported languages.';


-- -----------------------------------------------------
-- Table `mestrado`.`files`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mestrado`.`files` ;

CREATE TABLE IF NOT EXISTS `mestrado`.`files` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `parallel_file_id` INT UNSIGNED DEFAULT NULL,
  `name` VARCHAR(150) NOT NULL,
  `size` INT UNSIGNED NOT NULL,
  `modified` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `language_id` INT UNSIGNED NULL,
  PRIMARY KEY (`id`),
  KEY `fk_parallel_file_id` (`parallel_file_id`),
  CONSTRAINT `fk_parallel_file_id`
    FOREIGN KEY (`parallel_file_id`)
    REFERENCES `mestrado`.`files` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  KEY `fk_language_id` (`language_id`),
  CONSTRAINT `fk_language_id`
    FOREIGN KEY (`language_id`)
    REFERENCES `mestrado`.`languages` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Keep the saved files.';

CREATE UNIQUE INDEX `NAME_UNIQUE` ON `mestrado`.`files` (`name` ASC);

CREATE INDEX `FK_PARALLEL_FILE_ID_IDX` ON `mestrado`.`files` (`parallel_file_id` ASC);

CREATE INDEX `FK_LANGUAGE_ID_IDX` ON `mestrado`.`files` (`language_id` ASC);


-- -----------------------------------------------------
-- Table `mestrado`.`paragraphs`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mestrado`.`paragraphs` ;

CREATE TABLE IF NOT EXISTS `mestrado`.`paragraphs` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `file_id` INT UNSIGNED NOT NULL,
  `order_in_file` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_file_id`
    FOREIGN KEY (`file_id`)
    REFERENCES `mestrado`.`files` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Keep the paragraphs contained in the files.';

CREATE INDEX `FK_FILE_ID_IDX` ON `mestrado`.`paragraphs` (`file_id` ASC);


-- -----------------------------------------------------
-- Table `mestrado`.`sentences`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mestrado`.`sentences` ;

CREATE TABLE IF NOT EXISTS `mestrado`.`sentences` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `paragraph_id` BIGINT UNSIGNED NOT NULL,
  `number_of_words` SMALLINT UNSIGNED NOT NULL,
  `order_in_paragraph` SMALLINT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_paragraph_id`
    FOREIGN KEY (`paragraph_id`)
    REFERENCES `mestrado`.`paragraphs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Keep the sentences contained in the paragraphs.';

CREATE INDEX `FK_PARAGRAPH_ID_IDX` ON `mestrado`.`sentences` (`paragraph_id` ASC);


-- -----------------------------------------------------
-- Table `mestrado`.`part_of_speech`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mestrado`.`part_of_speech` ;

CREATE TABLE IF NOT EXISTS `mestrado`.`part_of_speech` (
  `id` INT UNSIGNED NOT NULL,
  `acronym` VARCHAR(10) NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  `language_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_language_id2` (`language_id`),
  CONSTRAINT `fk_language_id2`
    FOREIGN KEY (`language_id`)
    REFERENCES `mestrado`.`languages` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Keep the list of part of speech available for each language.';

CREATE INDEX `FK_LANGUAGE_ID_IDX2` ON `mestrado`.`part_of_speech` (`language_id` ASC);


-- -----------------------------------------------------
-- Table `mestrado`.`lemmas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mestrado`.`lemmas` ;

CREATE TABLE IF NOT EXISTS `mestrado`.`lemmas` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `lemma` TINYTEXT NOT NULL,
  `pos_id` INT UNSIGNED NOT NULL,
  `syllables` TINYTEXT NOT NULL,
  `length` TINYINT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_pos_id`
    FOREIGN KEY (`pos_id`)
    REFERENCES `mestrado`.`part_of_speech` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Keep the unique representation of each lemma.';

CREATE INDEX `FK_POS_ID_IDX` ON `mestrado`.`lemmas` (`pos_id` ASC);


-- -----------------------------------------------------
-- Table `mestrado`.`tokens`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mestrado`.`tokens` ;

CREATE TABLE IF NOT EXISTS `mestrado`.`tokens` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `token` TINYTEXT NOT NULL,
  `lemma_id` BIGINT UNSIGNED NOT NULL,
  `pos_id` INT UNSIGNED NOT NULL,
  `syllabes` TINYTEXT NOT NULL,
  `length` TINYINT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_lemma_id`
    FOREIGN KEY (`lemma_id`)
    REFERENCES `mestrado`.`lemmas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  KEY `fk_pos_id2` (`pos_id`),
  CONSTRAINT `fk_pos_id2`
    FOREIGN KEY (`pos_id`)
    REFERENCES `mestrado`.`part_of_speech` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Keep the unique representation of each different token.';

CREATE INDEX `FK_LEMMA_ID_IDX` ON `mestrado`.`tokens` (`lemma_id` ASC);

CREATE INDEX `FK_POS_ID_IDX2` ON `mestrado`.`tokens` (`pos_id` ASC);


-- -----------------------------------------------------
-- Table `mestrado`.`tokens_per_sentence`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mestrado`.`tokens_per_sentence` ;

CREATE TABLE IF NOT EXISTS `mestrado`.`tokens_per_sentence` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `sentence_id` BIGINT UNSIGNED NOT NULL,
  `token_id` BIGINT UNSIGNED NOT NULL,
  `order_in_sentence` SMALLINT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_sentence_id`
    FOREIGN KEY (`sentence_id`)
    REFERENCES `mestrado`.`sentences` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_token_id`
    FOREIGN KEY (`token_id`)
    REFERENCES `mestrado`.`tokens` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Keep the tokens contained in the sentences.';

CREATE INDEX `FK_SENTENCE_ID_IDX` ON `mestrado`.`tokens_per_sentence` (`sentence_id` ASC);

CREATE INDEX `FK_TOKEN_ID_IDX` ON `mestrado`.`tokens_per_sentence` (`token_id` ASC);


-- -----------------------------------------------------
-- Table `mestrado`.`senses`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mestrado`.`senses` ;

CREATE TABLE IF NOT EXISTS `mestrado`.`senses` (
  `token_id` BIGINT UNSIGNED NOT NULL,
  `related_token_id` BIGINT UNSIGNED NOT NULL,
  `sense_type` SET('SYNONYMY', 'ANTONYMY', 'HYPERNYMY', 'HYPONYMY', 'HOLONYNY', 'MERONYMY') NOT NULL,
  PRIMARY KEY (`token_id`, `related_token_id`),
  KEY `fk_token_id2` (`token_id`),
  CONSTRAINT `fk_token_id2`
    FOREIGN KEY (`token_id`)
    REFERENCES `mestrado`.`tokens` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_related_token_id`
    FOREIGN KEY (`related_token_id`)
    REFERENCES `mestrado`.`tokens` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Contains the semantic relation for tokens.';

CREATE INDEX `FK_RELATED_TOKEN_ID_IDX` ON `mestrado`.`senses` (`related_token_id` ASC);


-- -----------------------------------------------------
-- Table `mestrado`.`tokens_per_file`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mestrado`.`tokens_per_file` ;

CREATE TABLE IF NOT EXISTS `mestrado`.`tokens_per_file` (
  `file_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `token_id` BIGINT UNSIGNED NOT NULL,
  `count` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`file_id`, `token_id`),
  KEY `fk_file_id2` (`file_id`),
  CONSTRAINT `fk_file_id2`
    FOREIGN KEY (`file_id`)
    REFERENCES `mestrado`.`files` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  KEY `fk_token_id3` (`token_id`),
  CONSTRAINT `fk_token_id3`
    FOREIGN KEY (`token_id`)
    REFERENCES `mestrado`.`tokens` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Keep the statistics of tokens contained in each file.';

CREATE INDEX `FK_TOKEN_ID_IDX2` ON `mestrado`.`tokens_per_file` (`token_id` ASC);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
