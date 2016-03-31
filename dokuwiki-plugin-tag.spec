%define		plugin		tag
Summary:	DokuWiki Tag Plugin
Name:		dokuwiki-plugin-%{plugin}
Version:	20160116
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/dokufreaks/plugin-tag/archive/39c0568/%{name}-%{version}.tar.gz
# Source0-md5:	cc1b3fd8eabd3fbf468d04e1c7e467b5
URL:		https://www.dokuwiki.org/plugin:tag
Requires:	dokuwiki >= 20131208
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
The Tag Plugin lets you assign category tags to wiki pages. It will
display a list of links to the tag pages in the tag namespace
specified in the configuration.

%prep
%setup -qc
mv *-%{plugin}-*/* .
rm -r _test

%build
version=$(awk '/^date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm $RPM_BUILD_ROOT%{plugindir}/{COPYING,README}

%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%dir %{plugindir}
%{plugindir}/*.css
%{plugindir}/*.js
%{plugindir}/*.php
%{plugindir}/*.txt
%{plugindir}/conf
%{plugindir}/images
%{plugindir}/syntax
