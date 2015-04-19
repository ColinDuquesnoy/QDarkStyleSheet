#! /bin/bash

# package info
ppa="ppa:colin-duquesnoy/experimental"
name="qdarkstyle"
version="1.16"
debian_version=1

# read pgp key from gpg_key file
gpg_key=`cat gpg_key`

# generate debian source package and .orig.tar.gz
python3 setup.py --command-packages=stdeb.command sdist_dsc --suite trusty --debian-version ${debian_version}

# sign our package and prepare it for ppa upload
pushd deb_dist
dpkg-source -x ${name}_${version}-${debian_version}.dsc
pushd ${name}-${version}
debuild -S -sa -k${gpg_key}
popd

# upload to ppa
dput ${ppa} *.changes
popd

# cleanup
rm -rf *.tar.gz deb_dist/ dist/
