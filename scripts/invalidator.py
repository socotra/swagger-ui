#!/usr/bin/env python
import argparse
import boto


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--master_access_key',
                        help='Access key for master account')
    parser.add_argument('--master_secret_key',
                        help='Secret key for master account')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    c = boto.connect_cloudfront(
        args.master_access_key,
        args.master_secret_key)
    paths = ['/index.html']
    invalidation = c.create_invalidation_request(
        u'ERO5A1ICUUQLW',
        paths)
    print "created invalidation request: %s for paths: %s" % (invalidation.id,
                                                              paths)
    print 'this can take 10-15 minutes to propagate'
