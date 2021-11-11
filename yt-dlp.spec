Name:           yt-dlp
Version:        2021.11.10.1
Release:        1
Summary:        A tool for downloading from video sites for offline watching
License:        CC-BY-SA-3.0 and Unlicensed
Group:          Productivity/Video/Networking/Web/Utilities
URL:            https://github.com/yt-dlp/yt-dlp
Source:         https://github.com/yt-dlp/yt-dlp/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  git
BuildRequires:  make
#BuildRequires:  pandoc
#BuildRequires:  python3dist(pypandoc)
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
BuildArch:      noarch

%description
yt-dlp is a small command-line program to retrieve videos from
YouTube.com and other video sites for later watching.

A youtube-dl fork with additional features and fixes.

%package        bash-completion
Summary:        Bash completion for %name
Group:          System/Shells
Requires:       bash-completion
Supplements:    packageand(%name:bash)
BuildArch:      noarch

%description    bash-completion
Bash command line completion support for %name.

%package        fish-completion
Summary:        Fish completion for %name
Group:          System/Shells
Requires:       fish
Supplements:    packageand(%name:fish)
BuildArch:      noarch

%description    fish-completion
Fish command line completion support for %name.

%package        zsh-completion
Summary:        Zsh Completion for %name
Group:          System/Shells
Requires:       zsh
Supplements:    packageand(%name:zsh)
BuildArch:      noarch

%description zsh-completion
ZSH command line completion support for %name.

%prep
%autosetup -p1

%build
#rm -f yt-dlp
#make_build
%py_build

%install
#make_install PREFIX="%_prefix" MANDIR="%_mandir"
%py_install

%files
%license LICENSE
%doc README.txt
%_bindir/%name
#_mandir/man1/%name.1%{?ext_man}

%files bash-completion
%_datadir/bash-completion/

%files fish-completion
%_datadir/fish/

%files zsh-completion
%_datadir/zsh/
