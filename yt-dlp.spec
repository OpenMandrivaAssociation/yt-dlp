# Errata
# Never use source from github. Use pypi instead. Source from GH require to compile pandoc.
# Pandoc is not available in Cooker and resurrection of it is hard and cause importing and fixing a lot of heavy packages like ghc.
# So let's skip it by use PyPi sources and force use py_build and py_install instead recommended by upstream makeinstall.


Name:		yt-dlp
Version:	2026.3.17
Release:	1
Summary:	A tool for downloading from video sites for offline watching
License:	Unlicense
Group:		Productivity/Video/Networking/Web/Utilities
URL:		https://github.com/yt-dlp/yt-dlp
Source:		https://pypi.python.org/packages/source/y/yt-dlp/yt_dlp-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	zip
BuildRequires:	tomcli

Requires:	ffmpeg
Requires:	python
Requires:	atomicparsley
Requires:	rtmpdump
# Can be used outside of mpv or mplayer, so lets disable this dep.
#Requires:       (mpv or mplayer)
# Not available yet in Cooker
#Requires:       phantomjs
# Deprecated but also not available in Cooker
#Requires:       sponskrub
Requires:	python%{pyver}dist(mutagen)
Requires:	python%{pyver}dist(pycryptodomex)
Requires:	python%{pyver}dist(pycryptodome)
Requires:	python%{pyver}dist(websockets)
Requires:	python%{pyver}dist(keyring)
Recommends:	aria2
Recommends:	curl
Recommends:	wget
Recommends:	quickjs

Provides:	python-yt-dlp = %{version}-%{release}
Provides:	python3-yt-dlp = %{version}-%{release}

%description
yt-dlp is a small command-line program to retrieve videos from
YouTube.com and other video sites for later watching.

A youtube-dl fork with additional features and fixes.

%package bash-completion
Summary:		Bash completion for %name
Group:			System/Shells
Recommends:		bash-completion
Supplements:	packageand(%name:bash)
BuildArch:		noarch

%description bash-completion
Bash command line completion support for %name.

%package fish-completion
Summary:		Fish completion for %name
Group:			System/Shells
Recommends:		fish
Supplements:	packageand(%name:fish)
BuildArch:		noarch

%description fish-completion
Fish command line completion support for %name.

%package zsh-completion
Summary:		Zsh Completion for %name
Group:			System/Shells
Recommends:		zsh
Supplements:	packageand(%name:zsh)
BuildArch:		noarch

%description zsh-completion
ZSH command line completion support for %name.

%prep -a
# fix hardcoded install path for README.txt
tomcli set pyproject.toml replace 'tool.hatch.build.targets.wheel.shared-data."README.txt"' "share/doc/yt_dlp/README.txt" 'share/doc/%{name}/README.txt'

%files
%{_docdir}/%{name}/README.txt
%{_bindir}/%name
%{python_sitelib}/yt_dlp
%{python_sitelib}/yt_dlp-%{version}.dist-info
%{_mandir}/man1/yt-dlp.1.*

%files bash-completion
%{_datadir}/bash-completion/

%files fish-completion
%_datadir/fish/

%files zsh-completion
%_datadir/zsh/
