from src.controller import controller
from src.helpers import helper, download

if __name__ == '__main__':
    args = helper.setup_parser()
    controller.Controller(args).main()
