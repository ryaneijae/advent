import os
import logging

from datetime import date, datetime, timedelta

home_dir = os.path.expanduser("~")
log_file_dir = f"{home_dir}Personal/logs"

def setup_logger(name):
    
    formatter= logging.Formatter(
        '%(asctime)s '
        '%(name)s %(levelname)s %(filename)s '
        '%(funcName)s (line: %(lineno)d) %(message)s'
    )
    
    logfile = log_file_dir + "/" + str(date.today()) + ".log"
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.ERROR)
    
    #file_handler = logging.FileHandler(logfile)
    stream_handler = logging.StreamHandler()

    #file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    #logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger


def clean_logs():
    logger = setup_logger(__name__)

    dir_list = os.listdir(log_file_dir)
    logger.debug(f'List of files found in {log_file_dir}: {dir_list}')

    to_be_removed = []
    for filename in dir_list:
        creation_date = datetime.strptime(
            filename.replace('.log',''), '%Y-%m-%d'
        ).date()
        
        days_since = date.today() - creation_date
        
        if days_since >= timedelta(days=60): to_be_removed.append(filename)

    logger.debug(f'Files Prepped to be removed: {to_be_removed}')

    for filename in to_be_removed:
        try:
            os.remove(log_file_dir + "/" + filename)
        except OSError:
            logger.exception(f'{filename} is a directory')
        except Exception as e:
            logger.exception(f'Unexpected Exception occurred while removing {filename}: {e}')

    logger.info("File Removal Complete")


def main():
    clean_logs()


if __name__ == '__main__':
    main()
