# rpmbuild

## Source
- https://rogerwelin.github.io/rpm/rpmbuild/2015/04/04/rpmbuild-tutorial-part-1.html
- https://linuxconfig.org/how-to-modify-an-rpm-package-using-rpmrebuild

## Directory Structure
rpmbuild:
- BUILD
- RPMS
- SOURCES
- SPECS
- SRPMS


## Preparation
- sudo yum install -y rpmdevtools rpmlint

## Building and running
- *rpmbuild -bb rpmbuild/SPECS/rpm-test.spec*
- To edit a generated RPM, use rpmrebuild: *rpmrebuild -enp myfile.rpm*

