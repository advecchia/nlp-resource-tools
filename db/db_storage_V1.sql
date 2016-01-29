CREATE TABLE IF NOT EXISTS `mestrado`.`files` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `parallel_file_id` INT UNSIGNED NOT NULL,
  `name` VARCHAR(150) NOT NULL,
  `size` INT NOT NULL,
  `modified` TIMESTAMP NOT NULL,
  `language` VARCHAR(25) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `NAME_UNIQUE` (`name` ASC),
  INDEX `FK_PARALLEL_FILE_ID_IDX` (`parallel_file_id` ASC),
  CONSTRAINT `fk_parallel_file_id`
    FOREIGN KEY (`parallel_file_id`)
    REFERENCES `mestrado`.`files` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mestrado`.`paragraphs` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `order_in_file` INT UNSIGNED NOT NULL,
  `file_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `FK_FILE_ID_IDX` (`file_id` ASC),
  CONSTRAINT `fk_file_id`
    FOREIGN KEY (`file_id`)
    REFERENCES `mestrado`.`files` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mestrado`.`sentences` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `paragraph_id` INT UNSIGNED NOT NULL,
  `number_of_words` SMALLINT UNSIGNED NOT NULL,
  `order_in_paragraph` SMALLINT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `FK_PARAGRAPH_ID_IDX` (`paragraph_id` ASC),
  CONSTRAINT `fk_paragraph_id`
    FOREIGN KEY (`paragraph_id`)
    REFERENCES `mestrado`.`paragraphs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mestrado`.`tokens` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `sentence_id` INT UNSIGNED NOT NULL,
  `token` TINYTEXT NOT NULL,
  `lemma` TINYTEXT NOT NULL,
  `pos` VARCHAR(10) NOT NULL,
  `syllables` TINYTEXT NOT NULL,
  `order_in_sentence` SMALLINT UNSIGNED NOT NULL,
  `tf_idf` FLOAT NULL,
  `length` TINYINT UNSIGNED NOT NULL,
  `synonyms` TEXT NULL,
  PRIMARY KEY (`id`),
  INDEX `FK_SENTENCE_ID_IDX` (`sentence_id` ASC),
  CONSTRAINT `fk_sentence_id`
    FOREIGN KEY (`sentence_id`)
    REFERENCES `mestrado`.`sentences` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;