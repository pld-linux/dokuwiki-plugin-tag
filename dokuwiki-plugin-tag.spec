%define		plugin		tag
Summary:	DokuWiki Tag Plugin
Name:		dokuwiki-plugin-%{plugin}
Version:	20080707
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.chimeric.de/_src/plugin-tag.tgz
# Source0-md5:	6f9bc7915fc273a161c093ce525f0abc
Source1:	dokuwiki-find-lang.sh
URL:		http://www.dokuwiki.org/plugin:tag
Requires:	dokuwiki >= 20070626
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
The Tag Plugin lets you assign category tags to wiki pages. It will
display a list of links to the tag pages in the tag namespace
specified in the configuration.

%prep
%setup -q -n %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm -f $RPM_BUILD_ROOT%{plugindir}/{COPYING,README,VERSION}

# find locales
sh %{SOURCE1} %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README VERSION
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.css
%{plugindir}/*.js
%{plugindir}/conf
%{plugindir}/images
%{plugindir}/syntax
