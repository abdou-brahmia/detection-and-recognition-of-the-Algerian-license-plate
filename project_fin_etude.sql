-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le :  ven. 09 oct. 2020 à 00:12
-- Version du serveur :  10.4.8-MariaDB
-- Version de PHP :  7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `project_fin_etude`
--

-- --------------------------------------------------------

--
-- Structure de la table `voiture_client`
--

CREATE TABLE `voiture_client` (
  `matricule_client` varchar(10) NOT NULL,
  `nom_client` varchar(20) NOT NULL,
  `prenom_client` varchar(20) NOT NULL,
  `telephone_client` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `voiture_client`
--

INSERT INTO `voiture_client` (`matricule_client`, `nom_client`, `prenom_client`, `telephone_client`) VALUES
('0167011824', 'Zaim', 'zamitti', '0664493937');

-- --------------------------------------------------------

--
-- Structure de la table `voiture_entrer`
--

CREATE TABLE `voiture_entrer` (
  `id` int(11) NOT NULL,
  `matricule_entrer` varchar(10) NOT NULL,
  `date_entre` date NOT NULL,
  `heure_entrer` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `voiture_entrer`
--

INSERT INTO `voiture_entrer` (`id`, `matricule_entrer`, `date_entre`, `heure_entrer`) VALUES
(161, '0167011824', '2020-10-08', '00:01:40');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `voiture_client`
--
ALTER TABLE `voiture_client`
  ADD PRIMARY KEY (`matricule_client`);

--
-- Index pour la table `voiture_entrer`
--
ALTER TABLE `voiture_entrer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `matricule_entrer` (`matricule_entrer`,`date_entre`,`heure_entrer`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `voiture_entrer`
--
ALTER TABLE `voiture_entrer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=165;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
