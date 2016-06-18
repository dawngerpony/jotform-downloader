from src import jotformlib


def test_find_folder():
    print "Hello"
    client = jotformlib.JotformClient()
    client.download_all()
    print client.get_folders()
    print client.find_folder("CIAFF2016_DJ")
