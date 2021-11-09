Name:           yt-dlp
Version:        2021.10.10
Release:        0
Summary:        A tool for downloading from video sites for offline watching
License:        CC-BY-SA-3.0 AND SUSE-Public-Domain
Group:          Productivity/Networking/Web/Utilities
URL:            https://github.com/yt-dlp/yt-dlp
#Git-Clone:     https://github.com/yt-dlp/yt-dlp
Source:         https://github.com/yt-dlp/yt-dlp/archive/%version.tar.gz#/%name-%version.tar.gz
Source1:        %name.changes
# Fix binary and man page paths in the Makefile -- Arachnos
Patch0:         0001-Fix-Makefile.patch
BuildRequires:  git
BuildRequires:  make >= 4
BuildRequires:  pandoc
BuildRequires:  python3-devel
BuildRequires:  python3-xml
BuildRequires:  zip
Requires:       ffmpeg
Requires:       python3
Requires:       python3-mutagen
Requires:       python3-pycryptodome
Requires:       python3-websockets
Requires:       python3-xml
Suggests:       python3-keyring
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
rm -f yt-dlp
PYTHON="%_bindir/python3" %make_build lazy-extractors
PYTHON="%_bindir/python3" %make_build

%install
%make_install PREFIX="%_prefix" MANDIR="%_mandir"

%files
%license LICENSE
%doc README.txt
%_bindir/%name
%_mandir/man1/%name.1%{?ext_man}

%files bash-completion
%_datadir/bash-completion/

%files fish-completion
%_datadir/fish/

%files zsh-completion
%_datadir/zsh/
