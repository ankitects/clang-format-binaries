# https://github.com/chromium/chromium/tree/81cc23a856578b149a37dd109b147d8544f9cbd8/buildtools

import subprocess
import dataclasses
import requests
import os


@dataclasses.dataclass
class Platform:
    path: str
    fname: str
    bazel_platform_name: str


commit = "81cc23a856578b149a37dd109b147d8544f9cbd8"

platforms = (
    Platform(
        path="linux64/clang-format.sha1",
        fname="clang-format",
        bazel_platform_name="linux_x86_64",
    ),
    Platform(
        path="mac/clang-format.sha1",
        fname="clang-format",
        bazel_platform_name="macos_x86_64",
    ),
    Platform(
        path="win/clang-format.exe.sha1",
        fname="clang-format.exe",
        bazel_platform_name="windows_x86_64",
    ),
)

for plat in platforms:
    hash_url = f"https://raw.githubusercontent.com/chromium/chromium/{commit}/buildtools/{plat.path}"
    hash = requests.get(hash_url).text

    subprocess.run(
        ["gsutil", "cp", f"gs://chromium-clang-format/{hash}", plat.fname], check=True
    )

    zipname = f"clang-format_{plat.bazel_platform_name}.zip"
    subprocess.run(["zip", zipname, plat.fname], check=True)
    os.unlink(plat.fname)

    print("Processed", plat)

print("Done")
