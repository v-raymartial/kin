#  Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for
# full license information.
import functools
import json
import logging
import sys


class Logger:
    """
    A common logger class can be used for local, Spark or REST logging.  Logging level should have
    a default value. There are several constants defined in the class
    for various logging levels:  DEBUG, INFO, WARNING, ERROR, CRITICAL,
    FATAL, though not all of these are being used at this time.

    :param: name (str) -- a name for the logger instance
    :param: default_log_level (int) -- the logging level. Default is logging.INFO
    :param: filename (str) -- a name for the logfile to be written. Default is None
    :param: log_through_rest (bool) -- set to True if logging will be done using *** REST api. Default is False
    :param: log_through_spark (bool) -- set to True if logging will be done using spark. Default is False
    :param: log_to_json (bool) -- set to True if logging will be done using json format. Default is False
    :param: message_prefix (str) -- prefix added to the message. Default is empty
    """

    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL
    FATAL = logging.FATAL

    def __init__(
        self,
        name: str,
        default_log_level: int = logging.INFO,
        filename: str = None,
        log_through_rest=False,
        log_through_spark=False,
        log_to_json=False,
        message_prefix = ""
    ):
        """
        See class documentation for details
        """

        # we set py4j level to error because in the debug and info mode
        # will generate lots of fragmented debug info including socket data
        # info that will harden the debugging
        logging.getLogger("py4j").setLevel(self.ERROR)
        self.log_to_json = log_to_json
        #
        # older python approach using the built-in logger...
        #
        self.log_level = default_log_level
        self.name = name
        self.is_spark = log_through_spark
        self.log_rest = log_through_rest
        self.format = "%(asctime)s %(levelname)s - [%(name)s]:  %(message)s"
        self.message_prefix = message_prefix

        if not self.is_spark and not self.log_rest:
            self.local_logger = logging.getLogger(name)
            self.local_logger.propagate = False
            self.local_logger.setLevel(self.log_level)

            if filename is None:  # if we're logging to stdout
                if len(self.local_logger.handlers) == 0:
                    console_handler = logging.StreamHandler(stream=sys.stdout)
                    console_handler.setFormatter(
                        logging.Formatter(self.format)
                    )
                    self.local_logger.addHandler(console_handler)
            else:  # if we're logging to a file...
                if len(self.local_logger.handlers) == 0:
                    file_handler = logging.FileHandler(filename)
                    file_handler.setFormatter(logging.Formatter(self.format))
                    self.local_logger.addHandler(file_handler)
        elif self.log_rest:
            # TODO:
            raise NotImplementedError("log_rest not implemented")
        else:
            try:
                # TODO:
                raise NotImplementedError("is_spark not implemented")
            except Exception as e:
                print(
                    "Couldn't retrieve the spark logger, using standard logger"
                )
                self.is_spark = False
                self.local_logger = logging.getLogger(name)
                self.local_logger.setLevel(self.log_level)
                self.local_logger.propagate = False
                if len(self.local_logger.handlers) == 0:
                    console_handler = logging.StreamHandler(stream=sys.stdout)
                    console_handler.setFormatter(
                        logging.Formatter(self.format)
                    )
                    self.local_logger.addHandler(console_handler)

    def set_level(self, level: int):
        """
        A simple setter method for the logging level

        :param: level (int) -- one of the allowed levels

        @TODO: should check to verify that a valid level is being set
        otherwise an exception may be thrown or we may simply log into
        empty space

        """
        self.log_level = level
        if self.local_logger and callable(getattr(self.local_logger, "setLevel", None)):
            self.local_logger.setLevel(level)

    def debug(self, message, *args, **kwargs):
        """
        A utility method for posting log content at debug level. Delegates
        to post_data

        :param: message (string) -- the message payload
        :param: \\*args (a list of arguments) -- a list of arguments to accompany the message
        :param: \\*\\*kwargs (a list of argument pairs) -- a list of argument pairs to accompany the message

        """
        self.post_data(message, self.DEBUG, *args, **kwargs)

    def info(self, message, *args, **kwargs):
        """
        A utility method for posting log content at info level. Delegates
        to post_data

        :param: message (string) -- the message payload
        :param: \\*args (a list of arguments) -- a list of arguments to accompany the message
        :param: \\*\\*kwargs (a list of argument pairs) -- a list of argument pairs to accompany the message

        """
        self.post_data(message, self.INFO, *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        """
        A utility method for posting log content at warning level. Delegates
        to post_data

        :param: message (string) -- the message payload
        :param: \\*args (a list of arguments) -- a list of arguments to accompany the message
        :param: \\*\\*kwargs (a list of argument pairs) -- a list of argument pairs to accompany the message

        """
        self.post_data(message, self.WARNING, *args, **kwargs)

    def isEnabledFor(self, level=DEBUG) -> bool:
        """
        Is this logger enabled for level 'level'?
        This method can be used to prevent performing expensive computations (e.g. performing a count on a Spark
        DataFrame) which are only meant to be used for logging purposes, in log messages which might not even get
        logged because a certain logging level (e.g. DEBUG) is disabled for the current logger.

        :param: level (int) -- the logging level that is going to be used (default is DEBUG)
        :return: result (bool) -- a boolean indicating whether a log level has been enabled

        """
        return level >= self.log_level

    def exception(self, message, ex, traceback="", *args, **kwargs):
        """
        A utility method for errors. Delegates to self.error

        :param: message (str) -- the message payload
        :param: ex (Exception) -- the exception
        :param: traceback (str) -- the actual stack track to display
        :param: \\*args (list of arguments) -- a list of arguments to go with the message
        :param: \\*\\*kwargs (list of argument pairs) -- a list of argument pairs to go with the message

        """
        message = str(message) + " " + str(ex) + " " + traceback
        self.error(message, *args, **kwargs)

    def error(self, message, *args, **kwargs):
        """
        A utility method for posting log content at error level.
        Delegates to post_data

        :param: message (string) -- the message payload
        :param: \\*args (a list of arguments) -- a list of arguments
        :param: \\*\\*kwargs (a list of argument pairs) -- a list of argument pairs to go with the messsage

        """
        self.post_data(message, self.ERROR, *args, **kwargs)

    def post_data(self, message, level, *args, **kwargs):
        """
        A utility method for issuing the messages at the various levels

        :param: complete_message (str) -- the message payload for the log
        :param: level (int) -- the logging level to use
        :param: \\*args (list of arguments) -- a list of arguments
        :param: \\*\\*kwargs (list of argument pairs) -- a list of argument pairs

        """
        if not self.isEnabledFor(level):
            return

        message_prefix = f"[{self.message_prefix.lstrip()}] "
        complete_message = message
        
        if self.is_spark or self.log_rest:
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            if args:
                complete_message = complete_message % args

            if kwargs:
                complete_message = complete_message + ", ".join(kwargs_repr)

            if self.log_to_json:
                message_json = { "message": complete_message }
                complete_message = json.dumps(message_json)
            else:
                complete_message = f"{message_prefix}{complete_message}"

        if self.log_to_json:
            message_json = { "message": message }
            standard_logging_message = json.dumps(message_json)
        else:
            standard_logging_message = f"{message_prefix}{message}"

        if self.is_spark:
            try:
                self.local_logger.log(level, complete_message)
            except Exception as e:
                logging.getLogger().error("Error logging to spark logger", exc_info=e)
        elif self.log_rest:
            try:
                self.local_logger.log(level, complete_message)
            except Exception as e:
                logging.getLogger().error(f"Error logging to REST logger {type(self.local_logger)}", exc_info=e)
        else:
            self.local_logger.log(level, standard_logging_message, *args, **kwargs)

    @staticmethod
    def method_decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            self.logger.info(f"{func.__name__}:Started")
            try:
                result = func(self, *args, **kwargs)
            except Exception as e:
                self.logger.exception(f"{func.__name__}:Failed", e)
                raise e
            self.logger.info(f"{func.__name__}:Ended")
            return result
        return wrapper