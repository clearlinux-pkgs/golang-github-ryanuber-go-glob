Name     : golang-github-ryanuber-go-glob
Version  : 0.1
Release  : 2
URL      : https://github.com/ryanuber/go-glob/archive/v0.1.tar.gz
Source0  : https://github.com/ryanuber/go-glob/archive/v0.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : go

%description
# String globbing in golang [![Build Status](https://travis-ci.org/ryanuber/go-glob.svg)](https://travis-ci.org/ryanuber/go-glob)

%prep
%setup -q -n go-glob-0.1

%build
export LANG=C

%install
rm -rf %{buildroot}
%global gopath /usr/lib/golang
%global library_path github.com/ryanuber/go-glob

# Copy all *.go and *.s files
install -d -p %{buildroot}%{gopath}/src/%{library_path}/
for ext in go s src golden template; do
    for file in $(find . -iname "*.$ext") ; do
        install -d -p %{buildroot}%{gopath}/src/%{library_path}/$(dirname $file)
        cp -pav $file %{buildroot}%{gopath}/src/%{library_path}/$file
    done
done

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export GOPATH=%{buildroot}%{gopath}
go test %{library_path}/... || :


%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/ryanuber/go-glob/glob.go
/usr/lib/golang/src/github.com/ryanuber/go-glob/glob_test.go
