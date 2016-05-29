# Required build directory
%define _topdir		%(echo $HOME)/rpmbuild
%define service         mattermost
%define _name		%{service}-team
%define _version	3.0.3
%define _release	1
%define _packager	%(echo "$USER") <%(echo "$USER")@yourdomain.com>
%define _vendor		Mattermost
%define _license	MIT

BuildArchitectures:     x86_64
BuildArch:              x86_64


Name:			%{_name}
Version:		%{_version}
Release:		%{_release}
License:		%{_license}
Group:			Applications/System
Packager:		%{_packager}
Vendor:			%{_vendor}
Source:			%{name}-%{version}.tar.gz
Summary:		%{_vendor} %{_name}
BuildRoot:		%{_topdir}/BUILDROOT/%{name}-%{version}
Prefix:			%{_prefix}
Requires:		postgresql-server
Requires:		postgresql-contrib

#--------------------------------------------------------------------#
# Description                                                        #
#--------------------------------------------------------------------#
%description
The %{name} example service.

-------------------------------------------------------------------------

#--------------------------------------------------------------------#
# Prepare                                                            #
#--------------------------------------------------------------------#
%prep
%setup

#--------------------------------------------------------------------#
# Build                                                              #
#--------------------------------------------------------------------#
#%build

#--------------------------------------------------------------------#
# Install                                                            #
#--------------------------------------------------------------------#
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

mkdir -p %{buildroot}/opt/

tar -xf %{name}-%{version}-linux-amd64.tar.gz
mv mattermost %{buildroot}/opt/

cd %{buildroot}

# find in dir but exclude topdir in filelist
find opt ! -path opt -type d -exec echo %dir \"/{}\" \; > /tmp/file.list.%{_name}

for file in $(find opt -type f)
do
        if [ ${file: -5} == ".json" ]
        then
                echo %config /${file}  >> /tmp/file.list.%{_name}
        else
                echo /${file}  >> /tmp/file.list.%{_name}
        fi
done

#--------------------------------------------------------------------#
# Pre install script                                                 #
#--------------------------------------------------------------------#
%pre
if [ $1 -eq 1 ] ; then
	# add the "mattermost" group and user
	getent group mattermost >/dev/null || groupadd -r mattermost 
	getent passwd mattermost >/dev/null || \
	useradd -r -g mattermost -d /opt/mattermost \
	    -s /sbin/nologin -c "Mattermost " mattermost

fi
#--------------------------------------------------------------------#
# Post install script                                                #
#--------------------------------------------------------------------#
%post

#--------------------------------------------------------------------#
# Pre uninstall script                                               #
#--------------------------------------------------------------------#
%preun

#--------------------------------------------------------------------#
# Post uninstall script                                              #
#--------------------------------------------------------------------#
%postun
if [ $1 -eq 0 ] ; then
	# remove the "mattermost" group and user
	getent passwd mattermost >/dev/null && userdel mattermost
	getent group mattermost >/dev/null && groupdel mattermost 
fi

#--------------------------------------------------------------------#
# Clean up after the build                                           #
#--------------------------------------------------------------------#
%clean
rm -rf %{buildroot}

#--------------------------------------------------------------------#
# File list                                                          #
#--------------------------------------------------------------------#
%files -f /tmp/file.list.%{_name}
%defattr(-, mattermost, mattermost,-)
%attr(644,root,root) /etc/systemd/system/%{service}.service
%ghost /opt/mattermost/logs/mattermost.log

#--------------------------------------------------------------------#
# Changelog                                                          #
#--------------------------------------------------------------------#
%changelog
* Sun May 29 2016 goosj at github
- Created initial package for %{name} installation

