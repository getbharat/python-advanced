import logging
import logging.config

logging.config.fileConfig('loggging.conf')

logger = logging.getLogger('dev')

logger.info("Info Message")
