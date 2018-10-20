import logging
import os 


# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')

# Variables (Temporary since these will be in a config file later)


def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    
    source_dir = "G:/"
    target_dir = "F:/"

    logger.info('Source Directory is: %s' % (source_dir))
    logger.info('Target Directory is: %s' % (target_dir))

    print( os.listdir(source_dir))
    print (os.listdir(target_dir))


if __name__== "__main__":
  main()