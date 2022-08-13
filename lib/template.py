
# Autoreload packages when personnal packages are in development

DEV_MODE = 1
if DEV_MODE:
    %load_ext autoreload
    %autoreload 2



warnings.warn(
    "Kernel only supports one shell stream. Additional streams will be ignored. J'écris mon warning",
    RuntimeWarning,
    stacklevel=2,
)