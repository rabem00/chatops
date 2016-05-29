#------------------------------------------------------------------------------#
#                                                                              #
#           Creating mattermost-team rpm package	                       #
#                                                                              #
#------------------------------------------------------------------------------#
DESTDIR = /
SERVICENAME = mattermost
PKGNAME = $(SERVICENAME)-team
VERSION = $(shell awk '$$2 == "_version" { print $$3 }' ${PKGNAME}.spec)
RELEASE = $(shell awk '$$2 == "_release" { print $$3 }' ${PKGNAME}.spec)
SRCDIR  = $(shell rpm --eval "%{_sourcedir}")
RPMDIR  = $(shell rpm --eval "%{_rpmdir}")
EXCLUDE = "\.git|\.svn|\.CVS|\.gitignore|\.svnignore|\.cvsignore"

all: package 

clean:
	@rm -f *.pyc *.pyo *~ *.bak *.o
	@rm -rf $(PKGNAME)-$(VERSION)

install:
	@# this will be called from the rpmbuild phase %install
	@mkdir -p $(DESTDIR)/etc/systemd/system
	@install -m 755 systemd/mattermost.service $(DESTDIR)/etc/systemd/system/$(SERVICENAME).service

package:
	@echo "Start packaging"
	@-rm -rf $(PKGNAME)-$(VERSION);
	@mkdir $(PKGNAME)-$(VERSION);
	@find . ! -name $(PKGNAME)-$(VERSION)| egrep -v $(EXCLUDE) | cpio -dump $(PKGNAME)-$(VERSION);
	@tar -czf $(SRCDIR)/$(PKGNAME)-$(VERSION).tar.gz $(PKGNAME)-$(VERSION);
	rpmbuild -bb $(PKGNAME).spec;

help:
	@echo "The follow tags are valid for make:"
	@awk '/^[a-zA-Z].*:/{print substr($$1,1,length($$1)-1)}' Makefile
