Name:           binutils-isem
Version:        2.17.50.0.9
Release:        %mkrel 1
Epoch:          0
Summary:        GNU Binary Utility Development Utilities for tkisem
URL:            http://qa.mandriva.com/
License:        GPL
Group:          Development/Other
Requires:       cross-sun4-binutils = %{version}
BuildRequires:  cross-sun4-binutils = %{version}
BuildArch:      noarch

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

While it is true that tkisem could be modified to use the binaries
directly, this makes it easier to match upstream code and documentation.
EOF

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.isem
%{_bindir}/isem_as
%{_bindir}/isem_ld

