import logging

def main():
    log_file = "cf9.log"
    file_handler = logging.FileHandler(log_file, mode='a')
    handlers = [file_handler]
    logger = logging.getLogger("search-app")

    logging.basicConfig(
        handlers=handlers,
        level=logging.INFO,
        format="%(asctime)s:%(levelname)s:%(name)s:%(message)s"
    )

    nums = [10, 20, 30, 40, 50]
    num_to_find = 1200

    try:
        index  = nums.index(num_to_find)
        print(f"Fount at index: {index}")
    except ValueError as e:
        logger.error(f"Error occured: {e}.\n{num_to_find} not in the list.", exc_info=True)

if __name__ == "__main__":
    main()