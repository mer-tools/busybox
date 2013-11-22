Summary: Single binary providing simplified versions of system commands
Name: busybox
Version: 1.21.0
Release: 1
License: GPLv2
Group: System/Shells
Source0: %{name}-%{version}.tar.bz2
Source1: busybox_config
URL: https://github.com/mer-tools/busybox 

%define debug_package %{nil}

%description
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.  This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries.

This package contains only the busybox binary

#%package all
#Group: System/Shells
#Summary: Busybox symlinks

#%%description all
#This package contains all the busybox symlinks

%package docs
Group: Documentation
Summary: Busybox Documentation

%description docs
Busybox documentation and user guides

%prep
# Adjusting %%setup since git-pkg unpacks to src/
# %%setup -q -n %%{name}-%%{version}/%%{name}
%setup -q -n src

%build
cp %{SOURCE1} .config
#make defconfig
make %{_smp_mflags}
#make busybox.links

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/bin
install -m 755 busybox %{buildroot}/bin/busybox
#applets/install.sh %{buildroot} --symlinks

%files
%defattr(-,root,root,-)
%doc LICENSE
/bin/busybox

%files docs
%defattr(-,root,root,-)
%doc LICENSE docs/busybox.net/*.html

#%%files all
#%%defattr(-,root,root,-)
#%%exclude /bin/busybox
#/bin/*
#%%{_bindir}*
#/sbin/*
#%%{_sbindir}*
#/linuxrc
