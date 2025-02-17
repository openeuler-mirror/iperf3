Name:           iperf3
Version:        3.10.1
Release:        1
Summary:        TCP,UDP,and SCTP network bandwidth measurement tool
License:        BSD
URL:            http://github.com/esnet/iperf
Source0:        http://downloads.es.net/pub/iperf/iperf-%{version}.tar.gz

BuildRequires:  libuuid-devel gcc

%description
Iperf is a tool for active measurements of the maximum achievable bandwidth
on IP networks. It supports tuning of various parameters related to timing,
protocols, and buffers.

%package        devel
Summary:        Header files for iperf3
Requires:       %{name} = %{version}-%{release}

%description    devel
Header files for iperf3

%package_help

%prep
%autosetup -n iperf-%{version} -p1

%build
%configure
%disable_rpath
%make_build

%install
%make_install -C src INSTALL_DIR="%{buildroot}%{_bindir}"
mkdir -p %{buildroot}%{_mandir}/man1
%delete_la_and_a

%files
%defattr(-,root,root)
%doc README.md RELNOTES.md
%license LICENSE _esnet/LICENSE
%{_bindir}/iperf3
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/iperf_api.h
%{_libdir}/*.so

%files help
%defattr(-,root,root)
%{_mandir}/man1/iperf3.1.gz
%{_mandir}/man3/libiperf.3.gz

%changelog
* Tue Jan 4 2022 liyanan <liyanan32@huawei.com> - 3.10.1-1
- Upgrade to 3.10.1

* Tue Nov 26 2019 openEuler Buildteam <buildteam@openeuler.org> - 3.6-4
- Package init
