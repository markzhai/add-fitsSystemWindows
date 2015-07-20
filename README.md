Add fitsSystemWindows in one-step
=================================

[SystemBarTint](https://github.com/jgilfelt/SystemBarTint) is a magnificent project that can easily enable translucent mode of our apps.

However, as my own experience on two old projects(started 3-4 years ago), add fitsSystemWindows is a hard-job, as we may have hundreds of thousands of layout files, some maybe useful, some are already outdated.

Add the attribute manually is meaningless and time-consuming, so I created this project to make this process automatically.

Usage
-----

Add fitsSystemWindows to all layout files, painlessly!

how to
------

Just put the python file at your android project's root directory, and run it.
It will ignore generated and hidden directories, so don't worry about that.
To re-format all layouts again, you can use the nice feature of android studio (reformat code on the whole layout folder).

customization
-------------
As my system is Chinese, I use GBK to decode directory, you may change it to your system's encoding.

dirDecodeEncoding = "gbk";  #change this line

contribution
-------------
Any contribution is welcome.

1. This script should be easily modified to support more android layout batch-edit mission.
2. Nice format of output xml is wanted.
