#include "const.h"

enum game_states { MENU, NORMAL };
enum sprite_states { SFRONT, SBACK, SLEFT, SRIGHT, 
					 DFRONT, DBACK, DLEFT, DRIGHT };

typedef struct {
    uint32_t x, y;
	uint32_t size;
	char* sprites[];
} Sprite;

typedef struct {
	float velocity;
	float hp;
	Sprite sprite;
} Player;

typedef struct {
	int scene_number;
} Scene;

typedef struct {
} Game;
