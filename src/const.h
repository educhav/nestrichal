#pragma once

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>

#define GAME_WIDTH      640
#define GAME_HEIGHT     480
#define FPS		60

#ifdef _WIN_32
#define PATH_SEPARATOR "\\"
#else
#define PATH_SEPARATOR "/"
#endif
