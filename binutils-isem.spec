%define name	binutils-isem
%define version	%(rpm -q --queryformat "%{VERSION}" cross-sun4-binutils)
%define release	%mkrel 1

Summary:	GNU Binary Utility Development Utilities for tkisem
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Other
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:	cross-sun4-binutils
BuildRequires:	cross-sun4-binutils 

%description
This package simply provides symlinks from %{_bindir}/sun4-linux-as and 
%{_bindir}/sun4-linux-ld to isem_as and isem_ld, respectively. These 
symlinks are needed for the tkisem package.

%prep
%setup -q -c -T

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__ln_s} %{_bindir}/sun4-linux-as %{buildroot}%{_bindir}/isem_as
%{__ln_s} %{_bindir}/sun4-linux-ld %{buildroot}%{_bindir}/isem_ld

%{__cat} >> README.isem << EOF
This package simply provides symlinks from %{_bindir}/sun4-linux-as and 
%{_bindir}/sun4-linux-ld to isem_as and isem_ld, respectively. These 
symlinks are needed for the tkisem package.
EOF

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.isem
%{_bindir}/isem_as
%{_bindir}/isem_ld

