# tas_tools_misc
Misc tools and artifacts for GDQ

## Relevant Repos

### SmashBot and TAS Playing

The main logic of the run takes place from within SmashBot.
https://github.com/altf4/SmashBot/tree/tastm32-allstar

There's also a "plain" version of the SmashBot repo that doesn't have any of the DTM playing, and it more suitable for just playing against SmashBot. These two repos will merge soon though:
https://github.com/altf4/SmashBot/tree/tastm32

### Libmelee
Both repos require a custom version of libmelee with some features not in the mainline pip version.
https://github.com/altf4/libmelee/tree/tastm32-allstar

In order to "install" the libmelee above, the easiest way is to copy-paste the `melee` folder from libmelee into SmashBot.

### ASM
The custom Slippi ASM is here:
https://github.com/altf4/slippi-ssbm-asm/tree/exi-hw-test
(using the console output of course)

### GCI Building
The ASM is built into a GCI (memory card save file) using a fork of Dan Salvato's GCI compiler:
