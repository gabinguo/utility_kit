import logging

logging.root.setLevel(logging.NOTSET)

sep_vertical = u'\u2503'.encode('utf-8')
sep_horizontal = u'\u2500'.encode('utf-8')


def setup_logger(logger: logging.Logger, level: int = logging.INFO):
    if logger.hasHandlers():
        logger.handlers.clear()

    handler: logging.StreamHandler = logging.StreamHandler()
    formatter: logging.Formatter = logging.Formatter(
        fmt="%(asctime)s - %(module)s, L-%(lineno)d - [%(levelname)s] - %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S")
    handler.setFormatter(formatter)
    handler.setLevel(level)
    logger.addHandler(handler)


def log_map(logger: logging.Logger, title: str, kwargs: dict, width: int = 40, separator_h="═", separator_v="║"):
    max_key_len = max([len(key) for key in list(kwargs.keys())])
    max_value_len = max([len(value) for value in list(kwargs.values()) if isinstance(value, str)] or [8])
    max_len = max(max_key_len, max_value_len)
    while len(title) > width or max_len > width:
        width = int(width * 2)
    logger.info(f"{separator_h}{' ' * (width - 2)}{separator_h}")
    logger.info(f"╔{f' {title} ':{separator_h}^{width - 2}}╗")
    logger.info(f"{separator_v}{f'':^{width - 2}}{separator_v}")
    for key, value in kwargs.items():
        logger.info(f"{separator_v}{f'{key}: {value}':^{width - 2}}{separator_v}")
    logger.info(f"{separator_v}{f'':^{width - 2}}{separator_v}")
    logger.info(f"╚{'':{separator_h}^{width - 2}}╝")
    logger.info(f"{separator_h}{' ' * (width - 2)}{separator_h}")


def test_example():
    test_logger = logging.getLogger(__name__)
    setup_logger(test_logger)
    log_map(test_logger, title="Test Info",
            kwargs={"Argument-1": 1024, "Argument-2": 2048,
                    "Argument-3": "This_is_A_very_very_very_very_long_sequence"})


if __name__ == '__main__':
    test_example()
