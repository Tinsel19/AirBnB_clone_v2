#!/usr/bin/python3
""" uses the do_pack and do_deploy functions for full deployment """


def deploy():
    """ full deployment """
    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False