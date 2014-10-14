Name:		kafka
Version:	0.8.1.1
Release:	1%{?dist}
Summary:	Kafka is a distributed, partitioned, replicated message bus.

Group:		Communication/Message queue
License:	Apache 2.0
URL:		http://kafka.apache.org/
Source0:	http://apache.mirrors.lucidnetworks.net/kafka/0.8.1.1/kafka-0.8.1.1-src.tgz
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
%setup -a 0 -qn %{name}-%{version}-src

%build
mkdir -p %{buildroot}/opt/%{name}-%{version}
cp -rp %{name}-%{version}-src %{buildroot}/opt/%{name}-%{version}
mkdir %{buildroot}/opt/%{name}-%{version}/logs

%install
cd %{buildroot}/opt/%{name}-%{version}
./gradlew jar
chown -R kafka:kafka %{buildroot}/opt/%{name}-%{version}

%post
cd /opt
ln -f -s %{name}-%{version} %{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/opt/%{name}-{version}
%doc LICENSE NOTICE HEADER


%changelog
* Mon Oct 13 2014 Sebastien Le Digabel <sledigab@cisco.com> - 1.0 
- initial spec file
* Tue Oct 14 2014 Sebastien Le Digabel <sledigab@cisco.com> - 1.1
- Adding user/group creation


