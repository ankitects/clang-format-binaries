# clang-format binaries

## Windows

Extracted from "Binaries for Windows installer (64-bit) (.sig), based on Git commit 6923b0a7 (28 August 2020).",
by installing, and copying the clang-format.exe file from the program files\llvm folder into a zip.

https://llvm.org/builds/

## MacOS

Extracted from homebrew bottle:

==> Downloading https://homebrew.bintray.com/bottles/clang-format-11.0.1.big_sur.bottle.1.tar.gz
==> Downloading from https://d29vzk4ow07wi7.cloudfront.net/210043c597e9bde9a3f0237c1c31a8ef7da945594bbe9ae19dd1dd3775188ca4?response-content-disposition=attachment%3Bfilename%3D%22clang-format-11.0.1.big
######################################################################## 100.0%
==> Pouring clang-format-11.0.1.big_sur.bottle.1.tar.gz

File was taken from /usr/local/bin and placed in a zip.

## Linux

Taken from the (semi-static) binary Chromium uses. Hash fetched from:

https://raw.githubusercontent.com/chromium/chromium/81cc23a856578b149a37dd109b147d8544f9cbd8/buildtools/linux64/clang-format.sha1

Then downloaded with:

gsutil cat gs://chromium-clang-format/1baf0089e895c989a311b6a38ed94d0e8be4c0a7 > clang-format

And marked as executable and zipped up.
