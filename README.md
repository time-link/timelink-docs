This folder is the official documentation of Timelink.

This is produced with [Material for MKDocs](https://squidfunk.github.io/mkdocs-material/)

## Publishing

The directory `docs` is  published as  GitHub Pages when pushed in the `main` branch. See https://squidfunk.github.io/mkdocs-material/publishing-your-site/

## Defining the sections and navigation

We use  [Awesome Nav](https://lukasgeiter.github.io/mkdocs-awesome-nav/) to define the structure of the table of contents. See  https://lukasgeiter.github.io/mkdocs-awesome-nav/features/nav/ and check the file `.nav.yml` at the root of this directory.

Some subdirectories also have their `.nav.yml` fiiles. This file basically defines the order of the files in the Navigation settings.

Also options for features in the sections side-bar in https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation

Note than _table of contents_ in MKDocs refers to the structure of a page as defined by usage of '#' and is shown on the right of the page.

## Style guidelines

1. Folders and files should have _ instead of spaces in the name, so as to generate clean urls.
2. Use always lower case in directory and file names.
3. If renaming from upper to lower without other changes in case insensitive OS like MacOS, note that git does not recognise the change, and intermediate renaming is necessary see: https://www.perplexity.ai/search/a41f3bd3-65de-41f4-92d2-6cc29e56518a
4. Files should have a '#' title to override the default filename during rendering

## Todo

- [ ] add comment system see https://squidfunk.github.io/mkdocs-material/setup/adding-a-comment-system/

See ongoing result in github pages: https://time-link.github.io/timelink-docs/
