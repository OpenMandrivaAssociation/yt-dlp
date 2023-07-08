# Errata
# Never use source from github. Use pypi instead. Source from GH require to compile pandoc.
# Pandoc is not available in Cooker and resurrection of it is hard and cause importing and fixing a lot of heavy packages like ghc.
# So let's skip it by use PyPi sources and force use py_build and py_install instead recommended by upstream makeinstall.


Name:           yt-dlp
Version:        2023.7.6
Release:        1
Summary:        A tool for downloading from video sites for offline watching
License:        CC-BY-SA-3.0 and Unlicensed
Group:          Productivity/Video/Networking/Web/Utilities
URL:            https://github.com/yt-dlp/yt-dlp
Source:         https://pypi.python.org/packages/source/y/yt-dlp/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  zip

Requires:       ffmpeg
Requires:       python
Requires:       atomicparsley
Requires:       rtmpdump
Requires:       mplayer
Requires:       mpv
# Not available yet in Cooker
#Requires:       phantomjs
# Deprecated but also not available in Cooker
#Requires:       sponskrub
Requires:       python3dist(mutagen)
Requires:       python3dist(pycryptodomex)
Requires:       python3dist(pycryptodome)
Requires:       python3dist(websockets)
Requires:       python3dist(keyring)
Recommends:     aria2
Recommends:     curl
Recommends:     wget
BuildArch:      noarch

Provides:       python-yt-dlp
Provides:       python3-yt-dlp

%description
yt-dlp is a small command-line program to retrieve videos from
YouTube.com and other video sites for later watching.

A youtube-dl fork with additional features and fixes.

%package        bash-completion
Summary:        Bash completion for %name
Group:          System/Shells
Recommends:       bash-completion
Supplements:    packageand(%name:bash)
BuildArch:      noarch

%description    bash-completion
Bash command line completion support for %name.

%package        fish-completion
Summary:        Fish completion for %name
Group:          System/Shells
Recommends:       fish
Supplements:    packageand(%name:fish)
BuildArch:      noarch

%description    fish-completion
Fish command line completion support for %name.

%package        zsh-completion
Summary:        Zsh Completion for %name
Group:          System/Shells
Recommends:       zsh
Supplements:    packageand(%name:zsh)
BuildArch:      noarch

%description zsh-completion
ZSH command line completion support for %name.

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

# fix from ROSA
# installed as %%doc into standard location
#unlink %{buildroot}%{_datadir}/doc/yt_dlp/README*
#rmdir %{buildroot}%{_datadir}/doc/yt_dlp
#rmdir %{buildroot}%{_datadir}/doc

%files
%license LICENSE
%doc README*
%doc %{_datadir}/doc/yt_dlp/README.txt
%{_bindir}/%name
%{python_sitelib}/yt_dlp
%{python_sitelib}/yt_dlp-%{version}.dist-info
#{python_sitelib}/devscripts/
%{_mandir}/man1/yt-dlp.1.*

%files bash-completion
%{_datadir}/bash-completion/

%files fish-completion
%_datadir/fish/

%files zsh-completion
%_datadir/zsh/
