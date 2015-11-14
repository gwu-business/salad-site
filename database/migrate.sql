/* MIGRATE SALAD DATABASE */

CREATE TABLE `menu_items` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `category` varchar(255) NOT NULL,
    `title` varchar(255) NOT NULL,
    `calories` int(11) NOT NULL,
    `description` text NOT NULL,
    `contains_gluten` tinyint(1),
    `vegan_safe` tinyint(1),
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;
