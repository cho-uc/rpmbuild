Name:           rpm-test
Version:        1.0.0
Release:        1%{?dist}
Summary:        rpm-test
License:        GPLv2+
URL:            -
# No Source0 as we are using pre-built binaries
# Requires:       -


%description
rpm-test contains all required binaries for rpm test using rpm rebuild.
The all binaries should be packaged into a zip file to avoid being checking and modifying interpreter directives 
by rpmbuild

%prep
# we have no source, so nothing here

%build
rm -rf %{_builddir}/*
cat > hello-world.sh <<EOF
#!/usr/bin/bash
echo Hello world
EOF

%install
rm -rf %{buildroot}/*
mkdir -p %{buildroot}/opt/mycompany
cp -r %{_builddir}/* %{buildroot}/opt/mycompany/
cp -r %{_sourcedir}/* %{buildroot}/opt/mycompany/

# install -m 755 %{_builddir}/hello-world.sh %{buildroot}/opt/hello-world.sh
# install %{_builddir}/* -t %{buildroot}/opt/

%files
/opt/mycompany/*

# prevent BRP script from checking and modifying interpreter directives
%undefine __brp_mangle_shebangs

%post
cd /opt/com/
unzip git-v2.43.0-rc2.zip

%postun
rm -rf /opt/com/myfile

%clean
rm -rf %{buildroot}

%changelog
* Tue Jul 23 2024 First Lastname <first.last@mycompany.com> - 
- Initial package

