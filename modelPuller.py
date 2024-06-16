import apps
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Model Puller",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-n", "--modelname", help="model name")
    parser.add_argument("-a", "--alias", help="alias")
    parser.add_argument("-d", "--dst-path", 
            help="""Path of the local filesystem destination directory
                    to which to download the specified artifacts. If
                    the directory does not exist, it is created. If
                    unspecified the artifacts are downloaded to a new
                    uniquely-named directory on the local filesystem,
                    unless the artifacts already exist on the local
                    filesystem, in which case their local path is
                    returned directly""")
    args = parser.parse_args()
    params = vars(args)

    apps.download_model(params['modelname'], params['alias'])

if __name__ == "__main__":
    main()