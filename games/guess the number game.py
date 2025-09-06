import pygame
import random
import sys


pygame.init()


screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Number Guessing Game")


olive_drab = (107, 142, 35)
white = (255, 255, 255)


clock = pygame.time.Clock()


difficulty = None
max_attempts = None
time_limit = None



def select_difficulty():
    global difficulty, max_attempts, time_limit
    selecting = True
    while selecting:
        screen.fill(olive_drab)
        title_text = pygame.font.Font(None, 40).render("Select Difficulty Level", True, white)
        option1 = pygame.font.Font(None, 30).render("1 - Easy (Unlimited attempts, 60 seconds)", True, white)
        option2 = pygame.font.Font(None, 30).render("2 - Medium (10 attempts, 45 seconds)", True, white)
        option3 = pygame.font.Font(None, 30).render("3 - Hard (5 attempts, 30 seconds)", True, white)

        screen.blit(title_text, (220, 150))
        screen.blit(option1, (180, 250))
        screen.blit(option2, (180, 300))
        screen.blit(option3, (180, 350))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = "Easy"
                    max_attempts = None
                    time_limit = 60
                    selecting = False
                elif event.key == pygame.K_2:
                    difficulty = "Medium"
                    max_attempts = 10
                    time_limit = 45
                    selecting = False
                elif event.key == pygame.K_3:
                    difficulty = "Hard"
                    max_attempts = 5
                    time_limit = 30
                    selecting = False
        clock.tick(60)



select_difficulty()


number_to_guess = random.randint(1, 100)
attempts = 0
input_text = ""
feedback = ""


start_ticks = pygame.time.get_ticks()

game_over = False

while not game_over:
    screen.fill(olive_drab)


    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    remaining_time = max(0, time_limit - elapsed_time) if time_limit is not None else 0


    timer_text = pygame.font.Font(None, 40).render(f"Time Left: {int(remaining_time)} sec", True, white)
    screen.blit(timer_text, (50, 50))


    instruction_text = pygame.font.Font(None, 30).render("Enter your guess (1-100):", True, white)
    screen.blit(instruction_text, (50, 120))


    input_box = pygame.Rect(50, 170, 200, 50)
    pygame.draw.rect(screen, white, input_box, 2)
    guess_surface = pygame.font.Font(None, 40).render(input_text, True, white)
    screen.blit(guess_surface, (input_box.x + 5, input_box.y + 5))


    feedback_surface = pygame.font.Font(None, 30).render(feedback, True, white)
    screen.blit(feedback_surface, (50, 250))


    if max_attempts is not None:
        attempts_surface = pygame.font.Font(None, 30).render(f"Attempts: {attempts} / {max_attempts}", True, white)
    else:
        attempts_surface = pygame.font.Font(None, 30).render(f"Attempts: {attempts}", True, white)
    screen.blit(attempts_surface, (50, 300))

    pygame.display.flip()


    if remaining_time <= 0:
        feedback = f"Time's up! The correct number was {number_to_guess}."
        game_over = True


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if input_text.isdigit():
                    guess = int(input_text)
                    attempts += 1
                    if guess < number_to_guess:
                        feedback = "Too low!"
                    elif guess > number_to_guess:
                        feedback = "Too high!"
                    else:
                        feedback = f"Congratulations! The correct number was {number_to_guess}."
                        game_over = True
                    if max_attempts is not None and attempts >= max_attempts and guess != number_to_guess:
                        feedback = f"Out of attempts! The correct number was {number_to_guess}."
                        game_over = True
                else:
                    feedback = "Please enter a valid number."
                input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                if event.unicode.isdigit():
                    input_text += event.unicode

    clock.tick(30)


screen.fill(olive_drab)
final_text = pygame.font.Font(None, 40).render(feedback, True, white)
screen.blit(final_text, (50, 250))
pygame.display.flip()
pygame.time.delay(3000)
pygame.quit()