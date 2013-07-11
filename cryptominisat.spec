Name:           cryptominisat
Version:        2.9.6
Release:        1
Summary:        SAT solver

# The Mersenne Twister implementation is BSD-licensed.
# All other files are MIT-licensed.
License:        MIT
URL:            http://www.msoos.org/cryptominisat2/
Source0:        https://gforge.inria.fr/frs/download.php/32160/cmsat-%{version}.tar.gz
Source1:	%{name}.rpmlintrc

BuildRequires:  zlib-devel
Requires:       %{name}-libs = %{version}-%{release}

%description
CryptoMiniSat is a SAT solver that aims to become a premiere SAT solver
with all the features and speed of successful SAT solvers, such as
MiniSat and PrecoSat.  The long-term goals of CryptoMiniSat are to be an
efficient sequential, parallel and distributed solver.  There are
solvers that are good at one or the other, e.g. ManySat (parallel) or
PSolver (distributed), but we wish to excel at all.

CryptoMiniSat 2.5 won the SAT Race 2010 among 20 solvers submitted by
researchers and industry.

%package devel
Summary:        Header files for developing with %{name}
Requires:       %{name}-libs = %{version}-%{release}

%description devel
Header files for developing applications that use %{name}.

%package libs
Summary:        Cryptominisat library

%description libs
The %{name} library.

%prep
%setup -q -n cmsat-%{version}

%build
%configure --disable-static
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -i libtool
sed -i 's|^LIBS =.*|LIBS = -lz -lgomp|' cmsat/Makefile
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*

%files devel
%{_includedir}/cmsat/
%{_libdir}/lib%{name}.so

%files libs
%doc AUTHORS LICENSE-MIT NEWS README TODO
%{_libdir}/lib%{name}-%{version}.so
