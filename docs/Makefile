SPHINXBUILD ?= sphinx-build
SOURCEDIR = source
BUILDDIR = _build

.PHONY: html linkcheck clean
html:
	python ../scripts/sync_assets.py
	$(SPHINXBUILD) -W --keep-going -b html $(SOURCEDIR) $(BUILDDIR)/html
linkcheck:
	python ../scripts/sync_assets.py
	$(SPHINXBUILD) -W --keep-going -b linkcheck $(SOURCEDIR) $(BUILDDIR)/linkcheck
clean:
	rm -rf $(BUILDDIR) $(SOURCEDIR)/_static/generated
