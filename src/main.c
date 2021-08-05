#include <SDL2/SDL.h>
#include <SDL2/SDL_timer.h>
#include <SDL2/SDL_image.h>
#include "const.h"

int main(int argc, char *argv[])
{

    if (SDL_Init(SDL_INIT_EVERYTHING) != 0) 
        printf("error initializing SDL: %s\n", SDL_GetError());

    SDL_Window* window = SDL_CreateWindow("Nestrichal", // creates a window
                                       SDL_WINDOWPOS_CENTERED, 
                                       SDL_WINDOWPOS_CENTERED,
                                       GAME_WIDTH, GAME_HEIGHT, 0);
    SDL_Renderer* rend = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    SDL_Surface* surface = IMG_Load("assets" PATH_SEPARATOR "Elijah.png");
    SDL_Texture* tex = SDL_CreateTextureFromSurface(rend, surface);
    SDL_FreeSurface(surface);
 
    // let us control our image position
    // so that we can move it with our keyboard.
    SDL_Rect player;
 
    // connects our texture with dest to control position
    player.w = 32;
    player.h = 32;
    SDL_QueryTexture(tex, NULL, NULL, &player.w, &player.h);
 
    // adjust height and width of our image box.
 
    player.x = (GAME_WIDTH - player.w) / 2;
    player.y = (GAME_HEIGHT - player.h) / 2;
 
    int speed = 300;
    bool running = true;
 
    while (running) {
        SDL_Event event;
        while (SDL_PollEvent(&event)) {
            switch (event.type) {
                case SDL_QUIT:
                    running = false;
                    break;
                case SDL_KEYDOWN:
                    switch (event.key.keysym.scancode) {
                    case SDL_SCANCODE_W:
                    case SDL_SCANCODE_UP:
                        player.y -= speed / 30;
                        break;
                    case SDL_SCANCODE_A:
                    case SDL_SCANCODE_LEFT:
                        player.x -= speed / 30;
                        break;
                    case SDL_SCANCODE_S:
                    case SDL_SCANCODE_DOWN:
                        player.y += speed / 30;
                        break;
                    case SDL_SCANCODE_D:
                    case SDL_SCANCODE_RIGHT:
                        player.x += speed / 30;
                        break;
                    default:
                        break;
                    }
            }
        }
 
        if (player.x + player.w > GAME_WIDTH)
            player.x = GAME_WIDTH - player.w;
 
        if (player.x < 0)
            player.x = 0;
 
        if (player.y + player.h > GAME_HEIGHT)
            player.y = GAME_HEIGHT - player.h;
 
        if (player.y < 0)
            player.y = 0;
 
        // clears the screen
        SDL_RenderClear(rend);
        SDL_RenderCopy(rend, tex, NULL, &player);
 
        // triggers the double buffers
        // for multiple rendering
        SDL_RenderPresent(rend);
        SDL_Delay(1000 / FPS);
    }
    SDL_DestroyTexture(tex);
    SDL_DestroyRenderer(rend);
    SDL_DestroyWindow(window);
    SDL_Quit();
}
