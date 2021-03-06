Name:		kafka
Version:	0.8.1.1
Release:	1%{?dist}
Summary:	Kafka is a distributed, partitioned, replicated message bus.

Group:		Communication/Message queue
License:	Apache 2.0
URL:		http://kafka.apache.org/
Source0:	http://apache.mirrors.lucidnetworks.net/kafka/0.8.1.1/kafka-0.8.1.1-src.tgz
Source1:    kafka.initd
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	java-1.7.0-openjdk-devel
BuildRequires:	tar
Requires:	java-1.7.0-openjdk

%description
Kafka is a distributed, partitioned, replicated commit log service. It provides the functionality of a messaging system, but with a unique design. 

%pre
grep kafka /etc/group > /dev/null|| groupadd kafka
grep kafka /etc/passwd > /dev/null || useradd -g kafka -r -d /opt/kafka kafka

%prep
rm -rf %{buildroot}/*
%setup -a 0 -qn %{name}-%{version}-src

%build
%{__mkdir} -p %{buildroot}/opt
%{__mkdir} -p %{buildroot}/etc/init.d
cp -pr %{name}-%{version}-src %{buildroot}/opt/%{name}-%{version}
%{__install} -m 0755 -p %SOURCE1 %{buildroot}/etc/init.d/kafka
mkdir %{buildroot}/opt/%{name}-%{version}/logs

%install
cd %{buildroot}/opt/%{name}-%{version}
./gradlew jar

%post
ln -f -s /opt/%{name}-%{version} /opt/%{name}
chown -R kafka:kafka /opt/%{name}-%{version}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/opt/%{name}-%{version}
/etc/init.d/kafka
%doc LICENSE NOTICE HEADER


%changelog
* Tue Oct 14 2014 Sebastien Le Digabel <sledigab@cisco.com> - 1.2
- Adding init file
* Tue Oct 14 2014 Sebastien Le Digabel <sledigab@cisco.com> - 1.1
- Adding user/group creation
* Mon Oct 13 2014 Sebastien Le Digabel <sledigab@cisco.com> - 1.0 
- initial spec file


