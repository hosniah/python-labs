import logging

def main():
    logging.basicConfig(filename='myapp.csv', filemode='w', format='%(levelname)s;%(asctime)s;%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    logging.debug('Information détaillée, intéressante seulement lorsqu''on diagnostique un problème.')
    logging.info('Confirmation que tout fonctionne comme prévu.')
    logging.warning('L''indication que quelque chose d''inattendu a eu lieu, ou de la possibilité d''un problème dans un futur proche (par exemple « espace disque faible »). Le logiciel fonctionne encore normalement.')
    logging.error('Du fait d''un problème plus sérieux, le logiciel n''a pas été capable de réaliser une tâche.')
    logging.critical('Une erreur sérieuse, indiquant que le programme lui-même pourrait être incapable de continuer à fonctionner.')

if __name__ == '__main__':
    main()